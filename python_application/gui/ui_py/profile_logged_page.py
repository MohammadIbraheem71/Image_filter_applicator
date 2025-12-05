# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_logged_page.ui'
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
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_profile_logged_page(object):
    def setupUi(self, profile_logged_page):
        if not profile_logged_page.objectName():
            profile_logged_page.setObjectName(u"profile_logged_page")
        profile_logged_page.resize(540, 465)
        self.verticalLayout = QVBoxLayout(profile_logged_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.welcome_lbl = QLabel(profile_logged_page)
        self.welcome_lbl.setObjectName(u"welcome_lbl")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setStyleSheet(u"font-size: 30pt;")
        self.welcome_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.welcome_lbl)

        self.email_lbl = QLabel(profile_logged_page)
        self.email_lbl.setObjectName(u"email_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_lbl.sizePolicy().hasHeightForWidth())
        self.email_lbl.setSizePolicy(sizePolicy)
        self.email_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.email_lbl)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.img_count_lbl = QLabel(profile_logged_page)
        self.img_count_lbl.setObjectName(u"img_count_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img_count_lbl.sizePolicy().hasHeightForWidth())
        self.img_count_lbl.setSizePolicy(sizePolicy1)
        self.img_count_lbl.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(False)
        self.img_count_lbl.setFont(font1)
        self.img_count_lbl.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.12);  /* translucent */\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    padding: 8px;")
        self.img_count_lbl.setFrameShape(QFrame.Shape.NoFrame)
        self.img_count_lbl.setFrameShadow(QFrame.Shadow.Plain)
        self.img_count_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_count_lbl.setWordWrap(True)

        self.horizontalLayout.addWidget(self.img_count_lbl)

        self.like_count_lbl = QLabel(profile_logged_page)
        self.like_count_lbl.setObjectName(u"like_count_lbl")
        sizePolicy1.setHeightForWidth(self.like_count_lbl.sizePolicy().hasHeightForWidth())
        self.like_count_lbl.setSizePolicy(sizePolicy1)
        self.like_count_lbl.setMinimumSize(QSize(0, 0))
        self.like_count_lbl.setFont(font1)
        self.like_count_lbl.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.12);  /* translucent */\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    padding: 8px;")
        self.like_count_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.like_count_lbl.setWordWrap(True)

        self.horizontalLayout.addWidget(self.like_count_lbl)

        self.verified_status_lbl = QLabel(profile_logged_page)
        self.verified_status_lbl.setObjectName(u"verified_status_lbl")
        sizePolicy.setHeightForWidth(self.verified_status_lbl.sizePolicy().hasHeightForWidth())
        self.verified_status_lbl.setSizePolicy(sizePolicy)
        self.verified_status_lbl.setMinimumSize(QSize(0, 80))
        self.verified_status_lbl.setFont(font1)
        self.verified_status_lbl.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.12);  /* translucent */\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    padding: 8px;")
        self.verified_status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verified_status_lbl.setWordWrap(True)

        self.horizontalLayout.addWidget(self.verified_status_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(profile_logged_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.image_grid = QWidget()
        self.image_grid.setObjectName(u"image_grid")
        self.image_grid.setGeometry(QRect(0, 0, 514, 212))
        self.scrollArea.setWidget(self.image_grid)

        self.verticalLayout.addWidget(self.scrollArea)

        self.logout_btn = QPushButton(profile_logged_page)
        self.logout_btn.setObjectName(u"logout_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/leave.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_btn.setIcon(icon)
        self.logout_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.logout_btn)


        self.retranslateUi(profile_logged_page)

        QMetaObject.connectSlotsByName(profile_logged_page)
    # setupUi

    def retranslateUi(self, profile_logged_page):
        profile_logged_page.setWindowTitle(QCoreApplication.translate("profile_logged_page", u"Form", None))
        self.welcome_lbl.setText(QCoreApplication.translate("profile_logged_page", u"Welcome", None))
        self.email_lbl.setText(QCoreApplication.translate("profile_logged_page", u"Email", None))
        self.img_count_lbl.setText(QCoreApplication.translate("profile_logged_page", u"img count here", None))
        self.like_count_lbl.setText(QCoreApplication.translate("profile_logged_page", u"like count here", None))
        self.verified_status_lbl.setText(QCoreApplication.translate("profile_logged_page", u"verified status here", None))
        self.logout_btn.setText(QCoreApplication.translate("profile_logged_page", u"Log out", None))
    # retranslateUi

