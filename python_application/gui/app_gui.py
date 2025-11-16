# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        MainWindow.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_preview = QLabel(self.centralwidget)
        self.image_preview.setObjectName(u"image_preview")
        self.image_preview.setMinimumSize(QSize(400, 300))
        font = QFont()
        font.setPointSize(16)
        self.image_preview.setFont(font)
        self.image_preview.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.image_preview.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_preview)

        self.new_image_preview = QLabel(self.centralwidget)
        self.new_image_preview.setObjectName(u"new_image_preview")
        self.new_image_preview.setMinimumSize(QSize(400, 300))
        self.new_image_preview.setFont(font)
        self.new_image_preview.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #666;\n"
"}\n"
"")
        self.new_image_preview.setFrameShape(QFrame.Shape.StyledPanel)
        self.new_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.new_image_preview)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.upload_image = QPushButton(self.centralwidget)
        self.upload_image.setObjectName(u"upload_image")
        self.upload_image.setStyleSheet(u"QPushButton {\n"
"    background-color: #0078ff;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004799;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.upload_image)

        self.apply_filter = QPushButton(self.centralwidget)
        self.apply_filter.setObjectName(u"apply_filter")
        self.apply_filter.setStyleSheet(u"QPushButton {\n"
"    background-color: #0078ff;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004799;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.apply_filter)

        self.download_image = QPushButton(self.centralwidget)
        self.download_image.setObjectName(u"download_image")
        self.download_image.setStyleSheet(u"QPushButton {\n"
"    background-color: #0078ff;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004799;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.download_image)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_preview.setText(QCoreApplication.translate("MainWindow", u"original image appears here", None))
        self.new_image_preview.setText(QCoreApplication.translate("MainWindow", u"new image appears here", None))
        self.upload_image.setText(QCoreApplication.translate("MainWindow", u"upload image", None))
        self.apply_filter.setText(QCoreApplication.translate("MainWindow", u"apply filter", None))
        self.download_image.setText(QCoreApplication.translate("MainWindow", u"download image", None))
    # retranslateUi

