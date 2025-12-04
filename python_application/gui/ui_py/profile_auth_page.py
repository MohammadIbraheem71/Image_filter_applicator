# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_auth_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_profile_auth_page(object):
    def setupUi(self, profile_auth_page):
        if not profile_auth_page.objectName():
            profile_auth_page.setObjectName(u"profile_auth_page")
        profile_auth_page.resize(543, 480)
        self.horizontalLayout = QHBoxLayout(profile_auth_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sign_up_btn = QPushButton(profile_auth_page)
        self.sign_up_btn.setObjectName(u"sign_up_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/globe.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sign_up_btn.setIcon(icon)
        self.sign_up_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.sign_up_btn)

        self.log_in_btn = QPushButton(profile_auth_page)
        self.log_in_btn.setObjectName(u"log_in_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/entrance.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.log_in_btn.setIcon(icon1)
        self.log_in_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.log_in_btn)


        self.retranslateUi(profile_auth_page)

        QMetaObject.connectSlotsByName(profile_auth_page)
    # setupUi

    def retranslateUi(self, profile_auth_page):
        profile_auth_page.setWindowTitle(QCoreApplication.translate("profile_auth_page", u"Form", None))
        self.sign_up_btn.setText(QCoreApplication.translate("profile_auth_page", u"sign up", None))
        self.log_in_btn.setText(QCoreApplication.translate("profile_auth_page", u"log in", None))
    # retranslateUi

