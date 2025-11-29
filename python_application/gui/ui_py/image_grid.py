# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_grid.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QScrollArea,
    QSizePolicy, QWidget)

class Ui_image_gallery_grid(object):
    def setupUi(self, image_gallery_grid):
        if not image_gallery_grid.objectName():
            image_gallery_grid.setObjectName(u"image_gallery_grid")
        image_gallery_grid.resize(567, 399)
        image_gallery_grid.setStyleSheet(u"QWidget#image_gallery_grid {\n"
"    background-color: rgba(20, 20, 20, 0.7);  /* dark translucent background */\n"
"    border-radius: 15px;                      /* rounded corners */\n"
"    padding: 10px;                             /* inner padding for layout */\n"
"\n"
"    /* Optional subtle border for glass effect */\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"\n"
"    /* Optional shadow effect (works if using QGraphicsDropShadowEffect) */\n"
"    /* box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); */\n"
"}\n"
"\n"
"QScrollArea#gallery_scroll_area {\n"
"    background-color: rgba(20, 20, 20, 0.5); /* semi-transparent dark */\n"
"    border: 20px;                             /* remove default frame */\n"
"    border-radius: 35px;                      /* match grid corners */\n"
"}")
        self.gridLayout = QGridLayout(image_gallery_grid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gallery_scroll_area = QScrollArea(image_gallery_grid)
        self.gallery_scroll_area.setObjectName(u"gallery_scroll_area")
        self.gallery_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gallery_scroll_area.setWidgetResizable(True)
        self.grid_container = QWidget()
        self.grid_container.setObjectName(u"grid_container")
        self.grid_container.setGeometry(QRect(0, 0, 549, 381))
        self.horizontalLayout_2 = QHBoxLayout(self.grid_container)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gallery_scroll_area.setWidget(self.grid_container)

        self.gridLayout.addWidget(self.gallery_scroll_area, 0, 0, 1, 1)


        self.retranslateUi(image_gallery_grid)

        QMetaObject.connectSlotsByName(image_gallery_grid)
    # setupUi

    def retranslateUi(self, image_gallery_grid):
        image_gallery_grid.setWindowTitle(QCoreApplication.translate("image_gallery_grid", u"Form", None))
    # retranslateUi

