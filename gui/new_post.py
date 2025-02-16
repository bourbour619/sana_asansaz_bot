# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewPost.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_newPost(object):
    def setupUi(self, newPost):
        if not newPost.objectName():
            newPost.setObjectName(u"newPost")
        newPost.resize(1126, 627)
        font = QFont()
        font.setFamilies([u"B Yekan"])
        font.setPointSize(12)
        newPost.setFont(font)
        newPost.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.newPostBox = QGroupBox(newPost)
        self.newPostBox.setObjectName(u"newPostBox")
        self.newPostBox.setGeometry(QRect(10, 10, 1101, 611))
        self.createFinalBtn = QPushButton(self.newPostBox)
        self.createFinalBtn.setObjectName(u"createFinalBtn")
        self.createFinalBtn.setEnabled(False)
        self.createFinalBtn.setGeometry(QRect(30, 560, 81, 31))
        self.titleLabel = QLabel(self.newPostBox)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(280, 60, 49, 16))
        self.itemsBox = QGroupBox(self.newPostBox)
        self.itemsBox.setObjectName(u"itemsBox")
        self.itemsBox.setEnabled(False)
        self.itemsBox.setGeometry(QRect(30, 110, 1061, 441))
        self.uploadExcelBtn = QPushButton(self.itemsBox)
        self.uploadExcelBtn.setObjectName(u"uploadExcelBtn")
        self.uploadExcelBtn.setGeometry(QRect(840, 130, 211, 31))
        self.uploadExcelBtn.setFont(font)
        self.uploadExcelBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sanaItemsTable = QTableWidget(self.itemsBox)
        if (self.sanaItemsTable.columnCount() < 12):
            self.sanaItemsTable.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.sanaItemsTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.sanaItemsTable.setObjectName(u"sanaItemsTable")
        self.sanaItemsTable.setGeometry(QRect(10, 180, 1041, 251))
        font1 = QFont()
        font1.setFamilies([u"B Yekan"])
        font1.setPointSize(11)
        self.sanaItemsTable.setFont(font1)
        self.uploadFilesBtn = QPushButton(self.itemsBox)
        self.uploadFilesBtn.setObjectName(u"uploadFilesBtn")
        self.uploadFilesBtn.setGeometry(QRect(530, 130, 291, 31))
        self.guideLabel1 = QLabel(self.itemsBox)
        self.guideLabel1.setObjectName(u"guideLabel1")
        self.guideLabel1.setGeometry(QRect(450, 20, 571, 41))
        self.guideLabel1.setFont(font1)
        self.validateBtn = QPushButton(self.itemsBox)
        self.validateBtn.setObjectName(u"validateBtn")
        self.validateBtn.setGeometry(QRect(400, 130, 121, 31))
        self.validateBtn.setFont(font)
        self.validateBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.validateBtn.setStyleSheet(u"")
        self.guideLabel2 = QLabel(self.itemsBox)
        self.guideLabel2.setObjectName(u"guideLabel2")
        self.guideLabel2.setGeometry(QRect(470, 20, 201, 41))
        self.guideLabel2.setFont(font1)
        self.guideLabel3 = QLabel(self.itemsBox)
        self.guideLabel3.setObjectName(u"guideLabel3")
        self.guideLabel3.setGeometry(QRect(650, 50, 371, 41))
        self.guideLabel3.setFont(font1)
        self.guideLabel4 = QLabel(self.itemsBox)
        self.guideLabel4.setObjectName(u"guideLabel4")
        self.guideLabel4.setGeometry(QRect(640, 80, 381, 41))
        self.guideLabel4.setFont(font1)
        self.showExampleExcelBtn = QPushButton(self.itemsBox)
        self.showExampleExcelBtn.setObjectName(u"showExampleExcelBtn")
        self.showExampleExcelBtn.setGeometry(QRect(684, 30, 101, 24))
        self.createDraftBtn = QPushButton(self.newPostBox)
        self.createDraftBtn.setObjectName(u"createDraftBtn")
        self.createDraftBtn.setGeometry(QRect(710, 50, 141, 31))
        self.createDraftBtn.setAutoDefault(False)
        self.titleInput = QLineEdit(self.newPostBox)
        self.titleInput.setObjectName(u"titleInput")
        self.titleInput.setGeometry(QRect(50, 50, 221, 31))
        self.titleInput.setReadOnly(True)
        self.dateInput = QLineEdit(self.newPostBox)
        self.dateInput.setObjectName(u"dateInput")
        self.dateInput.setGeometry(QRect(890, 50, 121, 31))
        self.dateInput.setReadOnly(False)
        self.dateLabel = QLabel(self.newPostBox)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(1010, 60, 49, 16))
        self.allCountLabel = QLabel(self.newPostBox)
        self.allCountLabel.setObjectName(u"allCountLabel")
        self.allCountLabel.setGeometry(QRect(950, 570, 111, 31))
        self.allCountLabel.setFont(font1)
        self.allCountLabel.setStyleSheet(u"")
        self.uploadedCountLabel = QLabel(self.newPostBox)
        self.uploadedCountLabel.setObjectName(u"uploadedCountLabel")
        self.uploadedCountLabel.setGeometry(QRect(560, 570, 121, 31))
        self.uploadedCountLabel.setFont(font1)
        self.uploadedCountLabel.setStyleSheet(u"")
        self.validCountLabel = QLabel(self.newPostBox)
        self.validCountLabel.setObjectName(u"validCountLabel")
        self.validCountLabel.setGeometry(QRect(830, 570, 111, 31))
        self.validCountLabel.setFont(font1)
        self.validCountLabel.setStyleSheet(u"")
        self.invalidCountLabel = QLabel(self.newPostBox)
        self.invalidCountLabel.setObjectName(u"invalidCountLabel")
        self.invalidCountLabel.setGeometry(QRect(700, 570, 111, 31))
        self.invalidCountLabel.setFont(font1)
        self.invalidCountLabel.setStyleSheet(u"")

        self.retranslateUi(newPost)

        self.createDraftBtn.setDefault(False)


        QMetaObject.connectSlotsByName(newPost)
    # setupUi

    def retranslateUi(self, newPost):
        newPost.setWindowTitle(QCoreApplication.translate("newPost", u"\u0627\u0631\u0633\u0627\u0644 \u062c\u062f\u06cc\u062f", None))
        self.newPostBox.setTitle(QCoreApplication.translate("newPost", u"\u0627\u0631\u0633\u0627\u0644 \u062c\u062f\u06cc\u062f", None))
        self.createFinalBtn.setText(QCoreApplication.translate("newPost", u"\u062b\u0628\u062a \u0646\u0647\u0627\u06cc\u06cc", None))
        self.titleLabel.setText(QCoreApplication.translate("newPost", u"\u0639\u0646\u0648\u0627\u0646:", None))
        self.itemsBox.setTitle(QCoreApplication.translate("newPost", u"\u0644\u0627\u06cc\u062d\u0647 \u0647\u0627 ", None))
        self.uploadExcelBtn.setText(QCoreApplication.translate("newPost", u"\u0628\u0627\u0631\u06af\u0632\u0627\u0631\u06cc \u0627\u06a9\u0633\u0644 \u0645\u0634\u062e\u0635\u0627\u062a (1)", None))
        ___qtablewidgetitem = self.sanaItemsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("newPost", u"\u0634\u0645\u0627\u0631\u0647 \u0644\u0627\u06cc\u062d\u0647", None));
        ___qtablewidgetitem1 = self.sanaItemsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("newPost", u"\u062a\u0627\u0631\u06cc\u062e \u0644\u0627\u06cc\u062d\u0647", None));
        ___qtablewidgetitem2 = self.sanaItemsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("newPost", u"\u0646\u0648\u0639 \u0644\u0627\u06cc\u062d\u0647", None));
        ___qtablewidgetitem3 = self.sanaItemsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("newPost", u"\u0646\u0627\u0645 \u0648 \u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None));
        ___qtablewidgetitem4 = self.sanaItemsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("newPost", u"\u0634\u0639\u0628\u0647", None));
        ___qtablewidgetitem5 = self.sanaItemsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("newPost", u"\u0634\u0645\u0627\u0631\u0647 \u0628\u0627\u06cc\u06af\u0627\u0646\u06cc / \u067e\u0631\u0648\u0646\u062f\u0647", None));
        ___qtablewidgetitem6 = self.sanaItemsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("newPost", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u0628\u0644\u0627\u063a\u06cc\u0647 / \u062f\u0627\u062f\u0646\u0627\u0645\u0647", None));
        ___qtablewidgetitem7 = self.sanaItemsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("newPost", u"\u062a\u0627\u0631\u06cc\u062e \u062a\u0646\u0638\u06cc\u0645", None));
        ___qtablewidgetitem8 = self.sanaItemsTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("newPost", u"\u062a\u0627\u0631\u06cc\u062e \u0627\u0628\u0644\u0627\u063a", None));
        ___qtablewidgetitem9 = self.sanaItemsTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("newPost", u"\u0645\u062e\u0627\u0637\u0628 \u062b\u0646\u0627", None));
        ___qtablewidgetitem10 = self.sanaItemsTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("newPost", u" \u062a\u0639\u062f\u0627\u062f \u0641\u0627\u06cc\u0644 \u067e\u06cc\u0648\u0633\u062a", None));
        ___qtablewidgetitem11 = self.sanaItemsTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("newPost", u"\u0641\u0627\u06cc\u0644 \u067e\u06cc\u0648\u0633\u062a \u0646\u0647\u0627\u06cc\u06cc", None));
        self.uploadFilesBtn.setText(QCoreApplication.translate("newPost", u"\u0628\u0627\u0631\u06af\u0632\u0627\u0631\u06cc \u0648 \u0627\u062f\u063a\u0627\u0645 \u067e\u06cc\u0648\u0633\u062a \u0647\u0627\u06cc \u0644\u0627\u06cc\u062d\u0647 (\u06f2)", None))
        self.guideLabel1.setText(QCoreApplication.translate("newPost", u"\u06f1- \u0627\u0628\u062a\u062f\u0627 \u0627\u06a9\u0633\u0644 \u0645\u0634\u062e\u0635\u0627\u062a \u0631\u0627 \u0645\u0637\u0627\u0628\u0642 \u0646\u0645\u0648\u0646\u0647 (", None))
        self.validateBtn.setText(QCoreApplication.translate("newPost", u"\u0627\u0639\u062a\u0628\u0627\u0631 \u0633\u0646\u062c\u06cc (\u06f3)", None))
        self.guideLabel2.setText(QCoreApplication.translate("newPost", u") \u062a\u06a9\u0645\u06cc\u0644 \u0648 \u0628\u0627\u0631\u06af\u0632\u0627\u0631\u06cc \u06a9\u0646\u06cc\u062f.", None))
        self.guideLabel3.setText(QCoreApplication.translate("newPost", u"\u06f2- \u0633\u067e\u0633 \u0641\u0627\u06cc\u0644 \u0647\u0627\u06cc \u067e\u06cc\u0648\u0633\u062a \u0644\u0627\u06cc\u062d\u0647 \u0631\u0627 \u0628\u0627\u0631\u06af\u0632\u0627\u0631\u06cc \u0646\u0645\u0627\u06cc\u06cc\u062f \u062a\u0627 \u0627\u062f\u063a\u0627\u0645 \u0634\u0648\u0646\u062f.", None))
        self.guideLabel4.setText(QCoreApplication.translate("newPost", u"\u06f3- \u0627\u0639\u062a\u0628\u0627\u0631 \u0633\u0646\u062c\u06cc \u06a9\u0631\u062f\u0647 \u062a\u0627 \u0644\u06cc\u0633\u062a \u0644\u0627\u06cc\u062d\u0647 \u0647\u0627 \u0628\u0647 \u0647\u0645\u0631\u0627\u0647 \u067e\u06cc\u0648\u0633\u062a \u0627\u06cc\u062c\u0627\u062f \u0634\u0648\u062f.", None))
        self.showExampleExcelBtn.setText(QCoreApplication.translate("newPost", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0646\u0645\u0648\u0646\u0647", None))
        self.createDraftBtn.setText(QCoreApplication.translate("newPost", u"\u062b\u0628\u062a \u067e\u06cc\u0634 \u0646\u0648\u06cc\u0633 ", None))
        self.dateLabel.setText(QCoreApplication.translate("newPost", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.allCountLabel.setText(QCoreApplication.translate("newPost", u"\u0644\u0627\u06cc\u062d\u0647 : \u06f0 \u0645\u0648\u0631\u062f", None))
        self.uploadedCountLabel.setText(QCoreApplication.translate("newPost", u"\u0622\u067e\u0644\u0648\u062f\u200c:\u200c \u06f0 \u0641\u0627\u06cc\u0644", None))
        self.validCountLabel.setText(QCoreApplication.translate("newPost", u"\u0633\u0627\u0644\u0645 :\u200c \u06f0 \u0645\u0648\u0631\u062f", None))
        self.invalidCountLabel.setText(QCoreApplication.translate("newPost", u"\u062e\u0631\u0627\u0628: \u06f0 \u0645\u0648\u0631\u062f", None))
    # retranslateUi

