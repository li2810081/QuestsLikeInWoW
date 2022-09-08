# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 557)
        MainWindow.setDockOptions(QMainWindow.AnimatedDocks|QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.q_list = QWidget(MainWindow)
        self.q_list.setObjectName(u"q_list")
        self.verticalLayout_4 = QVBoxLayout(self.q_list)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.q_quest = QWidget(self.q_list)
        self.q_quest.setObjectName(u"q_quest")
        self.verticalLayout_2 = QVBoxLayout(self.q_quest)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.q_name = QLabel(self.q_quest)
        self.q_name.setObjectName(u"q_name")

        self.verticalLayout.addWidget(self.q_name)

        self.q_remark = QLabel(self.q_quest)
        self.q_remark.setObjectName(u"q_remark")

        self.verticalLayout.addWidget(self.q_remark)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.q_quest)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.q_list)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.q_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.q_remark.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

