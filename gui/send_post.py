# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SendPost.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QListView, QSizePolicy,
    QWidget)

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
        self.sendPostBox.setGeometry(QRect(10, 10, 571, 471))
        self.postSanaItemsList = QListView(self.sendPostBox)
        self.postSanaItemsList.setObjectName(u"postSanaItemsList")
        self.postSanaItemsList.setGeometry(QRect(15, 40, 541, 401))

        self.retranslateUi(sendPost)

        QMetaObject.connectSlotsByName(sendPost)
    # setupUi

    def retranslateUi(self, sendPost):
        sendPost.setWindowTitle(QCoreApplication.translate("sendPost", u"\u0627\u0646\u062c\u0627\u0645 \u0627\u0631\u0633\u0627\u0644", None))
        self.sendPostBox.setTitle(QCoreApplication.translate("sendPost", u"GroupBox", None))
    # retranslateUi

