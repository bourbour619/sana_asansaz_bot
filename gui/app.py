# This Python file uses the following encoding: utf-8
import shutil
import os
import time
import base64
import PyPDF2
import pandas as pd
import qtawesome as qta
from pathlib import Path
from functools import partial
from typing import List
from pydantic import ValidationError
from sqlalchemy import select
import sqlalchemy.exc as alch_exc
from dotenv import load_dotenv

from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget,
                                QListWidget, QListWidgetItem, QTableWidgetItem, QHeaderView,
                                 QFileDialog, QToolButton, QHBoxLayout, QLabel)
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt, Slot, Signal, QByteArray, QBuffer, QIODevice, QSize, QTimer, QThread, QEventLoop

from core import schemas, models, database, repository, driver


from .main_window import Ui_mainWindow
from .new_post import Ui_newPost
from .message_dialog import Ui_messageDialog
from .send_post import Ui_sendPost


base_dir = Path(__file__).resolve().parent.parent

load_dotenv()

db = database.DB()
    

class IconThroughText:

    @staticmethod
    def render(text, icon, size=24):
        pixmap = icon.pixmap(size, size)  # Convert QIcon to QPixmap
        image = pixmap.toImage()  # Convert QPixmap to QImage

        # Create a QByteArray and QBuffer
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)  # Open buffer in write mode

        # Save QImage to buffer in PNG format
        image.save(buffer, "PNG")

        # Convert buffer to Base64
        base64_data = base64.b64encode(byte_array.data()).decode()

        return f'''
    <table align="center">
        <tr>
            <td align="center">
                <img src="data:image/png;base64,{base64_data}">
            </td>
            <td align="center" style="padding-bottom: .5em;">
                {text}
            </td>
        </tr>
    </table>
'''


class MessageDialog(QWidget):
    def __init__(self, type, message):
        super(MessageDialog, self).__init__()
        self.ui = Ui_messageDialog()
        self.ui.setupUi(self)
        self.setFixedSize(400, 159)
        icon = None
        if type == 'error':
            self.setWindowTitle('خطا')
            icon = qta.icon('mdi.close')
        elif type == 'success':
            self.setWindowTitle('موفقیت')
            icon = qta.icon('mdi.check')
        elif type == 'warn':
            self.setWindowTitle('هشدار')
            icon = qta.icon('mdi.alert')
        self.setWindowIcon(icon)
        text = IconThroughText.render(message, icon)
        self.ui.messageText.setText(text)


