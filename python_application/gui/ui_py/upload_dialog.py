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
        upload_dialog.resize(491, 443)
        self.verticalLayout = QVBoxLayout(upload_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.preview_lbl = QLabel(upload_dialog)
        self.preview_lbl.setObjectName(u"preview_lbl")
        self.preview_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.preview_lbl)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.choose_img_btn = QPushButton(upload_dialog)
        self.choose_img_btn.setObjectName(u"choose_img_btn")

        self.horizontalLayout.addWidget(self.choose_img_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.description_lbl = QLabel(upload_dialog)
        self.description_lbl.setObjectName(u"description_lbl")

        self.horizontalLayout.addWidget(self.description_lbl)

        self.description_edt = QLineEdit(upload_dialog)
        self.description_edt.setObjectName(u"description_edt")

        self.horizontalLayout.addWidget(self.description_edt)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upload_btn = QPushButton(upload_dialog)
        self.upload_btn.setObjectName(u"upload_btn")

        self.horizontalLayout_2.addWidget(self.upload_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cancel_btn = QPushButton(upload_dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(upload_dialog)

        QMetaObject.connectSlotsByName(upload_dialog)
    # setupUi

    def retranslateUi(self, upload_dialog):
        upload_dialog.setWindowTitle(QCoreApplication.translate("upload_dialog", u"Dialog", None))
        self.preview_lbl.setText(QCoreApplication.translate("upload_dialog", u"no file selected", None))
        self.choose_img_btn.setText(QCoreApplication.translate("upload_dialog", u"choose image", None))
        self.description_lbl.setText(QCoreApplication.translate("upload_dialog", u"description:", None))
        self.upload_btn.setText(QCoreApplication.translate("upload_dialog", u"upload", None))
        self.cancel_btn.setText(QCoreApplication.translate("upload_dialog", u"cancel", None))
    # retranslateUi

