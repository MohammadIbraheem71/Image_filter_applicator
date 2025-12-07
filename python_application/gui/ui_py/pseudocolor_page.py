# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pseudocolor_page.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_pseudoclr_pg(object):
    def setupUi(self, pseudoclr_pg):
        if not pseudoclr_pg.objectName():
            pseudoclr_pg.setObjectName(u"pseudoclr_pg")
        pseudoclr_pg.resize(426, 447)
        pseudoclr_pg.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(pseudoclr_pg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(pseudoclr_pg)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.old_img_lbl = QLabel(pseudoclr_pg)
        self.old_img_lbl.setObjectName(u"old_img_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.old_img_lbl.sizePolicy().hasHeightForWidth())
        self.old_img_lbl.setSizePolicy(sizePolicy)
        self.old_img_lbl.setMinimumSize(QSize(200, 200))
        self.old_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.old_img_lbl)

        self.new_img_lbl = QLabel(pseudoclr_pg)
        self.new_img_lbl.setObjectName(u"new_img_lbl")
        sizePolicy.setHeightForWidth(self.new_img_lbl.sizePolicy().hasHeightForWidth())
        self.new_img_lbl.setSizePolicy(sizePolicy)
        self.new_img_lbl.setMinimumSize(QSize(200, 200))
        self.new_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.new_img_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upload_btn = QPushButton(pseudoclr_pg)
        self.upload_btn.setObjectName(u"upload_btn")

        self.horizontalLayout_2.addWidget(self.upload_btn)

        self.download_btn = QPushButton(pseudoclr_pg)
        self.download_btn.setObjectName(u"download_btn")

        self.horizontalLayout_2.addWidget(self.download_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(pseudoclr_pg)

        QMetaObject.connectSlotsByName(pseudoclr_pg)
    # setupUi

    def retranslateUi(self, pseudoclr_pg):
        pseudoclr_pg.setWindowTitle(QCoreApplication.translate("pseudoclr_pg", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("pseudoclr_pg", u"Specializes in coloring faces. Experimental feature.", None))
        self.old_img_lbl.setText(QCoreApplication.translate("pseudoclr_pg", u"original image here", None))
        self.new_img_lbl.setText(QCoreApplication.translate("pseudoclr_pg", u"new image here", None))
        self.upload_btn.setText(QCoreApplication.translate("pseudoclr_pg", u"upload image", None))
        self.download_btn.setText(QCoreApplication.translate("pseudoclr_pg", u"download image", None))
    # retranslateUi

