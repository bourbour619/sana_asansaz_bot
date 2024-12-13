# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MessageDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_messageDialog(object):
    def setupUi(self, messageDialog):
        if not messageDialog.objectName():
            messageDialog.setObjectName(u"messageDialog")
        messageDialog.resize(400, 159)
        font = QFont()
        font.setFamilies([u"B Yekan"])
        font.setPointSize(12)
        messageDialog.setFont(font)
        messageDialog.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.messageText = QLabel(messageDialog)
        self.messageText.setObjectName(u"messageText")
        self.messageText.setGeometry(QRect(30, 30, 341, 81))
        self.messageText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(messageDialog)

        QMetaObject.connectSlotsByName(messageDialog)
    # setupUi

    def retranslateUi(self, messageDialog):
        messageDialog.setWindowTitle(QCoreApplication.translate("messageDialog", u"Form", None))
        self.messageText.setText("")
    # retranslateUi