class MainWindow(QWidget):

    _posts: List[models.Post] = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1126, 627)
        self.setWindowIcon(QIcon(str(base_dir / 'staticfiles/adliran.ico')))
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.newPostBtn.setIcon(qta.icon('mdi.plus-box'))
        self.ui.newPostBtn.setIconSize(QSize(20, 20))
        self.ui.searchBtn.setIcon(qta.icon('mdi.magnify'))
        self.ui.searchBtn.setIconSize(QSize(20, 20))
        self.ui.postsTable.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.postsTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        for i in range(1, self.ui.postsTable.columnCount()):
            self.ui.postsTable.horizontalHeader().setSectionResizeMode(
                i, QHeaderView.ResizeMode.Stretch)
        self.ui.newPostBtn.clicked.connect(self.ui_new_post)
        self.fetch_all_posts()

    def fetch_all_posts(self):
        with db.get_session() as session:
            self._posts = session.scalars(select(models.Post)).all()
            self.ui.postsTable.setRowCount(len(self._posts))
            for i, post in enumerate(self._posts[::-1]):
                title = QTableWidgetItem(post.title)
                self.ui.postsTable.setItem(i, 0, title)
                date = QTableWidgetItem(post.date)
                self.ui.postsTable.setItem(i, 1, date)
                status = QTableWidgetItem(post.status.value)
                self.ui.postsTable.setItem(i, 3, status)
                items_count = QTableWidgetItem(str(post.items_count))
                self.ui.postsTable.setItem(i, 2, items_count)
                send_button = QToolButton()
                send_button.setIcon(qta.icon('mdi.play-circle'))
                send_button.setIconSize(QSize(20, 20))
                send_button.clicked.connect(
                    partial(self.ui_send_post, post.date))
                edit_button = QToolButton()
                edit_button.setIcon(qta.icon('mdi.lead-pencil'))
                edit_button.setIconSize(QSize(20, 20))
                delete_button = QToolButton()
                delete_button.setIcon(qta.icon('mdi.delete-forever'))
                delete_button.setIconSize(QSize(20, 20))
                delete_button.clicked.connect(
                    partial(self.delete_post, post.date))
                button_layout = QHBoxLayout()
                button_layout.addWidget(send_button)
                button_layout.addWidget(edit_button)
                button_layout.addWidget(delete_button)
                button_widget = QWidget()
                button_widget.setLayout(button_layout)
                self.ui.postsTable.setCellWidget(i, 8, button_widget)
                self.ui.postsTable.resizeRowToContents(i)

    @Slot(str)
    def delete_post(self, post_date):
        with db.get_session() as session:
            post = repository.PostRepository.delete(session, post_date)
            try:
                shutil.rmtree(base_dir / 'data' / post.title)
            except FileNotFoundError:
                pass
        self.fetch_all_posts()

    @Slot()
    def ui_new_post(self):
        self.new_post = NewPost()
        self.new_post.setFixedSize(1126, 627)
        self.new_post.setGeometry(
            640, 280, self.new_post.width(), self.new_post.height())
        self.new_post.show()
        self.new_post._created.connect(self.post_created)
        self.new_post._drafted.connect(self.post_drafted)

    @Slot(str)
    def ui_send_post(self, post_date):
        post: models.Post = None
        with db.get_session() as session:
            post = session.get(models.Post, post_date)
            if post is not None:
                self.send_post = SendPost(post)
                self.send_post.setFixedSize(600, 500)
                self.send_post.setGeometry(
                    640, 280, self.send_post.width(), self.send_post.height())
                self.send_post.show()

    @Slot()
    def post_created(self):
        self.new_post.close()
        self.fetch_all_posts()

    @Slot()
    def post_drafted(self):
        self.fetch_all_posts()


