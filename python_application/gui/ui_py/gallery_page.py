# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gallery_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_gallery_pg(object):
    def setupUi(self, gallery_pg):
        if not gallery_pg.objectName():
            gallery_pg.setObjectName(u"gallery_pg")
        gallery_pg.resize(423, 315)
        self.verticalLayout_3 = QVBoxLayout(gallery_pg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.upld_glry_btn = QPushButton(gallery_pg)
        self.upld_glry_btn.setObjectName(u"upld_glry_btn")
        icon = QIcon()
        icon.addFile(u":/icons/assets/upload_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.upld_glry_btn.setIcon(icon)
        self.upld_glry_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.upld_glry_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(gallery_pg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 403, 249))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(gallery_pg)

        QMetaObject.connectSlotsByName(gallery_pg)
    # setupUi

    def retranslateUi(self, gallery_pg):
        self.upld_glry_btn.setText(QCoreApplication.translate("gallery_pg", u"upload", None))
        pass
    # retranslateUi

