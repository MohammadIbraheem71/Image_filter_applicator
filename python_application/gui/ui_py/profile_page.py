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

class Ui_profile_pg(object):
    def setupUi(self, profile_pg):
        if not profile_pg.objectName():
            profile_pg.setObjectName(u"profile_pg")
        profile_pg.resize(381, 350)
        self.horizontalLayout_5 = QHBoxLayout(profile_pg)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profile_windows = QStackedWidget(profile_pg)
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


        self.retranslateUi(profile_pg)

        self.profile_windows.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(profile_pg)
    # setupUi

    def retranslateUi(self, profile_pg):
        self.login_btn.setText(QCoreApplication.translate("profile_pg", u"login", None))
        self.signup_btn.setText(QCoreApplication.translate("profile_pg", u"signup", None))
        self.label.setText(QCoreApplication.translate("profile_pg", u"logged in", None))
        pass
    # retranslateUi