class NewPost(QWidget):

    _drafted = Signal((bool),)
    _created = Signal((bool),)
    _excel_df: pd.DataFrame = None
    _post_object: models.Post = None
    _sana_item_objects: List[models.SanaItem] = list()

    def __init__(self):
        super(NewPost, self).__init__()
        self.setFixedSize(1126, 627)
        self.setWindowIcon(QIcon(str(base_dir / 'staticfiles/adliran.ico')))
        self.ui = Ui_newPost()
        self.ui.setupUi(self)
        self.ui.createDraftBtn.setIcon(qta.icon('mdi.content-save'))
        self.ui.createDraftBtn.setIconSize(QSize(20, 20))
        self.ui.createFinalBtn.setIcon(qta.icon('mdi.content-save-move'))
        self.ui.createDraftBtn.setIconSize(QSize(20, 20))
        # All count label
        icon = qta.icon('mdi.file')
        text = IconThroughText.render(self.ui.allCountLabel.text(), icon, 20)
        self.ui.allCountLabel.setText(text)
        # Valid count label
        icon = qta.icon('mdi.check')
        text = IconThroughText.render(self.ui.validCountLabel.text(), icon, 20)
        self.ui.validCountLabel.setText(text)
        # Invalid count label
        icon = qta.icon('mdi.close-circle')
        text = IconThroughText.render(
            self.ui.invalidCountLabel.text(), icon, 20)
        self.ui.invalidCountLabel.setText(text)
        # Uploaded count label
        icon = qta.icon('mdi.cloud-upload')
        text = IconThroughText.render(
            self.ui.uploadedCountLabel.text(), icon, 20)
        self.ui.uploadedCountLabel.setText(text)
        self.ui.sanaItemsTable.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.sanaItemsTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        self.ui.createDraftBtn.clicked.connect(self.new_draft_post)
        self.ui.createFinalBtn.clicked.connect(self.new_final_post)
        self.ui.showExampleExcelBtn.clicked.connect(self.show_example_excel)
        self.ui.uploadExcelBtn.clicked.connect(self.upload_excel)
        self.ui.uploadFilesBtn.clicked.connect(self.upload_and_merge)
        self.ui.validateBtn.clicked.connect(self.validate)

    @Slot()
    def new_draft_post(self):
        date_input = self.ui.dateInput.text()
        try:
            post = schemas.CreatePost(
                date=date_input, status=schemas.PostStatus.Draft)
            self.ui.titleInput.setText(post.title)
            self._post_object = models.Post(title=post.title,
                                            date=post.date,
                                            status=models.PostStatus(
                                                post.status.value),
                                            items=[])
            with db.get_session() as session:
                try:
                    session.add(self._post_object)
                    session.commit()
                    self.emit_drafted()
                    self.ui.itemsBox.setEnabled(True)
                    self.ui.uploadFilesBtn.setEnabled(False)
                    self.ui.validateBtn.setEnabled(False)
                except alch_exc.IntegrityError:
                    message_dialog = MessageDialog(
                        'error', 'تاریخ ارسال تکراری است')
                    message_dialog.show()
        except ValidationError as e:
            err = e.errors()[0]
            message_dialog = MessageDialog('error', err['msg'])
            message_dialog.show()

    @Slot()
    def emit_drafted(self):
        self._drafted.emit(True)

    @Slot()
    def emit_created(self):
        self._created.emit(True)

    @Slot()
    def show_example_excel(self):
        if self._post_object is not None:
            try:
                post_dir = 'data/%s' % (self._post_object.title)
                os.mkdir(base_dir / post_dir)
            except FileExistsError:
                pass
            shutil.copyfile(base_dir / 'staticfiles/نمونه اکسل مشخصات.xlsx',
                            base_dir / ('%s/اکسل مشخصات.xlsx' % post_dir))
            os.startfile(base_dir / ('%s/اکسل مشخصات.xlsx' % post_dir))

    @Slot()
    def upload_excel(self):
        if self._post_object is not None:
            try:
                post_dir = 'data/%s' % (self._post_object.title)
                os.mkdir(base_dir / post_dir)
            except FileExistsError:
                pass
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            excel_path = dialog.getOpenFileName(
                self, 'باز کردن فایل', 'C:\\Dekstop', 'Excel file (*.xlsx *.xls)')
            shutil.copyfile(Path(excel_path[0]).resolve(
            ), base_dir / ('%s/اکسل مشخصات.xlsx' % post_dir))
            self._excel_df = pd.read_excel(
                base_dir / ('%s/اکسل مشخصات.xlsx' % post_dir),
                converters={'شماره لایحه': str,
                            'تاریخ لایحه': str,
                            'شماره بایگانی / پرونده': str,
                            'شماره ابلاغیه / دادنامه': str,
                            'تاریخ تنظیم': str,
                            'تاریخ ابلاغ': str})
            self.ui.sanaItemsTable.setRowCount(self._excel_df.shape[0])
            for i, row in self._excel_df.iterrows():
                number = QTableWidgetItem(str(row['شماره لایحه']))
                number.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 0, number)
                date = QTableWidgetItem(str(row['تاریخ لایحه']))
                date.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 1, date)
                type = QTableWidgetItem(row['نوع لایحه'])
                type.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 2, type)
                owner = QTableWidgetItem(row['نام و نام خانوادگی'])
                owner.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 3, owner)
                branch = QTableWidgetItem(row['شعبه'])
                branch.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 4, branch)
                file_number = QTableWidgetItem(
                    str(row['شماره بایگانی / پرونده']))
                file_number.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 5, file_number)
                notice_number = QTableWidgetItem(
                    str(row['شماره ابلاغیه / دادنامه']))
                notice_number.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 6, notice_number)
                set_date = QTableWidgetItem(str(row['تاریخ تنظیم']))
                set_date.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 7, set_date)
                notice_date = QTableWidgetItem(str(row['تاریخ ابلاغ']))
                notice_date.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 8, notice_date)
                sana_audience = QTableWidgetItem(row['مخاطب ثنا'])
                sana_audience.setTextAlignment(Qt.AlignCenter)
                self.ui.sanaItemsTable.setItem(i, 9, sana_audience)
            self.ui.allCountLabel.setText(
                'لایحه:‌ %d مورد' % self._excel_df.shape[0])
            icon = qta.icon('mdi.file')
            text = IconThroughText.render(
                self.ui.allCountLabel.text(), icon, 20)
            self.ui.allCountLabel.setText(text)
            self.ui.uploadFilesBtn.setEnabled(True)

    @Slot()
    def upload_and_merge(self):
        if self._post_object is not None:
            self._excel_df['attachments_count'] = None
            self._excel_df['final_attachment'] = None
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)

            src_filepaths = dialog.getOpenFileNames(
                self, 'باز کردن فایل', 'C:\\Dekstop', 'Pdf Files (*.pdf)')
            dest_filepaths = []
            for src_filepath in src_filepaths[0]:
                dest_filepath = base_dir / 'data' / \
                    self._post_object.title / src_filepath.split('/')[-1]
                shutil.copyfile(Path(src_filepath).resolve(), dest_filepath)
                dest_filepaths.append(dest_filepath)
            self.ui.uploadedCountLabel.setText(
                'آپلود:‌ %d فایل' % len(dest_filepaths))
            icon = qta.icon('mdi.cloud-upload')
            text = IconThroughText.render(
                self.ui.uploadedCountLabel.text(), icon, 20)
            self.ui.uploadedCountLabel.setText(text)

            attachments: List[schemas.CreateAttachment] = list()
            for i, row in self._excel_df.iterrows():
                deleted = []
                for j, dest_filepath in enumerate(dest_filepaths):
                    attachment: schemas.CreateAttachment = None
                    if ('%s %s' % (row['نوع لایحه'], row['نام و نام خانوادگی'])) in str(dest_filepath):
                        attachment = schemas.CreateAttachment(
                            name=dest_filepath.stem, path=str(dest_filepath))
                        attachments.append(attachment)
                        deleted.append(j)
                for d in deleted[::-1]:
                    dest_filepaths.pop(d)

                attachments.sort(key=lambda x: x.name)
                if len(attachments) > 0:
                    with PyPDF2.PdfWriter() as merger:
                        for attachment in attachments:
                            merger.append(attachment.path)
                        merged_filename = Path(attachments[0].name).stem
                        merged_filepath = base_dir / \
                            ('data/%s/%s 0.pdf' %
                             (self._post_object.title, merged_filename))
                        merger.write(merged_filepath)
                    self._excel_df.loc[i, 'attachments_count'] = len(attachments)
                    self._excel_df.loc[i,'final_attachment'] = merged_filepath
                attachments.clear()
            self.ui.validateBtn.setEnabled(True)

    def styleTableWidgetItem(item: QTableWidgetItem, error: str):
        if error is not None:
            item.setToolTip(error)
            item.setBackground(QColor('crimson'))
        else:
            item.setBackground(QColor('green'))

    @Slot()
    def validate(self):
        errors = {}
        all, valid = int(self._excel_df.shape[0]), 0
        sana_items: List[schemas.CreateSanaItem] = list()

        for i, row in self._excel_df.iterrows():
            try:
                sana_item = schemas.CreateSanaItem(
                    number=str(row['شماره لایحه']),
                    date=row['تاریخ لایحه'],
                    type=row['نوع لایحه'],
                    owner=row['نام و نام خانوادگی'],
                    branch=row['شعبه'],
                    file_number=str(row['شماره بایگانی / پرونده']),
                    notice_number=str(row['شماره ابلاغیه / دادنامه']),
                    notice_date=row['تاریخ ابلاغ'],
                    set_date=row['تاریخ تنظیم'],
                    sana_audience=row['مخاطب ثنا'])
                sana_items.append(sana_item)
            except ValidationError as e:
                for err in e.errors():
                    for name in err['loc']:
                        errors[name] = err['msg']

            number = QTableWidgetItem(str(row['شماره لایحه']))
            NewPost.styleTableWidgetItem(number, errors.get('number'))
            number.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 0, number)
            date = QTableWidgetItem(str(row['تاریخ لایحه']))
            NewPost.styleTableWidgetItem(date, errors.get('date'))
            date.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 1, date)
            type = QTableWidgetItem(str(row['نوع لایحه']))
            NewPost.styleTableWidgetItem(type, errors.get('type'))
            type.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 2, type)
            owner = QTableWidgetItem(str(row['نام و نام خانوادگی']))
            NewPost.styleTableWidgetItem(owner, errors.get('owner'))
            owner.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 3, owner)
            branch = QTableWidgetItem(str(row['شعبه']))
            NewPost.styleTableWidgetItem(branch, errors.get('branch'))
            branch.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 4, branch)
            file_number = QTableWidgetItem(str(row['شماره بایگانی / پرونده']))
            NewPost.styleTableWidgetItem(
                file_number, errors.get('file_number'))
            file_number.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 5, file_number)
            notice_number = QTableWidgetItem(
                str(row['شماره ابلاغیه / دادنامه']))
            NewPost.styleTableWidgetItem(
                notice_number, errors.get('notice_number'))
            notice_number.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 6, notice_number)
            set_date = QTableWidgetItem(str(row['تاریخ تنظیم']))
            NewPost.styleTableWidgetItem(set_date, errors.get('set_date'))
            set_date.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 7, set_date)
            notice_date = QTableWidgetItem(str(row['تاریخ ابلاغ']))
            NewPost.styleTableWidgetItem(
                notice_date, errors.get('notice_date'))
            notice_date.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 8, notice_date)
            sana_audience = QTableWidgetItem(str(row['مخاطب ثنا']))
            NewPost.styleTableWidgetItem(
                sana_audience, errors.get('sana_audience'))
            sana_audience.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 9, sana_audience)
            if row.get('attachments_count') is not None:
                attachments_count = QTableWidgetItem(
                    str(row['attachments_count']))
            else:
                attachments_count = QTableWidgetItem('0')
                errors['attachments_count'] = 'فایل پیوست برای لایحه وجود ندارد.'
            NewPost.styleTableWidgetItem(
                attachments_count, errors.get('attachments_count'))
            attachments_count.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 10, attachments_count)
            if row.get('final_attachment') is not None:
                attachment_name = Path(row['final_attachment']).stem
                final_attachment = QTableWidgetItem(attachment_name)
            else:
                final_attachment = QTableWidgetItem('!')
                errors['final_attachment'] = 'فایل پیوست برای لایحه وجود ندارد.'
            NewPost.styleTableWidgetItem(
                final_attachment, errors.get('final_attachment'))
            final_attachment.setTextAlignment(Qt.AlignCenter)
            self.ui.sanaItemsTable.setItem(i, 11, final_attachment)
            if not errors:
                valid += 1
                attachment = models.Attachment(
                    name=Path(row['final_attachment']).stem,
                    path=str(row['final_attachment']),
                    count=row['attachments_count']
                )
                sana_item_object = models.SanaItem(
                    **sana_item.model_dump(exclude=['type', 'attachments', 'sana_audience']),
                    type=models.SanaItemType(sana_item.type),
                    sana_audience=models.SanaAudienceType(
                        sana_item.sana_audience),
                    post=self._post_object,
                    attachments=[attachment]
                )
                self._sana_item_objects.append(sana_item_object)
            errors.clear()
        self.ui.validCountLabel.setText('سالم: %d مورد' % valid)
        icon = qta.icon('mdi.check')
        text = IconThroughText.render(self.ui.validCountLabel.text(), icon, 20)
        self.ui.validCountLabel.setText(text)
        self.ui.invalidCountLabel.setText('خراب: %d مورد' % (all - valid))
        icon = qta.icon('mdi.close-circle')
        text = IconThroughText.render(
            self.ui.invalidCountLabel.text(), icon, 20)
        self.ui.invalidCountLabel.setText(text)

        if all - valid == 0:
            self.ui.createFinalBtn.setEnabled(True)

    @Slot()
    def new_final_post(self):
        failed = False
        with db.get_session() as session:
            error_dialog_list : list[MessageDialog] = list()
            for i, sana_item_object in enumerate(self._sana_item_objects):
                try:
                    if sana_item_object.post in session:
                        session.expunge(sana_item_object.post)
                    session.add(sana_item_object)
                    session.commit()
                except alch_exc.IntegrityError:
                    failed = True
                    error_dialog_list.append(
                        MessageDialog(
                        'error', 'شماره لایحه %d تکراری است' % int(sana_item_object.number))
                    )
                    error_dialog_list[-1].show()
                    session.rollback()
                    continue
        if not failed:
            self.emit_created()
    

