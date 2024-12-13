# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1126, 627)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"B Yekan"])
        font.setPointSize(12)
        mainWindow.setFont(font)
        mainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        mainWindow.setAutoFillBackground(False)
        self.tabWidget = QTabWidget(mainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(16, 10, 1101, 611))
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.sendToDivanTab = QWidget()
        self.sendToDivanTab.setObjectName(u"sendToDivanTab")
        self.sendToDivanTab.setFont(font)
        self.newPostBtn = QPushButton(self.sendToDivanTab)
        self.newPostBtn.setObjectName(u"newPostBtn")
        self.newPostBtn.setGeometry(QRect(970, 30, 111, 31))
        self.newPostBtn.setFont(font)
        self.newPostBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newPostBtn.setAutoFillBackground(False)
        self.newPostBtn.setCheckable(False)
        self.newPostBtn.setFlat(False)
        self.postsBox = QGroupBox(self.sendToDivanTab)
        self.postsBox.setObjectName(u"postsBox")
        self.postsBox.setGeometry(QRect(29, 90, 1051, 461))
        self.postsBox.setFont(font)
        self.postsTable = QTableWidget(self.postsBox)
        if (self.postsTable.columnCount() < 9):
            self.postsTable.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.postsTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.postsTable.setObjectName(u"postsTable")
        self.postsTable.setGeometry(QRect(20, 50, 1021, 391))
        self.postsTable.setFont(font)
        self.searchBtn = QPushButton(self.sendToDivanTab)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(30, 30, 111, 31))
        self.searchBtn.setFont(font)
        self.searchBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchBtn.setAutoFillBackground(False)
        self.searchBtn.setCheckable(False)
        self.searchBtn.setFlat(False)
        self.searchInput = QLineEdit(self.sendToDivanTab)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setGeometry(QRect(150, 30, 251, 31))
        self.searchLabel = QLabel(self.sendToDivanTab)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setGeometry(QRect(410, 40, 101, 20))
        self.tabWidget.addTab(self.sendToDivanTab, "")
        self.fetchEblagh = QWidget()
        self.fetchEblagh.setObjectName(u"fetchEblagh")
        self.tabWidget.addTab(self.fetchEblagh, "")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0631\u0628\u0627\u062a \u0622\u0633\u0627\u0646 \u0633\u0627\u0632 \u062b\u0646\u0627", None))
        self.newPostBtn.setText(QCoreApplication.translate("mainWindow", u"\u0627\u0631\u0633\u0627\u0644 \u062c\u062f\u06cc\u062f", None))
        self.postsBox.setTitle(QCoreApplication.translate("mainWindow", u"\u0627\u0631\u0633\u0627\u0644 \u0647\u0627", None))
        ___qtablewidgetitem = self.postsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\u0639\u0646\u0648\u0627\u0646", None));
        ___qtablewidgetitem1 = self.postsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0627\u0631\u06cc\u062e", None));
        ___qtablewidgetitem2 = self.postsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0644\u0627\u06cc\u062d\u0647 \u0647\u0627", None));
        ___qtablewidgetitem3 = self.postsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"\u0648\u0636\u0639\u06cc\u062a", None));
        ___qtablewidgetitem4 = self.postsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"\u0632\u0645\u0627\u0646 \u0634\u0631\u0648\u0639", None));
        ___qtablewidgetitem5 = self.postsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"\u0632\u0645\u0627\u0646 \u0627\u062a\u0645\u0627\u0645", None));
        ___qtablewidgetitem6 = self.postsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0645\u0648\u0641\u0642", None));
        ___qtablewidgetitem7 = self.postsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"\u062a\u0639\u062f\u0627\u062f \u062e\u0637\u0627", None));
        ___qtablewidgetitem8 = self.postsTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"\u0639\u0645\u0644\u06cc\u0627\u062a", None));
        self.searchBtn.setText(QCoreApplication.translate("mainWindow", u"\u062c\u0633\u062a \u0648 \u062c\u0648", None))
        self.searchLabel.setText(QCoreApplication.translate("mainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u06cc\u0627 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sendToDivanTab), QCoreApplication.translate("mainWindow", u"\u0627\u0631\u0633\u0627\u0644 \u0644\u0648\u0627\u06cc\u062d \u0628\u0647 \u062f\u06cc\u0648\u0627\u0646 \u0639\u062f\u0627\u0644\u062a \u0627\u062f\u0627\u0631\u06cc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fetchEblagh), QCoreApplication.translate("mainWindow", u"\u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0628\u0644\u0627\u063a\u06cc\u0647", None))
    # retranslateUi

