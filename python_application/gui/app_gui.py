# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_sw.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 559)
        MainWindow.setStyleSheet(u"/* -----------------------------------------\n"
"   GENERAL\n"
"----------------------------------------- */\n"
"QWidget {\n"
"    background-color: #FFEFE6;   /* soft peach background */\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    color: #5A3E36;              /* warm brown text */\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   BUTTONS\n"
"----------------------------------------- */\n"
"QPushButton {\n"
"    background-color: #FFD9C7;       /* peach */\n"
"    color: #5A3E36;                  /* warm brown */\n"
"    border: 2px solid #FFCDB8;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"\n"
"    /* subtle shadow */\n"
"    box-shadow: 0 2px 4px rgba(0,0,0,0.15);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFCCBC;       /* slightly darker peach */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F8BAA7;       /* deeper peach when pressed */\n"
"    border: 2px solid #F3A88F;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QPus"
                        "hButton:disabled {\n"
"    background-color: #F5DAD1;\n"
"    color: #A88E86;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   COMBO BOX\n"
"----------------------------------------- */\n"
"/*\n"
"QComboBox {\n"
"    background-color: #FFE3D7;\n"
"    border: 2px solid #FFCDB8;\n"
"    border-radius: 8px;\n"
"    padding: 6px 30px 6px 10px;   /* leave space for arrow \n"
"    color: #5A3E36;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #FFCDB8;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0; \n"
"    height: 0;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 7px solid #5A3E36; \n"
"    margin-right: 5px;\n"
"}\n"
"*/\n"
"\n"
"/* hover */\n"
"QComboBox:hover {\n"
"    background-color: #FFD9C9;\n"
"}\n"
"\n"
"/* pressed */\n"
"QComboBox:pressed {\n"
"    background-color: #F8CAB8;\n"
"}\n"
"\n"
"/* po"
                        "pup list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFEFE6;\n"
"    border: 1px solid #FFCDB8;\n"
"    selection-background-color: #FFD4C4;\n"
"    selection-color: #5A3E36;\n"
"    outline: 0;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(50, 0))
        self.sidebar.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.filter_pg_btn = QPushButton(self.sidebar)
        self.filter_pg_btn.setObjectName(u"filter_pg_btn")
        self.filter_pg_btn.setMinimumSize(QSize(30, 0))
        self.filter_pg_btn.setMaximumSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.filter_pg_btn)

        self.pushButton = QPushButton(self.sidebar)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.sidebar)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.windows = QStackedWidget(self.centralwidget)
        self.windows.setObjectName(u"windows")
        self.filter_pg = QWidget()
        self.filter_pg.setObjectName(u"filter_pg")
        self.verticalLayout = QVBoxLayout(self.filter_pg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.og_img_lbl = QLabel(self.filter_pg)
        self.og_img_lbl.setObjectName(u"og_img_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.og_img_lbl.sizePolicy().hasHeightForWidth())
        self.og_img_lbl.setSizePolicy(sizePolicy)
        self.og_img_lbl.setMinimumSize(QSize(200, 200))
        self.og_img_lbl.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.og_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.og_img_lbl)

        self.new_img_lbl = QLabel(self.filter_pg)
        self.new_img_lbl.setObjectName(u"new_img_lbl")
        sizePolicy.setHeightForWidth(self.new_img_lbl.sizePolicy().hasHeightForWidth())
        self.new_img_lbl.setSizePolicy(sizePolicy)
        self.new_img_lbl.setMinimumSize(QSize(200, 200))
        self.new_img_lbl.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.new_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.new_img_lbl)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.upload_btn = QPushButton(self.filter_pg)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.upload_btn)

        self.filter_cbx = QComboBox(self.filter_pg)
        self.filter_cbx.setObjectName(u"filter_cbx")

        self.horizontalLayout_3.addWidget(self.filter_cbx)

        self.download_btn = QPushButton(self.filter_pg)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.download_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.windows.addWidget(self.filter_pg)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.windows.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.windows)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filter_pg_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.og_img_lbl.setText(QCoreApplication.translate("MainWindow", u"original image here", None))
        self.new_img_lbl.setText(QCoreApplication.translate("MainWindow", u"new image here", None))
        self.upload_btn.setText(QCoreApplication.translate("MainWindow", u"upload image", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"download image", None))
    # retranslateUi

