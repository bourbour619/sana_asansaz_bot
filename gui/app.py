# This Python file uses the following encoding: utf-8
import shutil
import os
import PyPDF2
import pandas as pd
from pathlib import Path

from typing import List
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget,
                            QTableWidgetItem,QHeaderView, QFileDialog)
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Slot, Signal

from core import schema, model, database


from .main_window import Ui_mainWindow
from .new_post import Ui_newPost
from .message_dialog import Ui_messageDialog


base_dir = Path(__file__).resolve().parent.parent

db_instance = database.DB()


class MessageDialog(QWidget):
    def __init__(self, type, message):
        super(MessageDialog, self).__init__()
        self.ui = Ui_messageDialog()
        self.ui.setupUi(self)
        self.setFixedSize(400, 159)
        if type == 'error':
            self.setWindowTitle('خطا ❌')
        elif type == 'success':
            self.setWindowTitle('موفقیت ✅')
        elif type == 'warn':
            self.setWindowTitle('هشدار ⚠️')
        self.ui.messageText.setText(message)


class MainWindow(QWidget):

    _posts: List[model.Post] = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1126,627)
        self.setWindowIcon(QIcon(str(base_dir / 'staticfiles/adliran.ico')))
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.postsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.postsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        for i in range(1, self.ui.postsTable.columnCount()):
            self.ui.postsTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        self.ui.newPostBtn.clicked.connect(self.new_post)
        self.fetch_all_posts()


    def fetch_all_posts(self):
        with db_instance.get_session() as session:
            self._posts = session.scalars(select(model.Post)).all()
            self.ui.postsTable.setRowCount(len(self._posts))
            for i,post in enumerate(self._posts[::-1]):
                title = QTableWidgetItem(post.title)
                self.ui.postsTable.setItem(i, 0, title)
                date = QTableWidgetItem(post.date)
                self.ui.postsTable.setItem(i, 1, date)
                status = QTableWidgetItem(post.status.value)
                self.ui.postsTable.setItem(i, 3, status)
                items_count = QTableWidgetItem(str(post.items_count))
                self.ui.postsTable.setItem(i, 2, items_count)

    @Slot()
    def new_post(self):
        self.post = NewPost()
        self.post.setFixedSize(1126, 627)
        self.post.setGeometry(640, 280, self.post.width(), self.post.height())
        self.post.show()
        self.post._created.connect(self.post_created)
        self.post._drafted.connect(self.post_drafted)


    @Slot()
    def post_created(self):
        self.post.close()
        self.fetch_all_posts()

    @Slot()
    def post_drafted(self):
        self.fetch_all_posts()

