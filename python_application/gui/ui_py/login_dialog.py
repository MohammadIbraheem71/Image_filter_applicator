# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log-in_dialog.ui'
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

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        if not login_dialog.objectName():
            login_dialog.setObjectName(u"login_dialog")
        login_dialog.resize(462, 405)
        self.verticalLayout = QVBoxLayout(login_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.email_lbl = QLabel(login_dialog)
        self.email_lbl.setObjectName(u"email_lbl")

        self.horizontalLayout.addWidget(self.email_lbl)

        self.email_edt = QLineEdit(login_dialog)
        self.email_edt.setObjectName(u"email_edt")

        self.horizontalLayout.addWidget(self.email_edt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pswrd_lbl = QLabel(login_dialog)
        self.pswrd_lbl.setObjectName(u"pswrd_lbl")

        self.horizontalLayout_2.addWidget(self.pswrd_lbl)

        self.pswrd_edt = QLineEdit(login_dialog)
        self.pswrd_edt.setObjectName(u"pswrd_edt")

        self.horizontalLayout_2.addWidget(self.pswrd_edt)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(login_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(login_dialog)

        QMetaObject.connectSlotsByName(login_dialog)
    # setupUi

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QCoreApplication.translate("login_dialog", u"Dialog", None))
        self.email_lbl.setText(QCoreApplication.translate("login_dialog", u"email:", None))
        self.pswrd_lbl.setText(QCoreApplication.translate("login_dialog", u"password:", None))
    # retranslateUi

