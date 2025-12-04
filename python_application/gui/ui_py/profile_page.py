# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QStackedWidget,
    QWidget)
import resources_rc

class Ui_profile_pg(object):
    def setupUi(self, profile_pg):
        if not profile_pg.objectName():
            profile_pg.setObjectName(u"profile_pg")
        profile_pg.resize(541, 467)
        self.horizontalLayout_5 = QHBoxLayout(profile_pg)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profile_windows = QStackedWidget(profile_pg)
        self.profile_windows.setObjectName(u"profile_windows")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.profile_windows.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.profile_windows.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.profile_windows)


        self.retranslateUi(profile_pg)

        QMetaObject.connectSlotsByName(profile_pg)
    # setupUi

    def retranslateUi(self, profile_pg):
        pass
    # retranslateUi