class SanaListItemWidget(QWidget):

    def __init__(self, index: int, item: models.SanaItem):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)  # Left, Top, Right, Bottom margins
        layout.setSpacing(10)  # Space between elements

        text_label1 = QLabel(f'{index} {models.SanaItemType(item.type).value} {item.owner}')
        text_label1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Set text alignment to RTL
        layout.addWidget(text_label1)

        arrow_icon = qta.icon('mdi.arrow-left-thick')
        arrow_icon_label1 = QLabel()
        arrow_icon_label1.setPixmap(arrow_icon.pixmap(20, 20))
        arrow_icon_label1.setFixedSize(20, 20)
        layout.addWidget(arrow_icon_label1)


        text_label2 = QLabel(models.SanaAudienceType(item.sana_audience).value)
        text_label2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(text_label2)

        arrow_icon_label2 = QLabel()
        arrow_icon_label2.setPixmap(arrow_icon.pixmap(20, 20))
        arrow_icon_label2.setFixedSize(20, 20)
        layout.addWidget(arrow_icon_label2)


        text_label3 = QLabel(models.SanaItemSendingStatus(item.sending_status).value)
        text_label3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(text_label3)

        if item.sending_status == models.SanaItemSendingStatus.Send_Queue:
            hand_icon = qta.icon('mdi.hand-left')
            hand_icon_label = QLabel()
            hand_icon_label.setPixmap(hand_icon.pixmap(20, 20))
            hand_icon_label.setFixedSize(20, 20)
            layout.addWidget(hand_icon_label)
        elif item.sending_status == models.SanaItemSendingStatus.Sending:
            loading_icon_widget = qta.IconWidget()
            loading_icon = qta.icon('fa.spinner', animation=qta.Pulse(loading_icon_widget, autostart=True))
            loading_icon_widget.setIcon(loading_icon)
            loading_icon_widget.setFixedSize(20, 20)
            layout.addWidget(loading_icon_widget)
        elif item.sending_status == models.SanaItemSendingStatus.Sent:
            if item.success:
                text_label4 = QLabel(item.tracking_code)
                text_label4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                layout.addWidget(text_label4)
                ok_icon = qta.icon('mdi.check')
                ok_icon_label = QLabel()
                ok_icon_label.setPixmap(ok_icon.pixmap(20, 20))
                ok_icon_label.setFixedSize(20, 20)
                layout.addWidget(ok_icon_label)
            else:
                error_icon = qta.icon('mdi.close-circle')
                error_icon_label = QLabel()
                error_icon_label.setPixmap(error_icon.pixmap(20, 20))
                error_icon_label.setFixedSize(20, 20)
                layout.addWidget(error_icon_label)


        layout.addStretch()

        self.setLayout(layout)


