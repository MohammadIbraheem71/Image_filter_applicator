# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_image_widget(object):
    def setupUi(self, image_widget):
        if not image_widget.objectName():
            image_widget.setObjectName(u"image_widget")
        image_widget.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(image_widget.sizePolicy().hasHeightForWidth())
        image_widget.setSizePolicy(sizePolicy)
        image_widget.setMinimumSize(QSize(300, 200))
        image_widget.setMaximumSize(QSize(300, 200))
        image_widget.setStyleSheet(u"QWidget#sub_widget {\n"
"    border-radius: 12px;                          /* Rounded corners like sidebar */\n"
"    background-color: rgba(255, 255, 255, 0.08); /* Very translucent dark */\n"
"    border: 1px solid rgba(200, 160, 220, 0.3);  /* Subtle glass border */\n"
"    padding: 5px;                                 /* Inner padding */\n"
"}\n"
"\n"
"/* Optional: add hover effect */\n"
"QWidget#sub_widget:hover {\n"
"    background-color: rgba(220, 180, 240, 0.15); /* Slight highlight on hover */\n"
"    border: 1px solid rgba(230, 190, 250, 0.4);\n"
"    /*box-shadow: 0 0 12px rgba(200, 150, 230, 0.3);*/\n"
"}\n"
"\n"
"\n"
"QWidget#sub_widget QLabel#img_lbl {\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"    background-color: #f5f5f5;\n"
"    /* Force the label to clip its contents to the border radius */\n"
"    border: none;\n"
"	color: #666;\n"
"}\n"
"\n"
"QWidget#sub_widget QWidget#img_inf"
                        "o {\n"
"    background-color: #fafafa;\n"
"    border-top: 1px solid #eee;\n"
"    border-radius: 0 0 12px 12px;\n"
"}")
        self.verticalLayout = QVBoxLayout(image_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sub_widget = QWidget(image_widget)
        self.sub_widget.setObjectName(u"sub_widget")
        self.verticalLayout_2 = QVBoxLayout(self.sub_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_lbl = QLabel(self.sub_widget)
        self.img_lbl.setObjectName(u"img_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img_lbl.sizePolicy().hasHeightForWidth())
        self.img_lbl.setSizePolicy(sizePolicy1)
        self.img_lbl.setMinimumSize(QSize(263, 120))
        self.img_lbl.setMaximumSize(QSize(263, 120))
        self.img_lbl.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.img_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.magnify_btn = QPushButton(self.sub_widget)
        self.magnify_btn.setObjectName(u"magnify_btn")
        sizePolicy1.setHeightForWidth(self.magnify_btn.sizePolicy().hasHeightForWidth())
        self.magnify_btn.setSizePolicy(sizePolicy1)
        self.magnify_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    font-size: 22px;          /* normal size */\n"
"    color: #888;              /* grey color */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/magnify.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.magnify_btn.setIcon(icon)
        self.magnify_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.magnify_btn)

        self.like_btn = QPushButton(self.sub_widget)
        self.like_btn.setObjectName(u"like_btn")
        sizePolicy1.setHeightForWidth(self.like_btn.sizePolicy().hasHeightForWidth())
        self.like_btn.setSizePolicy(sizePolicy1)
        self.like_btn.setMinimumSize(QSize(0, 0))
        self.like_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    font-size: 22px;          /* normal size */\n"
"    color: #888;              /* grey color */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/heart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.like_btn.setIcon(icon1)
        self.like_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.like_btn)

        self.liked_btn = QPushButton(self.sub_widget)
        self.liked_btn.setObjectName(u"liked_btn")
        sizePolicy1.setHeightForWidth(self.liked_btn.sizePolicy().hasHeightForWidth())
        self.liked_btn.setSizePolicy(sizePolicy1)
        self.liked_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    font-size: 22px;          /* normal size */\n"
"    color: #888;              /* grey color */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/heartred.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.liked_btn.setIcon(icon2)
        self.liked_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.liked_btn)

        self.like_count = QLabel(self.sub_widget)
        self.like_count.setObjectName(u"like_count")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.like_count.sizePolicy().hasHeightForWidth())
        self.like_count.setSizePolicy(sizePolicy2)
        self.like_count.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.like_count)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 3)

        self.verticalLayout.addWidget(self.sub_widget)


        self.retranslateUi(image_widget)

        QMetaObject.connectSlotsByName(image_widget)
    # setupUi

    def retranslateUi(self, image_widget):
        image_widget.setWindowTitle(QCoreApplication.translate("image_widget", u"Form", None))
        self.img_lbl.setText(QCoreApplication.translate("image_widget", u"loading image", None))
        self.magnify_btn.setText("")
        self.like_btn.setText("")
        self.liked_btn.setText("")
        self.like_count.setText(QCoreApplication.translate("image_widget", u"0", None))
    # retranslateUi

