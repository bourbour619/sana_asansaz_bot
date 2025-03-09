# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SendPost.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_sendPost(object):
    def setupUi(self, sendPost):
        if not sendPost.objectName():
            sendPost.setObjectName(u"sendPost")
        sendPost.resize(600, 500)
        font = QFont()
        font.setFamilies([u"B Yekan"])
        font.setPointSize(12)
        sendPost.setFont(font)
        sendPost.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sendPostBox = QGroupBox(sendPost)
        self.sendPostBox.setObjectName(u"sendPostBox")
        self.sendPostBox.setGeometry(QRect(10, 70, 571, 411))
        self.postSanaItemsList = QListWidget(self.sendPostBox)
        self.postSanaItemsList.setObjectName(u"postSanaItemsList")
        self.postSanaItemsList.setGeometry(QRect(10, 30, 551, 371))
        self.startButton = QPushButton(sendPost)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(500, 20, 81, 31))
        self.stopButton = QPushButton(sendPost)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(410, 20, 81, 31))
        self.stopwatchLabel = QLabel(sendPost)
        self.stopwatchLabel.setObjectName(u"stopwatchLabel")
        self.stopwatchLabel.setGeometry(QRect(20, 20, 121, 31))

        self.retranslateUi(sendPost)

        QMetaObject.connectSlotsByName(sendPost)
    # setupUi

    def retranslateUi(self, sendPost):
        sendPost.setWindowTitle(QCoreApplication.translate("sendPost", u"\u0627\u0646\u062c\u0627\u0645 \u0627\u0631\u0633\u0627\u0644", None))
        self.sendPostBox.setTitle(QCoreApplication.translate("sendPost", u"GroupBox", None))
        self.startButton.setText(QCoreApplication.translate("sendPost", u"\u0634\u0631\u0648\u0639   ", None))
        self.stopButton.setText(QCoreApplication.translate("sendPost", u"\u062a\u0648\u0642\u0641   ", None))
        self.stopwatchLabel.setText(QCoreApplication.translate("sendPost", u"\u0632\u0645\u0627\u0646: \u06f0\u06f0:\u06f0\u06f0:\u06f0\u06f0", None))
    # retranslateUi