class SendPost(QWidget):
    
    seconds : int = 0

    def __init__(self, post: models.Post):
        super(SendPost, self).__init__()
        self.setFixedSize(600, 500)
        self.setWindowIcon(QIcon(str(base_dir / 'staticfiles/adliran.ico')))
        self.ui = Ui_sendPost()
        self.ui.setupUi(self)
        self.ui.sendPostBox.setTitle(post.title)
        self.ui.postSanaItemsList.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        self.ui.postSanaItemsList.setLayoutDirection(Qt.RightToLeft)
        self.ui.startButton.setIcon(qta.icon('fa.play'))
        self.ui.startButton.setIconSize(QSize(16, 16))
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.setIcon(qta.icon('fa.stop'))
        self.ui.stopButton.setIconSize(QSize(16, 16))
        self.ui.stopButton.clicked.connect(self.stop)
        # stopwatch
        h = SendPost.seconds // 3600
        m = (SendPost.seconds % 3600) // 60
        s = SendPost.seconds % 60
        self.ui.stopwatchLabel.setText(f'زمان: {h:02}:{m:02}:{s:02}')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stopwatch)
        self._post = post
        self.render_items_list()

    @Slot()
    def update_stopwatch(self):
        SendPost.seconds += 1
        h = SendPost.seconds // 3600
        m = (SendPost.seconds % 3600) // 60
        s = SendPost.seconds % 60
        self.ui.stopwatchLabel.setText(f'زمان: {h:02}:{m:02}:{s:02}')

    @Slot()    
    def start(self):
        if self._post.items is not None:
            if not self.timer.isActive():
                self.timer.start(1000)
            loop = QEventLoop()
            self._sana_worker = SanaSeleniumWorker(sana_items_list=self._post.items)
            self._sana_worker.sana_item_change.connect(self.change_item_status)
            self._sana_worker.finished.connect(loop.quit)
            self._sana_worker.start()
            loop.exec_()
    @Slot()
    def stop(self):
        self.timer.stop()

    def change_item_status(self, item: models.SanaItem):
        with db.get_session() as session:
            item = session.merge(item)
            session.commit()
        self.render_items_list()

    def render_items_list(self):
        with db.get_session() as session:
            self._post = session.get(models.Post, self._post.date)
            self._post.items.sort(
                    key=lambda item: (
                        0 if item.sana_audience == models.SanaAudienceType.Saba else 
                        1 if item.sana_audience == models.SanaAudienceType.Sata else 
                        2)
                )
            self.ui.postSanaItemsList.clear()
            for i, item in enumerate(self._post.items, start=1):
                item_widget = SanaListItemWidget(index=i, item=item)
                list_item = QListWidgetItem(self.ui.postSanaItemsList)
                list_item.setSizeHint(item_widget.sizeHint())  # Set item size to match the widget's size
                list_item.setTextAlignment(Qt.AlignRight)
                self.ui.postSanaItemsList.addItem(list_item)
                self.ui.postSanaItemsList.setItemWidget(list_item, item_widget)
            self.ui.postSanaItemsList.show()


