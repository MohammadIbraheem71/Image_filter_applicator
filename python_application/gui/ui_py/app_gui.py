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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 559)
        MainWindow.setStyleSheet(u"/* -----------------------------------------\n"
"   GENERAL\n"
"----------------------------------------- */\n"
"QWidget {\n"
"    background-color: #E6F0FA;   /* soft light blue */\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    color: #2A3E5C;              /* dark blue text for contrast */\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   BUTTONS (GENERAL)\n"
"----------------------------------------- */\n"
"QPushButton {\n"
"    background-color: #D0E4F7;       /* pale blue */\n"
"    color: #2A3E5C;                  /* dark blue text */\n"
"    border: 2px solid #A3C2E7;       /* subtle border */\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* soft shadow */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B7D6F2;       /* slightly darker on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A3C2E7;       /* deeper blue when pressed */\n"
"    border: 2px solid #91B3DC;\n"
"}\n"
""
                        "\n"
"/* Disabled state */\n"
"QPushButton:disabled {\n"
"    background-color: #D9E7F5;\n"
"    color: #A3B9C9;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   SIDEBAR\n"
"----------------------------------------- */\n"
"QFrame#sidebar {\n"
"    background-color: #C6DEF8;       /* slightly darker blue */\n"
"    border: 2px solid #91B3DC; /* subtle outline */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel#logo_gif{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   SIDEBAR BUTTONS (ICON ONLY)\n"
"----------------------------------------- */\n"
"QPushButton#filter_pg_btn,\n"
"QPushButton#gallery_pg_btn,\n"
"QPushButton#profile_pg_btn {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: transparent;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QPushButton#filter_pg_btn:hover,\n"
"QPushButton#gallery_pg_btn:hover,\n"
"QPushButton#profile_pg_btn:hover {\n"
"    background-color: rgba(41, 128, 185, 0.1); /*"
                        " soft hover effect */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#filter_pg_btn:pressed,\n"
"QPushButton#gallery_pg_btn:pressed,\n"
"QPushButton#profile_pg_btn:pressed {\n"
"    background-color: rgba(41, 128, 185, 0.2); /* subtle press effect */\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   COMBO BOX\n"
"----------------------------------------- */\n"
"QComboBox {\n"
"    background-color: #D0E4F7;\n"
"    border: 2px solid #A3C2E7;\n"
"    border-radius: 8px;\n"
"    padding: 6px 30px 6px 10px; /* leave space for arrow */\n"
"    color: #2A3E5C;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #A3C2E7;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0; \n"
"    height: 0;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 7px solid #2A3E5C; \n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"/* hover */\n"
""
                        "QComboBox:hover {\n"
"    background-color: #B7D6F2;\n"
"}\n"
"\n"
"/* pressed */\n"
"QComboBox:pressed {\n"
"    background-color: #A3C2E7;\n"
"}\n"
"\n"
"/* popup list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #E6F0FA;\n"
"    border: 1px solid #A3C2E7;\n"
"    selection-background-color: #B7D6F2;\n"
"    selection-color: #2A3E5C;\n"
"    outline: 0;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(62, 0))
        self.sidebar.setMaximumSize(QSize(62, 16777215))
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_gif = QLabel(self.sidebar)
        self.logo_gif.setObjectName(u"logo_gif")

        self.verticalLayout_2.addWidget(self.logo_gif)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.filter_pg_btn = QPushButton(self.sidebar)
        self.filter_pg_btn.setObjectName(u"filter_pg_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filter_pg_btn.sizePolicy().hasHeightForWidth())
        self.filter_pg_btn.setSizePolicy(sizePolicy1)
        self.filter_pg_btn.setMinimumSize(QSize(0, 0))
        self.filter_pg_btn.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/assets/filter_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filter_pg_btn.setIcon(icon)
        self.filter_pg_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.filter_pg_btn)

        self.gallery_pg_btn = QPushButton(self.sidebar)
        self.gallery_pg_btn.setObjectName(u"gallery_pg_btn")
        sizePolicy1.setHeightForWidth(self.gallery_pg_btn.sizePolicy().hasHeightForWidth())
        self.gallery_pg_btn.setSizePolicy(sizePolicy1)
        self.gallery_pg_btn.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/gallery_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gallery_pg_btn.setIcon(icon1)
        self.gallery_pg_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.gallery_pg_btn)

        self.profile_pg_btn = QPushButton(self.sidebar)
        self.profile_pg_btn.setObjectName(u"profile_pg_btn")
        self.profile_pg_btn.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/profile_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_pg_btn.setIcon(icon2)
        self.profile_pg_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.profile_pg_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.windows = QStackedWidget(self.centralwidget)
        self.windows.setObjectName(u"windows")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.windows.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.windows.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.windows)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_gif.setText(QCoreApplication.translate("MainWindow", u"logo here", None))
        self.filter_pg_btn.setText("")
        self.gallery_pg_btn.setText("")
        self.profile_pg_btn.setText("")
    # retranslateUi

