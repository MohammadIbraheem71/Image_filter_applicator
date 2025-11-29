# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_dialog.ui'
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

class Ui_upload_dialog(object):
    def setupUi(self, upload_dialog):
        if not upload_dialog.objectName():
            upload_dialog.setObjectName(u"upload_dialog")
        upload_dialog.resize(489, 443)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(upload_dialog.sizePolicy().hasHeightForWidth())
        upload_dialog.setSizePolicy(sizePolicy)
        upload_dialog.setStyleSheet(u"/* -----------------------------------------\n"
"   UPLOAD DIALOG BACKGROUND WIDGET\n"
"----------------------------------------- */\n"
"QWidget#bg_widget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 87, 203, 255), stop:1 rgba(0, 85, 255, 255));\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* -----------------------------------------\n"
"   UPLOAD FORM CARD (Glass Panel)\n"
"----------------------------------------- */\n"
"QWidget#form_widget {\n"
"    background-color: rgba(240, 240, 240, 0.65); /* lighter translucent glass */\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.45);\n"
"    padding: 20px;\n"
"    backdrop-filter: blur(8px);  /* supported on Mac, ignored on Windows */\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   LABELS INSIDE UPLOAD FORM\n"
"----------------------------------------- */\n"
"QWidget#upload_form_widget QLabel {\n"
"    background: transparent;\n"
"    color: #2D2440; \n"
"    font-weight: 50"
                        "0;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   INPUT FIELDS\n"
"----------------------------------------- */\n"
"QLineEdit#description_edt {\n"
"    background-color: rgba(255, 255, 255, 0.25);\n"
"    border: 1px solid rgba(255, 255, 255, 0.45);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #2D2440;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit#title_edit:focus,\n"
"QTextEdit#description_edt:focus,\n"
"QLineEdit#tags_edit:focus {\n"
"    background-color: rgba(255, 255, 255, 0.35);\n"
"    border: 1px solid rgba(200, 150, 230, 0.9);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   IMAGE WIDGET (Card-style glassmorphism)\n"
"----------------------------------------- */\n"
"QWidget#img_widget {\n"
"    background-color: rgba(255, 255, 255, 0.10);     /* subtle glass layer */\n"
"    border: 1px solid rgba(255, 255, 255, 0.18);      /* soft edge */\n"
"    border-radius: 14px;\n"
""
                        "    padding: 8px;\n"
"\n"
"    /* Optional: smooth transition on hover */\n"
"    transition: background-color 150ms ease,\n"
"                border 150ms ease;\n"
"}\n"
"\n"
"/* Hover effect - stronger glass glow */\n"
"QWidget#img_widget:hover {\n"
"    background-color: rgba(255, 255, 255, 0.18);\n"
"    border: 1px solid rgba(255, 255, 255, 0.30);\n"
"}\n"
"\n"
"/* Inside labels (optional cleanup) */\n"
"QWidget#img_widget QLabel {\n"
"    background: transparent;\n"
"    color: #F5F0FF; /* soft white text */\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* -----------------------------------------\n"
"   SELECT IMAGE BUTTON (Glass Style)\n"
"----------------------------------------- */\n"
"QPushButton#select_img_btn {\n"
"    background-color: rgba(255, 255, 255, 0.12);   /* Translucent glass */\n"
"    color: #F5F0FF;\n"
"    border: 1px solid rgba(255, 255, 255, 0.25);\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"    min-height: 36px;\n"
"}\n"
""
                        "\n"
"/* Hover - stronger glass glow */\n"
"QPushButton#select_img_btn:hover {\n"
"    background-color: rgba(255, 255, 255, 0.18);\n"
"    border: 1px solid rgba(255, 255, 255, 0.35);\n"
"}\n"
"\n"
"/* Pressed - slightly darker */\n"
"QPushButton#select_img_btn:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.20);\n"
"    transform: scale(0.97);\n"
"}\n"
"\n"
"\n"
"/* -----------------------------------------\n"
"   UPLOAD BUTTON\n"
"----------------------------------------- */\n"
"QPushButton#upload_btn {\n"
"    background-color:rgb(168, 85, 247) ;\n"
"	color: rgb(30, 24, 64);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 12px 20px;\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QPushButton#upload_btn:hover {\n"
"    background-color: #C084FC;\n"
"}\n"
"\n"
"QPushButton#upload_btn:pressed {\n"
"    background-color: #9333EA;\n"
"    transform: scale(0.97);\n"
"}\n"
"\n"
"/* ---------------------------------"
                        "--------\n"
"   CANCEL BUTTON\n"
"----------------------------------------- */\n"
"QPushButton#cancel_btn {\n"
"    background-color: rgba(0,0,0,0.25);\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#cancel_btn:hover {\n"
"    background-color: rgba(0,0,0,0.38);\n"
"}\n"
"\n"
"QPushButton#cancel_btn:pressed {\n"
"    background-color: rgba(0,0,0,0.50);\n"
"    transform: scale(0.97);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   IMAGE PREVIEW BOX\n"
"----------------------------------------- */\n"
"QLabel#preview_lbl {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(255, 255, 255, 0.45);\n"
"    border-radius: 12px;\n"
"    padding: 5px;\n"
"    min-height: 160px; /* adjust as needed */\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(upload_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bg_widget = QWidget(upload_dialog)
        self.bg_widget.setObjectName(u"bg_widget")
        self.verticalLayout_2 = QVBoxLayout(self.bg_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_widget = QWidget(self.bg_widget)
        self.img_widget.setObjectName(u"img_widget")
        self.verticalLayout_3 = QVBoxLayout(self.img_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.img_lbl = QLabel(self.img_widget)
        self.img_lbl.setObjectName(u"img_lbl")
        self.img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.img_lbl)


        self.verticalLayout_2.addWidget(self.img_widget)

        self.form_widget = QWidget(self.bg_widget)
        self.form_widget.setObjectName(u"form_widget")
        self.verticalLayout_4 = QVBoxLayout(self.form_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.error_lbl = QLabel(self.form_widget)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"    background-color: rgba(248, 215, 218, 150); /* light red with 150/255 opacity */\n"
"    color: rgb(196, 62, 57);                              /* dark red text */\n"
"    border: 1px solid rgba(196, 62, 57, 200);  /* optional semi-transparent border */\n"
"    border-radius: 4px;\n"
"    padding: 2px 4px;\n"
"")

        self.verticalLayout_4.addWidget(self.error_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_img_btn = QPushButton(self.form_widget)
        self.select_img_btn.setObjectName(u"select_img_btn")

        self.horizontalLayout.addWidget(self.select_img_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.description_edt = QLineEdit(self.form_widget)
        self.description_edt.setObjectName(u"description_edt")

        self.verticalLayout_4.addWidget(self.description_edt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.upload_btn = QPushButton(self.form_widget)
        self.upload_btn.setObjectName(u"upload_btn")

        self.horizontalLayout_2.addWidget(self.upload_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.form_widget)


        self.verticalLayout.addWidget(self.bg_widget)


        self.retranslateUi(upload_dialog)

        QMetaObject.connectSlotsByName(upload_dialog)
    # setupUi

    def retranslateUi(self, upload_dialog):
        upload_dialog.setWindowTitle(QCoreApplication.translate("upload_dialog", u"Dialog", None))
        self.img_lbl.setText(QCoreApplication.translate("upload_dialog", u"browse an image from your computer", None))
        self.error_lbl.setText(QCoreApplication.translate("upload_dialog", u"text label", None))
        self.select_img_btn.setText(QCoreApplication.translate("upload_dialog", u"select image", None))
        self.description_edt.setPlaceholderText(QCoreApplication.translate("upload_dialog", u"enter a short description!", None))
        self.upload_btn.setText(QCoreApplication.translate("upload_dialog", u"all done!", None))
    # retranslateUi

