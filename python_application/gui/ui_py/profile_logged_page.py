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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_profile_logged_page(object):
    def setupUi(self, profile_logged_page):
        if not profile_logged_page.objectName():
            profile_logged_page.setObjectName(u"profile_logged_page")
        profile_logged_page.resize(540, 465)
        self.verticalLayout = QVBoxLayout(profile_logged_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.welcome_lbl = QLabel(profile_logged_page)
        self.welcome_lbl.setObjectName(u"welcome_lbl")

        self.horizontalLayout.addWidget(self.welcome_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.email_lbl = QLabel(profile_logged_page)
        self.email_lbl.setObjectName(u"email_lbl")

        self.verticalLayout_2.addWidget(self.email_lbl)

        self.img_count_lbl = QLabel(profile_logged_page)
        self.img_count_lbl.setObjectName(u"img_count_lbl")

        self.verticalLayout_2.addWidget(self.img_count_lbl)

        self.like_count_lbl = QLabel(profile_logged_page)
        self.like_count_lbl.setObjectName(u"like_count_lbl")

        self.verticalLayout_2.addWidget(self.like_count_lbl)

        self.verified_status_lbl = QLabel(profile_logged_page)
        self.verified_status_lbl.setObjectName(u"verified_status_lbl")

        self.verticalLayout_2.addWidget(self.verified_status_lbl)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(profile_logged_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.image_grid = QWidget()
        self.image_grid.setObjectName(u"image_grid")
        self.image_grid.setGeometry(QRect(0, 0, 520, 287))
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

