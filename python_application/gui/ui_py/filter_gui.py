# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_filter_pg(object):
    def setupUi(self, filter_pg):
        if not filter_pg.objectName():
            filter_pg.setObjectName(u"filter_pg")
        filter_pg.resize(426, 469)
        self.verticalLayout = QVBoxLayout(filter_pg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.og_img_lbl = QLabel(filter_pg)
        self.og_img_lbl.setObjectName(u"og_img_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.og_img_lbl.sizePolicy().hasHeightForWidth())
        self.og_img_lbl.setSizePolicy(sizePolicy)
        self.og_img_lbl.setMinimumSize(QSize(200, 200))
        self.og_img_lbl.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.og_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.og_img_lbl)

        self.new_img_lbl = QLabel(filter_pg)
        self.new_img_lbl.setObjectName(u"new_img_lbl")
        sizePolicy.setHeightForWidth(self.new_img_lbl.sizePolicy().hasHeightForWidth())
        self.new_img_lbl.setSizePolicy(sizePolicy)
        self.new_img_lbl.setMinimumSize(QSize(200, 200))
        self.new_img_lbl.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.new_img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.new_img_lbl)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.upload_btn = QPushButton(filter_pg)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.upload_btn)

        self.filter_cbx = QComboBox(filter_pg)
        self.filter_cbx.setObjectName(u"filter_cbx")

        self.horizontalLayout_3.addWidget(self.filter_cbx)

        self.download_btn = QPushButton(filter_pg)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.download_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(filter_pg)

        QMetaObject.connectSlotsByName(filter_pg)
    # setupUi

    def retranslateUi(self, filter_pg):
        self.og_img_lbl.setText(QCoreApplication.translate("filter_pg", u"original image here", None))
        self.new_img_lbl.setText(QCoreApplication.translate("filter_pg", u"new image here", None))
        self.upload_btn.setText(QCoreApplication.translate("filter_pg", u"upload image", None))
        self.download_btn.setText(QCoreApplication.translate("filter_pg", u"download image", None))
        pass
    # retranslateUi

