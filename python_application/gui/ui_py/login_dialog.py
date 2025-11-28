# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log-in_test.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        if not login_dialog.objectName():
            login_dialog.setObjectName(u"login_dialog")
        login_dialog.resize(531, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
        login_dialog.setSizePolicy(sizePolicy)
        login_dialog.setMinimumSize(QSize(531, 300))
        login_dialog.setMaximumSize(QSize(531, 500))
        login_dialog.setStyleSheet(u"/* -----------------------------------------\n"
"   DIALOG BACKGROUND WIDGET\n"
"----------------------------------------- */\n"
"QWidget#bg_widget {\n"
"    /* Full dialog background */\n"
"    /* FIX: Switched to background-image and related properties for a full background cover */\n"
"    background-image:url(:/icons/assets/sunset_2.jpg) ;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover; /* Tries to cover the entire area, similar to stretch */\n"
"    border: none;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   FORM WIDGET (on top of background)\n"
"----------------------------------------- */\n"
"QWidget#form_widget {\n"
"    background-color: rgba(220, 220, 220, 0.7); /* translucent grey */\n"
"    border: 1px solid rgba(200, 200, 200, 0.5); /* subtle border */\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   LABELS INSIDE FORM\n"
"---------------------------"
                        "-------------- */\n"
"QWidget#form_widget QLabel {\n"
"    background: transparent;  /* completely transparent, no outline */\n"
"    color: #2D2440;           /* dark text */\n"
"    font-weight: 500;\n"
"    padding: 0;               /* remove any extra spacing */\n"
"    border: none;             /* ensure no borders */\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   FORM INPUTS\n"
"----------------------------------------- */\n"
"QLineEdit, QTextEdit {\n"
"    background-color: rgba(255, 255, 255, 0.25);\n"
"    border: 1px solid rgba(255, 255, 255, 0.4);\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    color: #2D2440;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 0.35);\n"
"    border: 1px solid rgba(220, 180, 230, 0.8);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   SIGNUP BUTTON\n"
"----------------------------------------- */\n"
"QPushButton#login_btn {\n"
"    background-color: #"
                        "A855F7; /* solid purple */\n"
"    color: #FFFFFF;            /* white text */\n"
"    border: none;              /* clean look */\n"
"    border-radius: 8px;\n"
"    padding: 12px 20px;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton#login_btn:hover {\n"
"    background-color: #C084FC; /* lighter purple on hover */\n"
"}\n"
"\n"
"QPushButton#login_btn:pressed {\n"
"    background-color: #9333EA; /* darker purple on press */\n"
"    transform: scale(0.97);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   FORGOT PASSWORD BUTTON\n"
"----------------------------------------- */\n"
"QPushButton#forgot_password_btn {\n"
"    background-color: transparent;  /* no solid background */\n"
"    color: #6B7280;                 /* greyish text (Tailwind gray-500) */\n"
"    border: none;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"    text-decoration: underline;     /* optional: make it look like a link */\n"
"    padding: 4px 0;\n"
"}\n"
"\n"
"QPushButton#forgot_"
                        "password_btn:hover {\n"
"    color: #4B5563;                 /* slightly darker grey on hover */\n"
"    cursor: pointer;                /* show pointer cursor */\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(login_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bg_widget = QWidget(login_dialog)
        self.bg_widget.setObjectName(u"bg_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.bg_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.form_widget = QWidget(self.bg_widget)
        self.form_widget.setObjectName(u"form_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.form_widget.sizePolicy().hasHeightForWidth())
        self.form_widget.setSizePolicy(sizePolicy1)
        self.form_widget.setMinimumSize(QSize(260, 0))
        self.verticalLayout = QVBoxLayout(self.form_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.login_lbl = QLabel(self.form_widget)
        self.login_lbl.setObjectName(u"login_lbl")
        self.login_lbl.setMinimumSize(QSize(250, 0))
        self.login_lbl.setMaximumSize(QSize(250, 16777215))
        self.login_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.login_lbl)

        self.email_edt = QLineEdit(self.form_widget)
        self.email_edt.setObjectName(u"email_edt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.email_edt.sizePolicy().hasHeightForWidth())
        self.email_edt.setSizePolicy(sizePolicy2)
        self.email_edt.setMinimumSize(QSize(250, 0))
        self.email_edt.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.email_edt)

        self.passwrd_edt = QLineEdit(self.form_widget)
        self.passwrd_edt.setObjectName(u"passwrd_edt")
        sizePolicy2.setHeightForWidth(self.passwrd_edt.sizePolicy().hasHeightForWidth())
        self.passwrd_edt.setSizePolicy(sizePolicy2)
        self.passwrd_edt.setMinimumSize(QSize(250, 0))
        self.passwrd_edt.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.passwrd_edt)

        self.forgotpass_btn = QPushButton(self.form_widget)
        self.forgotpass_btn.setObjectName(u"forgotpass_btn")

        self.verticalLayout.addWidget(self.forgotpass_btn)

        self.login_btn = QPushButton(self.form_widget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(250, 0))
        self.login_btn.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.login_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.form_widget)


        self.horizontalLayout.addWidget(self.bg_widget)


        self.retranslateUi(login_dialog)

        QMetaObject.connectSlotsByName(login_dialog)
    # setupUi

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QCoreApplication.translate("login_dialog", u"Dialog", None))
        self.login_lbl.setText(QCoreApplication.translate("login_dialog", u"login", None))
        self.email_edt.setPlaceholderText(QCoreApplication.translate("login_dialog", u"email", None))
        self.passwrd_edt.setPlaceholderText(QCoreApplication.translate("login_dialog", u"password", None))
        self.forgotpass_btn.setText(QCoreApplication.translate("login_dialog", u"forgot password?", None))
        self.login_btn.setText(QCoreApplication.translate("login_dialog", u"login", None))
    # retranslateUi

