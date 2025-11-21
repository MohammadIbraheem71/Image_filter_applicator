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
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

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

        self.gallery_pg_btn = QPushButton(self.sidebar)
        self.gallery_pg_btn.setObjectName(u"gallery_pg_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gallery_pg_btn.sizePolicy().hasHeightForWidth())
        self.gallery_pg_btn.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.gallery_pg_btn)

        self.profile_pg_btn = QPushButton(self.sidebar)
        self.profile_pg_btn.setObjectName(u"profile_pg_btn")

        self.verticalLayout_2.addWidget(self.profile_pg_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.windows = QStackedWidget(self.centralwidget)
        self.windows.setObjectName(u"windows")
        self.garbage = QWidget()
        self.garbage.setObjectName(u"garbage")
        self.verticalLayout = QVBoxLayout(self.garbage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.new_img_lbl = QLabel(self.garbage)
        self.new_img_lbl.setObjectName(u"new_img_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.new_img_lbl.sizePolicy().hasHeightForWidth())
        self.new_img_lbl.setSizePolicy(sizePolicy1)
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

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.upload_btn = QPushButton(self.garbage)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.upload_btn)

        self.filter_cbx = QComboBox(self.garbage)
        self.filter_cbx.setObjectName(u"filter_cbx")

        self.horizontalLayout_3.addWidget(self.filter_cbx)

        self.download_btn = QPushButton(self.garbage)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.download_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.windows.addWidget(self.garbage)
        self.gallery_pg = QWidget()
        self.gallery_pg.setObjectName(u"gallery_pg")
        self.verticalLayout_3 = QVBoxLayout(self.gallery_pg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.upld_glry_btn = QPushButton(self.gallery_pg)
        self.upld_glry_btn.setObjectName(u"upld_glry_btn")

        self.horizontalLayout_4.addWidget(self.upld_glry_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(self.gallery_pg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.windows.addWidget(self.gallery_pg)
        self.profile_pg = QWidget()
        self.profile_pg.setObjectName(u"profile_pg")
        self.horizontalLayout_5 = QHBoxLayout(self.profile_pg)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profile_windows = QStackedWidget(self.profile_pg)
        self.profile_windows.setObjectName(u"profile_windows")
        self.auth_page = QWidget()
        self.auth_page.setObjectName(u"auth_page")
        self.verticalLayout_4 = QVBoxLayout(self.auth_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.login_btn = QPushButton(self.auth_page)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout_6.addWidget(self.login_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.signup_btn = QPushButton(self.auth_page)
        self.signup_btn.setObjectName(u"signup_btn")

        self.horizontalLayout_6.addWidget(self.signup_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.profile_windows.addWidget(self.auth_page)
        self.logged_page = QWidget()
        self.logged_page.setObjectName(u"logged_page")
        self.label = QLabel(self.logged_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 170, 141, 61))
        self.profile_windows.addWidget(self.logged_page)

        self.horizontalLayout_5.addWidget(self.profile_windows)

        self.windows.addWidget(self.profile_pg)

        self.horizontalLayout.addWidget(self.windows)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.windows.setCurrentIndex(0)
        self.profile_windows.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filter_pg_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.gallery_pg_btn.setText(QCoreApplication.translate("MainWindow", u"gallery", None))
        self.profile_pg_btn.setText(QCoreApplication.translate("MainWindow", u"profile", None))
        self.new_img_lbl.setText(QCoreApplication.translate("MainWindow", u"new image here", None))
        self.upload_btn.setText(QCoreApplication.translate("MainWindow", u"upload image", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"download image", None))
        self.upld_glry_btn.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"signup", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"logged in", None))
    # retranslateUi