class App(QApplication):

    def __init__(self, *argv):
        super(App, self).__init__(*argv)

    def exec(self):
        main_window = MainWindow()
        main_window.show()
        super(App, self).exec()


class SanaSeleniumWorker(QThread):

    sana_item_change = Signal(object)
    SABA_PEROSN = schemas.SanaHoghooghiPerson(
                            national_code=os.getenv('SABA_PERSON_NATIONAL_CODE'),
                            user_password=os.getenv('SABA_PERSON_USER_PASSWORD'),
                            legal_identity=os.getenv('SABA_PERSON_LEGAL_IDENTITY'),
                            otp_password=os.getenv('SABA_PERSON_OTP_PASSWORD'))

    SATA_PERSON = schemas.SanaHoghooghiPerson(
                    national_code=os.getenv('SATA_PERSON_NATIONAL_CODE'),
                    user_password=os.getenv('SATA_PERSON_USER_PASSWORD'),
                    legal_identity=os.getenv('SATA_PERSON_LEGAL_IDENTITY'),
                    otp_password=os.getenv('SATA_PERSON_OTP_PASSWORD'))

    def __init__(self, sana_items_list: List[models.SanaItem], parent=None):
        super().__init__(parent)
        self._driver = driver.SanaHoghooghiDriver()
        self._sana_items_list = sana_items_list

    def run(self):
        for i, sana_item in enumerate(self._sana_items_list, start=1):
            if isinstance(sana_item, models.SanaItem):
                sana_item.sending_status =  models.SanaItemSendingStatus.Sending
                self.sana_item_change.emit(sana_item)
                if sana_item.sana_audience == models.SanaAudienceType.Saba:
                    if self._driver.get_sana_perosn() != self.SABA_PEROSN:
                            self._driver.set_sana_person(person=self.SABA_PEROSN)
                    self._driver.send_sana_item(i, sana_item)
                if sana_item.sana_audience == models.SanaAudienceType.Sata:
                    if self._driver.get_sana_perosn() != self.SATA_PERSON:
                            self._driver.set_sana_person(person=self.SATA_PERSON)
                    self._driver.send_sana_item(i, sana_item)
                if sana_item.sending_status == models.SanaItemSendingStatus.Sent:
                    self.sana_item_change.emit(sana_item)