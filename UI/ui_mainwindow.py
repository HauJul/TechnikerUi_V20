# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 549)
        font = QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 167, 146, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(100, 100))
        self.btn_settings.setMaximumSize(QSize(100, 16777215))
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(85, 85, 85);\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"Qss/icons/original_svg/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(70, 70))
        self.btn_settings.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_settings)

        self.btn_skip = QPushButton(self.centralwidget)
        self.btn_skip.setObjectName(u"btn_skip")
        self.btn_skip.setMinimumSize(QSize(100, 100))
        self.btn_skip.setMaximumSize(QSize(100, 16777215))
        self.btn_skip.setFont(font)
        self.btn_skip.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(85, 85, 85);")
        icon1 = QIcon()
        icon1.addFile(u"Qss/icons/original_svg/arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_skip.setIcon(icon1)
        self.btn_skip.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.btn_skip)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(100, 100))
        self.btn_exit.setMaximumSize(QSize(100, 16777215))
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(85, 85, 85);")
        icon2 = QIcon()
        icon2.addFile(u"Qss/icons/original_svg/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon2)
        self.btn_exit.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.btn_exit)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbl_artno = QLabel(self.centralwidget)
        self.lbl_artno.setObjectName(u"lbl_artno")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setUnderline(True)
        self.lbl_artno.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_artno)

        self.sb_artno = QSpinBox(self.centralwidget)
        self.sb_artno.setObjectName(u"sb_artno")
        font2 = QFont()
        font2.setPointSize(20)
        self.sb_artno.setFont(font2)
        self.sb_artno.setMinimum(10000000)
        self.sb_artno.setMaximum(99999999)

        self.verticalLayout.addWidget(self.sb_artno)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_tool = QLabel(self.centralwidget)
        self.lbl_tool.setObjectName(u"lbl_tool")
        self.lbl_tool.setFont(font2)

        self.gridLayout_2.addWidget(self.lbl_tool, 2, 0, 1, 1)

        self.txt_process = QLabel(self.centralwidget)
        self.txt_process.setObjectName(u"txt_process")
        self.txt_process.setFont(font2)

        self.gridLayout_2.addWidget(self.txt_process, 1, 1, 1, 1)

        self.txt_name = QLabel(self.centralwidget)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setFont(font2)

        self.gridLayout_2.addWidget(self.txt_name, 0, 1, 1, 1)

        self.txt_tool = QLabel(self.centralwidget)
        self.txt_tool.setObjectName(u"txt_tool")
        self.txt_tool.setFont(font2)

        self.gridLayout_2.addWidget(self.txt_tool, 2, 1, 1, 1)

        self.lbl_process = QLabel(self.centralwidget)
        self.lbl_process.setObjectName(u"lbl_process")
        self.lbl_process.setFont(font2)

        self.gridLayout_2.addWidget(self.lbl_process, 1, 0, 1, 1)

        self.lbl_name = QLabel(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.lbl_name.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl_name, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_process_state = QLabel(self.centralwidget)
        self.lbl_process_state.setObjectName(u"lbl_process_state")
        self.lbl_process_state.setFont(font2)

        self.verticalLayout.addWidget(self.lbl_process_state)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lbl_cvir_state = QLabel(self.centralwidget)
        self.lbl_cvir_state.setObjectName(u"lbl_cvir_state")
        self.lbl_cvir_state.setFont(font2)

        self.verticalLayout.addWidget(self.lbl_cvir_state)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Schraubersteuerung", None))
        self.btn_settings.setText("")
        self.btn_skip.setText("")
        self.btn_exit.setText("")
        self.lbl_artno.setText(QCoreApplication.translate("MainWindow", u"Materialnummer:", None))
        self.lbl_tool.setText(QCoreApplication.translate("MainWindow", u"Bit Einsatz:", None))
        self.txt_process.setText(QCoreApplication.translate("MainWindow", u"0 von 0", None))
        self.txt_name.setText(QCoreApplication.translate("MainWindow", u"Produkt X", None))
        self.txt_tool.setText(QCoreApplication.translate("MainWindow", u"Bit X", None))
        self.lbl_process.setText(QCoreApplication.translate("MainWindow", u"Schraubvorgang:", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Bezeichnung:", None))
        self.lbl_process_state.setText(QCoreApplication.translate("MainWindow", u"Einsatz wechseln!", None))
        self.lbl_cvir_state.setText(QCoreApplication.translate("MainWindow", u"In Ordnung", None))
    # retranslateUi

