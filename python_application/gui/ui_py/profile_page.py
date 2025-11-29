# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_profile_pg(object):
    def setupUi(self, profile_pg):
        if not profile_pg.objectName():
            profile_pg.setObjectName(u"profile_pg")
        profile_pg.resize(541, 467)
        self.horizontalLayout_5 = QHBoxLayout(profile_pg)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profile_windows = QStackedWidget(profile_pg)
        self.profile_windows.setObjectName(u"profile_windows")
        self.profile_windows.setStyleSheet(u"")
        self.logged_pg = QWidget()
        self.logged_pg.setObjectName(u"logged_pg")
        self.horizontalLayout_3 = QHBoxLayout(self.logged_pg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.welcome_lbl = QLabel(self.logged_pg)
        self.welcome_lbl.setObjectName(u"welcome_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_lbl.sizePolicy().hasHeightForWidth())
        self.welcome_lbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        font.setKerning(True)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.welcome_lbl.setStyleSheet(u"background-color: #D0E4F7;       /* Purple background */\n"
"        color: #2A3E5C;                        /* Text color */\n"
"        font-size: 26px;                  /* Large text */\n"
"        font-weight: 600;                 /* Semi-bold */\n"
"        padding: 14px 24px;               /* Padding inside label */\n"
"        border-radius: 16px;              /* Rounded corners */\n"
"        border: 5px solid #A3C2E7;          /* Black border */\n"
"        letter-spacing: 1px;")
        self.welcome_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.welcome_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.email_lbl = QLabel(self.logged_pg)
        self.email_lbl.setObjectName(u"email_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.email_lbl.sizePolicy().hasHeightForWidth())
        self.email_lbl.setSizePolicy(sizePolicy1)
        self.email_lbl.setStyleSheet(u"background-color: #D0E4F7;  \n"
"        color: #2A3E5C;                  /* Text color */\n"
"        font-size: 16px;\n"
"        font-weight: 500;\n"
"        padding: 6px 12px;           /* Padding inside badge */\n"
"        border-radius: 12px;         /* Rounded corners */\n"
"        border: 2px solid #A3C2E7;  /* Black border */\n"
"        font-family: 'Segoe UI', 'Poppins', sans-serif;\n"
"")

        self.verticalLayout_12.addWidget(self.email_lbl)

        self.image_count_lbl = QLabel(self.logged_pg)
        self.image_count_lbl.setObjectName(u"image_count_lbl")
        sizePolicy.setHeightForWidth(self.image_count_lbl.sizePolicy().hasHeightForWidth())
        self.image_count_lbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.Medium)
        self.image_count_lbl.setFont(font1)
        self.image_count_lbl.setStyleSheet(u"background-color: #D0E4F7;  \n"
"        color: #2A3E5C;                   /* Text color */\n"
"        font-size: 16px;\n"
"        font-weight: 500;\n"
"        padding: 6px 12px;           /* Padding inside badge */\n"
"        border-radius: 12px;         /* Rounded corners */\n"
"        border: 2px solid #A3C2E7;     /* Black border */\n"
"        font-family: 'Segoe UI', 'Poppins', sans-serif;\n"
"")

        self.verticalLayout_12.addWidget(self.image_count_lbl)

        self.likes_lbl = QLabel(self.logged_pg)
        self.likes_lbl.setObjectName(u"likes_lbl")
        sizePolicy1.setHeightForWidth(self.likes_lbl.sizePolicy().hasHeightForWidth())
        self.likes_lbl.setSizePolicy(sizePolicy1)
        self.likes_lbl.setStyleSheet(u"background-color: #D0E4F7;   \n"
"        color: #2A3E5C;                   /* Text color */\n"
"        font-size: 16px;\n"
"        font-weight: 500;\n"
"        padding: 6px 12px;           /* Padding inside badge */\n"
"        border-radius: 12px;         /* Rounded corners */\n"
"        border: 2px solid #A3C2E7;     /* Black border */\n"
"        font-family: 'Segoe UI', 'Poppins', sans-serif;\n"
"")

        self.verticalLayout_12.addWidget(self.likes_lbl)

        self.verification_lbl = QLabel(self.logged_pg)
        self.verification_lbl.setObjectName(u"verification_lbl")
        sizePolicy1.setHeightForWidth(self.verification_lbl.sizePolicy().hasHeightForWidth())
        self.verification_lbl.setSizePolicy(sizePolicy1)
        self.verification_lbl.setStyleSheet(u"background-color: #D0E4F7;  \n"
"        color: #2A3E5C;                   /* Text color */\n"
"        font-size: 16px;\n"
"        font-weight: 500;\n"
"        padding: 6px 12px;           /* Padding inside badge */\n"
"        border-radius: 12px;         /* Rounded corners */\n"
"        border: 2px solid #A3C2E7;     /* Black border */\n"
"        font-family: 'Segoe UI', 'Poppins', sans-serif;\n"
"")

        self.verticalLayout_12.addWidget(self.verification_lbl)


        self.verticalLayout.addLayout(self.verticalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.logout_btn = QPushButton(self.logged_pg)
        self.logout_btn.setObjectName(u"logout_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/leave.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_btn.setIcon(icon)
        self.logout_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.logout_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.profile_windows.addWidget(self.logged_pg)
        self.auth_pg = QWidget()
        self.auth_pg.setObjectName(u"auth_pg")
        self.horizontalLayout_2 = QHBoxLayout(self.auth_pg)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sign_up_btn = QPushButton(self.auth_pg)
        self.sign_up_btn.setObjectName(u"sign_up_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/globe.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sign_up_btn.setIcon(icon1)
        self.sign_up_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.sign_up_btn)

        self.log_in_btn = QPushButton(self.auth_pg)
        self.log_in_btn.setObjectName(u"log_in_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/entrance.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.log_in_btn.setIcon(icon2)
        self.log_in_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.log_in_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.profile_windows.addWidget(self.auth_pg)

        self.horizontalLayout_5.addWidget(self.profile_windows)


        self.retranslateUi(profile_pg)

        self.profile_windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(profile_pg)
    # setupUi

    def retranslateUi(self, profile_pg):
        self.welcome_lbl.setText(QCoreApplication.translate("profile_pg", u"Welcome", None))
        self.email_lbl.setText(QCoreApplication.translate("profile_pg", u"email", None))
        self.image_count_lbl.setText(QCoreApplication.translate("profile_pg", u"Welcome", None))
        self.likes_lbl.setText(QCoreApplication.translate("profile_pg", u"TextLabel", None))
        self.verification_lbl.setText(QCoreApplication.translate("profile_pg", u"TextLabel", None))
        self.logout_btn.setText(QCoreApplication.translate("profile_pg", u"Log out", None))
        self.sign_up_btn.setText(QCoreApplication.translate("profile_pg", u"sign up", None))
        self.log_in_btn.setText(QCoreApplication.translate("profile_pg", u"log in", None))
        pass
    # retranslateUi