class NewPost(QWidget):

    _drafted = Signal((bool),)
    _created = Signal((bool),)
    _post_object: model.Post = None
    _sana_item_objects: List[model.SanaItem] = list()

    def __init__(self):
        super(NewPost, self).__init__()
        self.setFixedSize(1126,627)
        self.setWindowIcon(QIcon(str(base_dir / 'staticfiles/adliran.ico')))
        self.ui = Ui_newPost()
        self.ui.setupUi(self)
        self.ui.sanaItemsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.sanaItemsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.createDraftBtn.clicked.connect(self.new_draft_post)
        self.ui.createFinalBtn.clicked.connect(self.emit_created)
        self.ui.showExampleExcelBtn.clicked.connect(self.show_example_excel)
        self.ui.uploadExcelBtn.clicked.connect(self.upload_excel)
        self.ui.uploadFilesBtn.clicked.connect(self.upload_and_merge)


    @Slot()
    def new_draft_post(self):
        date_input = self.ui.dateInput.text()
        try:
            post = schema.CreatePost(date=date_input, status=schema.PostStatus.Draft)
            self.ui.titleInput.setText(post.title)
            self._post_object = model.Post(title=post.title,
                        date=post.date,
                        status=model.PostStatus(post.status.value),
                        items=[])
            with db_instance.get_session() as session:
                try:
                    session.add(self._post_object)
                    session.commit()
                    self.emit_drafted()
                    self.ui.commitBtn.setEnabled(True)
                    self.ui.itemsBox.setEnabled(True)
                    self.ui.uploadFilesBtn.setEnabled(False)
                    self.ui.commitBtn.setEnabled(False)
                except IntegrityError:
                    message_dialog = MessageDialog('error', 'تاریخ لایحه تکراری است')
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
                post_dir = 'data/%s' %(self._post_object.title)
                os.mkdir(base_dir / post_dir)
            except FileExistsError:
                pass
            shutil.copyfile(base_dir / 'staticfiles/نمونه اکسل مشخصات.xlsx', base_dir / ('%s/اکسل مشخصات.xlsx' %post_dir))
            os.startfile(base_dir / ('%s/اکسل مشخصات.xlsx' %post_dir))

    @Slot()
    def upload_excel(self):
        if self._post_object is not None:
            try:
                post_dir = 'data/%s' %(self._post_object.title)
                os.mkdir(base_dir / post_dir)
            except FileExistsError:
                pass
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            excel_path = dialog.getOpenFileName(self, 'باز کردن فایل','C:\\Dekstop', 'Excel file (*.xlsx *.xls)')
            shutil.copyfile(Path(excel_path[0]).resolve(), base_dir / ('%s/اکسل مشخصات.xlsx' %post_dir))
            excel_df = pd.read_excel(base_dir / ('%s/اکسل مشخصات.xlsx' %post_dir))
            self.ui.sanaItemsTable.setRowCount(excel_df.shape[0])
            errors = {}
            def wrapTableWidgetItemError(item: QTableWidgetItem, name: str):
                try:
                    if errors[name] is not None:
                        item.setToolTip(errors[name])
                        item.setBackground(QColor('crimson'))
                except KeyError:
                    pass

            items: List[schema.CreateSanaItem] = list()
            for i, row in excel_df.iterrows():
                try:
                    sana_item = schema.CreateSanaItem(
                                    number=str(row['شماره لایحه']),
                                    date=row['تاریخ لایحه'],
                                    type=row['نوع لایحه'],
                                    owner=row['نام و نام خانوادگی'],
                                    branch=row['شعبه'],
                                    file_number=str(row['شماره بایگانی / پرونده']),
                                    notice_number=str(row['شماره ابلاغیه / دادنامه']),
                                    notice_date=row['تاریخ ابلاغ'],
                                    set_date=row['تاریخ تنظیم'])
                    items.append(sana_item)
                except ValidationError as e:
                    for err in e.errors():
                        for name in err['loc']:
                            errors[name] = err['msg']

                number = QTableWidgetItem(str(row['شماره لایحه']))
                wrapTableWidgetItemError(number, 'number')
                self.ui.sanaItemsTable.setItem(i, 0, number)
                date = QTableWidgetItem(row['تاریخ لایحه'])
                wrapTableWidgetItemError(date, 'date')
                self.ui.sanaItemsTable.setItem(i, 1, date)
                type = QTableWidgetItem(row['نوع لایحه'])
                wrapTableWidgetItemError(type, 'type')
                self.ui.sanaItemsTable.setItem(i, 2, type)
                owner = QTableWidgetItem(row['نام و نام خانوادگی'])
                wrapTableWidgetItemError(owner, 'owner')
                self.ui.sanaItemsTable.setItem(i, 3, owner)
                branch = QTableWidgetItem(row['شعبه'])
                wrapTableWidgetItemError(branch, 'branch')
                self.ui.sanaItemsTable.setItem(i, 4, branch)
                file_number = QTableWidgetItem(str(row['شماره بایگانی / پرونده']))
                wrapTableWidgetItemError(file_number, 'file_number')
                self.ui.sanaItemsTable.setItem(i, 5, file_number)
                notice_number = QTableWidgetItem(str(row['شماره ابلاغیه / دادنامه']))
                wrapTableWidgetItemError(notice_number, 'notice_number')
                self.ui.sanaItemsTable.setItem(i, 6, notice_number)
                set_date = QTableWidgetItem(row['تاریخ تنظیم'])
                wrapTableWidgetItemError(set_date, 'set_date')
                self.ui.sanaItemsTable.setItem(i, 7, set_date)
                notice_date = QTableWidgetItem(row['تاریخ ابلاغ'])
                wrapTableWidgetItemError(notice_date, 'notice_date')
                self.ui.sanaItemsTable.setItem(i, 8, notice_date)
                errors.clear()

            with db_instance.get_session() as session:
                for sana_item in items:
                    self._sana_item_objects.append(
                        model.SanaItem(**sana_item.model_dump(exclude=['type', 'attachments']),
                                        type= model.SanaItemType(sana_item.type),
                                        post=self._post_object,
                                        attachments=[]
                                    )
                        )
                session.add_all(self._sana_item_objects)
                session.commit()
            self.ui.uploadFilesBtn.setEnabled(True)
            self.emit_drafted()


    @Slot()
    def upload_and_merge(self):
        if self._post_object is not None:
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)

            src_file_paths = dialog.getOpenFileNames(self, 'باز کردن فایل','C:\\Dekstop', 'Pdf Files (*.pdf)')
            dest_file_paths = []
            for src_file_path in src_file_paths[0]:
                dest_file_path = base_dir / 'data' / self._post_object.title / src_file_path.split('/')[-1]
                shutil.copyfile(Path(src_file_path).resolve(), dest_file_path)
                dest_file_paths.append(dest_file_path)

            for item in self._sana_item_objects:
                attachments: List[schema.CreateAttachment] = []
                deleted = []
                for i, dest_file_path in enumerate(dest_file_paths):
                    attachment: schema.CreateAttachment = None
                    if ('%s %s'%(item.type.value, item.owner)) in str(dest_file_path):
                        attachment = schema.CreateAttachment(title=dest_file_path.stem, stored_at= str(dest_file_path))
                        attachments.append(attachment)
                        item.attachments.append(
                                model.Attachment(**attachment.model_dump())
                        )
                        deleted.append(i)
                for d in deleted[::-1]:
                    dest_file_paths.pop(d)
                attachments.sort(key=lambda x: x.title)

                if len(attachments) > 0:
                    with PyPDF2.PdfWriter() as merger:
                        for attachment in attachments:
                            merger.append(attachment.stored_at)
                        merged_filename = Path(attachments[0].title).stem
                        merged_file_path = base_dir / ('data/%s/%s 0.pdf' %(self._post_object.title, merged_filename))
                        merger.write(merged_file_path)
                        attachment = schema.CreateAttachment(title=merged_filename, stored_at=str(merged_file_path), merged=True)
                        item.attachments.append(
                                model.Attachment(**attachment.model_dump())
                        )

            with db_instance.get_session() as session:
                session.add_all(self._sana_item_objects)
                session.commit()

            for i, item in enumerate(self._sana_item_objects):
                if item.attachments_count > 0:
                    attachment_count = QTableWidgetItem(str(item.attachments_count))
                    self.ui.sanaItemsTable.setItem(i, 9, attachment_count)
                    final_attachment = QTableWidgetItem(item.attachments[-1].title)
                    self.ui.sanaItemsTable.setItem(i, 10, final_attachment)

            self.ui.commitBtn.setEnabled(True)
            self.emit_drafted()



class App(QApplication):

    def __init__(self, *argv):
        super(App, self).__init__(*argv)

    def exec(self):
        main_window = MainWindow()
        main_window.show()
        super(App, self).exec()

