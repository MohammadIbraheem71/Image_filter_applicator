# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign-up_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_signup_dialog(object):
    def setupUi(self, signup_dialog):
        if not signup_dialog.objectName():
            signup_dialog.setObjectName(u"signup_dialog")
        signup_dialog.resize(313, 189)
        self.verticalLayout = QVBoxLayout(signup_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.email_lbl = QLabel(signup_dialog)
        self.email_lbl.setObjectName(u"email_lbl")

        self.horizontalLayout.addWidget(self.email_lbl)

        self.email_edt = QLineEdit(signup_dialog)
        self.email_edt.setObjectName(u"email_edt")

        self.horizontalLayout.addWidget(self.email_edt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pswrd_lbl = QLabel(signup_dialog)
        self.pswrd_lbl.setObjectName(u"pswrd_lbl")

        self.horizontalLayout_2.addWidget(self.pswrd_lbl)

        self.pswrd_edt = QLineEdit(signup_dialog)
        self.pswrd_edt.setObjectName(u"pswrd_edt")

        self.horizontalLayout_2.addWidget(self.pswrd_edt)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(signup_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(signup_dialog)
        self.buttonBox.accepted.connect(signup_dialog.accept)
        self.buttonBox.rejected.connect(signup_dialog.reject)

        QMetaObject.connectSlotsByName(signup_dialog)
    # setupUi

    def retranslateUi(self, signup_dialog):
        signup_dialog.setWindowTitle(QCoreApplication.translate("signup_dialog", u"Dialog", None))
        self.email_lbl.setText(QCoreApplication.translate("signup_dialog", u"email:", None))
        self.pswrd_lbl.setText(QCoreApplication.translate("signup_dialog", u"password:", None))
    # retranslateUi

