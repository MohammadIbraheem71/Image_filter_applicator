# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_magnified_view.ui'
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
import resources_rc

class Ui_img_magnified_view(object):
    def setupUi(self, img_magnified_view):
        if not img_magnified_view.objectName():
            img_magnified_view.setObjectName(u"img_magnified_view")
        img_magnified_view.resize(597, 418)
        img_magnified_view.setStyleSheet(u"/* -----------------------------------------\n"
"   MAGNIFIED IMAGE VIEW PAGE\n"
"----------------------------------------- */\n"
"QWidget#img_magnified_view {\n"
"    background-color: rgba(30, 30, 40, 0.6); /* semi-transparent dark */\n"
"    border-radius: 16px;\n"
"    padding: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   IMAGE WIDGET (left side)\n"
"----------------------------------------- */\n"
"QWidget#img_widget {\n"
"    background-color: rgba(255, 255, 255, 0.12);  /* translucent */\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    padding: 8px;\n"
"  \n"
"}\n"
"\n"
"QWidget#img_widget:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(255, 255, 255, 0.35);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
""
                        "   IMAGE LABEL\n"
"----------------------------------------- */\n"
"QLabel#img_lbl {\n"
"    border-radius: 12px;\n"
"    background-color: rgba(0,0,0,0.1);\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   INFO WIDGET (right side)\n"
"----------------------------------------- */\n"
"QWidget#info_widget {\n"
"    background-color: rgba(255, 255, 255, 0.12);  /* translucent */\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    padding: 12px;\n"
"  \n"
"}\n"
"\n"
"QWidget#info_widget:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(255, 255, 255, 0.35);\n"
"    \n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   INFO LABELS\n"
"----------------------------------------- */\n"
"QLabel {\n"
"    color: #F5F0FF;\n"
"    font-weight: 500;\n"
"    font-size: 14px;\n"
"    padding:"
                        " 2px 0;\n"
"}\n"
"\n"
"/* -----------------------------------------\n"
"   LIKE BUTTON\n"
"----------------------------------------- */\n"
"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"    color: #F5F0FF;\n"
"    border: 1px solid rgba(255, 255, 255, 0.25);\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"   \n"
"    min-height: 36px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(255, 255, 255, 0.4);\n"
" \n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(img_magnified_view)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_widget = QWidget(img_magnified_view)
        self.img_widget.setObjectName(u"img_widget")
        self.verticalLayout = QVBoxLayout(self.img_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_lbl = QLabel(self.img_widget)
        self.image_lbl.setObjectName(u"image_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_lbl.sizePolicy().hasHeightForWidth())
        self.image_lbl.setSizePolicy(sizePolicy)
        self.image_lbl.setScaledContents(False)
        self.image_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.image_lbl)


        self.horizontalLayout.addWidget(self.img_widget)

        self.info_widget = QWidget(img_magnified_view)
        self.info_widget.setObjectName(u"info_widget")
        self.verticalLayout_2 = QVBoxLayout(self.info_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.uploaded_by_lbl = QLabel(self.info_widget)
        self.uploaded_by_lbl.setObjectName(u"uploaded_by_lbl")

        self.verticalLayout_2.addWidget(self.uploaded_by_lbl)

        self.uploaded_at_lbl = QLabel(self.info_widget)
        self.uploaded_at_lbl.setObjectName(u"uploaded_at_lbl")

        self.verticalLayout_2.addWidget(self.uploaded_at_lbl)

        self.description_lbl = QLabel(self.info_widget)
        self.description_lbl.setObjectName(u"description_lbl")

        self.verticalLayout_2.addWidget(self.description_lbl)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.like_counter_lbl = QLabel(self.info_widget)
        self.like_counter_lbl.setObjectName(u"like_counter_lbl")

        self.horizontalLayout_2.addWidget(self.like_counter_lbl)

        self.liked_btn = QPushButton(self.info_widget)
        self.liked_btn.setObjectName(u"liked_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/heartred.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.liked_btn.setIcon(icon)
        self.liked_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.liked_btn)

        self.like_btn = QPushButton(self.info_widget)
        self.like_btn.setObjectName(u"like_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.like_btn.sizePolicy().hasHeightForWidth())
        self.like_btn.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/heart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.like_btn.setIcon(icon1)
        self.like_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.like_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.download_btn = QPushButton(self.info_widget)
        self.download_btn.setObjectName(u"download_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/downloads.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download_btn.setIcon(icon2)
        self.download_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.download_btn)


        self.horizontalLayout.addWidget(self.info_widget)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(img_magnified_view)

        QMetaObject.connectSlotsByName(img_magnified_view)
    # setupUi

    def retranslateUi(self, img_magnified_view):
        img_magnified_view.setWindowTitle(QCoreApplication.translate("img_magnified_view", u"Form", None))
        self.image_lbl.setText(QCoreApplication.translate("img_magnified_view", u"loading image..", None))
        self.uploaded_by_lbl.setText(QCoreApplication.translate("img_magnified_view", u"uploaded by", None))
        self.uploaded_at_lbl.setText(QCoreApplication.translate("img_magnified_view", u"uploaded at", None))
        self.description_lbl.setText(QCoreApplication.translate("img_magnified_view", u"TextLabel", None))
        self.like_counter_lbl.setText(QCoreApplication.translate("img_magnified_view", u"likes", None))
        self.liked_btn.setText("")
        self.like_btn.setText("")
        self.download_btn.setText("")
    # retranslateUi

