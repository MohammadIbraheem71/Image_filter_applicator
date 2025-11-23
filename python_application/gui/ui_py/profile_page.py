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
    QSizePolicy, QStackedWidget, QWidget)
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
        self.logged_pg = QWidget()
        self.logged_pg.setObjectName(u"logged_pg")
        self.horizontalLayout_3 = QHBoxLayout(self.logged_pg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.logged_pg)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.profile_windows.addWidget(self.logged_pg)
        self.auth_pg = QWidget()
        self.auth_pg.setObjectName(u"auth_pg")
        self.horizontalLayout_2 = QHBoxLayout(self.auth_pg)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sign_up_btn = QPushButton(self.auth_pg)
        self.sign_up_btn.setObjectName(u"sign_up_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/signup_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sign_up_btn.setIcon(icon)
        self.sign_up_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.sign_up_btn)

        self.log_in_btn = QPushButton(self.auth_pg)
        self.log_in_btn.setObjectName(u"log_in_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/login_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.log_in_btn.setIcon(icon1)
        self.log_in_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.log_in_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.profile_windows.addWidget(self.auth_pg)

        self.horizontalLayout_5.addWidget(self.profile_windows)


        self.retranslateUi(profile_pg)

        self.profile_windows.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(profile_pg)
    # setupUi

    def retranslateUi(self, profile_pg):
        self.label.setText(QCoreApplication.translate("profile_pg", u"you are logged in", None))
        self.sign_up_btn.setText(QCoreApplication.translate("profile_pg", u"sign up", None))
        self.log_in_btn.setText(QCoreApplication.translate("profile_pg", u"log in", None))
        pass
    # retranslateUi

