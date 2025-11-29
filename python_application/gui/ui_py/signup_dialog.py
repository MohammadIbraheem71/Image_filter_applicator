# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign-up_test.ui'
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

class Ui_signup_dialog(object):
    def setupUi(self, signup_dialog):
        if not signup_dialog.objectName():
            signup_dialog.setObjectName(u"signup_dialog")
        signup_dialog.resize(531, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(signup_dialog.sizePolicy().hasHeightForWidth())
        signup_dialog.setSizePolicy(sizePolicy)
        signup_dialog.setMinimumSize(QSize(531, 300))
        signup_dialog.setMaximumSize(QSize(531, 500))
        signup_dialog.setStyleSheet(u"/* -----------------------------------------\n"
"   DIALOG BACKGROUND WIDGET\n"
"----------------------------------------- */\n"
"QWidget#bg_widget {\n"
"    /* Full dialog background */\n"
"    /* FIX: Switched to background-image and related properties for a full background cover */\n"
"    background-image: url(:/icons/assets/manhattn_sunset_crp.png);\n"
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
"----------------"
                        "------------------------- */\n"
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
"QPushButton#signup_btn {\n"
"    backgro"
                        "und-color: #A855F7; /* solid purple */\n"
"    color: #FFFFFF;            /* white text */\n"
"    border: none;              /* clean look */\n"
"    border-radius: 8px;\n"
"    padding: 12px 20px;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton#signup_btn:hover {\n"
"    background-color: #C084FC; /* lighter purple on hover */\n"
"}\n"
"\n"
"QPushButton#signup_btn:pressed {\n"
"    background-color: #9333EA; /* darker purple on press */\n"
"    transform: scale(0.97);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(signup_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bg_widget = QWidget(signup_dialog)
        self.bg_widget.setObjectName(u"bg_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.bg_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.sign_up_lbl = QLabel(self.form_widget)
        self.sign_up_lbl.setObjectName(u"sign_up_lbl")
        self.sign_up_lbl.setMinimumSize(QSize(250, 0))
        self.sign_up_lbl.setMaximumSize(QSize(250, 16777215))
        self.sign_up_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.sign_up_lbl)

        self.username_edt = QLineEdit(self.form_widget)
        self.username_edt.setObjectName(u"username_edt")
        sizePolicy.setHeightForWidth(self.username_edt.sizePolicy().hasHeightForWidth())
        self.username_edt.setSizePolicy(sizePolicy)
        self.username_edt.setMinimumSize(QSize(250, 0))
        self.username_edt.setMaximumSize(QSize(250, 16777215))
        self.username_edt.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.username_edt)

        self.email_edt = QLineEdit(self.form_widget)
        self.email_edt.setObjectName(u"email_edt")
        sizePolicy.setHeightForWidth(self.email_edt.sizePolicy().hasHeightForWidth())
        self.email_edt.setSizePolicy(sizePolicy)
        self.email_edt.setMinimumSize(QSize(250, 0))
        self.email_edt.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.email_edt)

        self.passwrd_edt = QLineEdit(self.form_widget)
        self.passwrd_edt.setObjectName(u"passwrd_edt")
        sizePolicy.setHeightForWidth(self.passwrd_edt.sizePolicy().hasHeightForWidth())
        self.passwrd_edt.setSizePolicy(sizePolicy)
        self.passwrd_edt.setMinimumSize(QSize(250, 0))
        self.passwrd_edt.setMaximumSize(QSize(250, 16777215))
        self.passwrd_edt.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passwrd_edt)

        self.crm_passwrd_edt = QLineEdit(self.form_widget)
        self.crm_passwrd_edt.setObjectName(u"crm_passwrd_edt")
        sizePolicy.setHeightForWidth(self.crm_passwrd_edt.sizePolicy().hasHeightForWidth())
        self.crm_passwrd_edt.setSizePolicy(sizePolicy)
        self.crm_passwrd_edt.setMinimumSize(QSize(25, 0))
        self.crm_passwrd_edt.setMaximumSize(QSize(250, 16777215))
        self.crm_passwrd_edt.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.crm_passwrd_edt)

        self.error_lbl = QLabel(self.form_widget)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setMinimumSize(QSize(0, 30))
        self.error_lbl.setStyleSheet(u"    background-color: rgba(248, 215, 218, 150); /* light red with 150/255 opacity */\n"
"    color: rgb(196, 62, 57);                              /* dark red text */\n"
"    border: 1px solid rgba(196, 62, 57, 200);  /* optional semi-transparent border */\n"
"    border-radius: 4px;\n"
"    padding: 2px 4px;\n"
"")
        self.error_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.error_lbl)

        self.success_lbl = QLabel(self.form_widget)
        self.success_lbl.setObjectName(u"success_lbl")
        self.success_lbl.setMinimumSize(QSize(0, 30))
        self.success_lbl.setStyleSheet(u"background-color: rgba(198, 239, 206, 150); /* light green with 150/255 opacity */\n"
"color: rgb(0, 97, 0);                        /* dark green text */\n"
"border: 1px solid rgba(0, 97, 0, 200);      /* optional semi-transparent border */\n"
"border-radius: 4px;\n"
"padding: 2px 4px;\n"
"")
        self.success_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.success_lbl)

        self.signup_btn = QPushButton(self.form_widget)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setMinimumSize(QSize(250, 0))
        self.signup_btn.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.signup_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.form_widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.bg_widget)


        self.retranslateUi(signup_dialog)

        QMetaObject.connectSlotsByName(signup_dialog)
    # setupUi

    def retranslateUi(self, signup_dialog):
        signup_dialog.setWindowTitle(QCoreApplication.translate("signup_dialog", u"Dialog", None))
        self.sign_up_lbl.setText(QCoreApplication.translate("signup_dialog", u"sign up", None))
        self.username_edt.setPlaceholderText(QCoreApplication.translate("signup_dialog", u"username", None))
        self.email_edt.setPlaceholderText(QCoreApplication.translate("signup_dialog", u"email", None))
        self.passwrd_edt.setPlaceholderText(QCoreApplication.translate("signup_dialog", u"password", None))
        self.crm_passwrd_edt.setPlaceholderText(QCoreApplication.translate("signup_dialog", u"confirm password", None))
        self.error_lbl.setText(QCoreApplication.translate("signup_dialog", u"TextLabel", None))
        self.success_lbl.setText(QCoreApplication.translate("signup_dialog", u"TextLabel", None))
        self.signup_btn.setText(QCoreApplication.translate("signup_dialog", u"sign up", None))
    # retranslateUi

