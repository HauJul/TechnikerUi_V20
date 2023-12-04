# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(800, 480)
        self.centralwidget = QWidget(SettingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 167, 146, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.tbl_prod = QTableWidget(self.centralwidget)
        if (self.tbl_prod.columnCount() < 18):
            self.tbl_prod.setColumnCount(18)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_prod.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        if (self.tbl_prod.rowCount() < 1):
            self.tbl_prod.setRowCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_prod.setVerticalHeaderItem(0, __qtablewidgetitem18)
        self.tbl_prod.setObjectName(u"tbl_prod")
        self.tbl_prod.setGeometry(QRect(10, 10, 780, 211))
        self.tbl_prod.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_prod.horizontalHeader().setMinimumSectionSize(20)
        self.tbl_prod.verticalHeader().setVisible(True)
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(590, 450, 91, 24))
        self.tbl_tool = QTableWidget(self.centralwidget)
        if (self.tbl_tool.columnCount() < 1):
            self.tbl_tool.setColumnCount(1)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbl_tool.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        if (self.tbl_tool.rowCount() < 1):
            self.tbl_tool.setRowCount(1)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbl_tool.setVerticalHeaderItem(0, __qtablewidgetitem20)
        self.tbl_tool.setObjectName(u"tbl_tool")
        self.tbl_tool.setGeometry(QRect(10, 230, 381, 201))
        self.tbl_tool.horizontalHeader().setStretchLastSection(False)
        self.tbl_tool.verticalHeader().setVisible(True)
        self.tbl_tool.verticalHeader().setStretchLastSection(False)
        self.tbl_prog = QTableWidget(self.centralwidget)
        if (self.tbl_prog.columnCount() < 1):
            self.tbl_prog.setColumnCount(1)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbl_prog.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        if (self.tbl_prog.rowCount() < 1):
            self.tbl_prog.setRowCount(1)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbl_prog.setVerticalHeaderItem(0, __qtablewidgetitem22)
        self.tbl_prog.setObjectName(u"tbl_prog")
        self.tbl_prog.setGeometry(QRect(400, 230, 391, 201))
        self.tbl_prog.horizontalHeader().setStretchLastSection(True)
        self.tbl_prog.verticalHeader().setVisible(True)
        self.btn_new = QPushButton(self.centralwidget)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setGeometry(QRect(240, 450, 161, 24))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(420, 450, 151, 24))
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(700, 450, 91, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 430, 781, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        SettingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingWindow)

        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tbl_prod.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SettingWindow", u"Bezeichnung", None));
        ___qtablewidgetitem1 = self.tbl_prod.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SettingWindow", u"Anzahl Schritte", None));
        ___qtablewidgetitem2 = self.tbl_prod.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SettingWindow", u"S1_Prog", None));
        ___qtablewidgetitem3 = self.tbl_prod.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SettingWindow", u"S1_Tool", None));
        ___qtablewidgetitem4 = self.tbl_prod.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SettingWindow", u"S2_Prog", None));
        ___qtablewidgetitem5 = self.tbl_prod.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SettingWindow", u"S2_Tool", None));
        ___qtablewidgetitem6 = self.tbl_prod.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SettingWindow", u"S3_Prog", None));
        ___qtablewidgetitem7 = self.tbl_prod.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SettingWindow", u"S3_Tool", None));
        ___qtablewidgetitem8 = self.tbl_prod.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SettingWindow", u"S4_Prog", None));
        ___qtablewidgetitem9 = self.tbl_prod.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("SettingWindow", u"S4_Tool", None));
        ___qtablewidgetitem10 = self.tbl_prod.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("SettingWindow", u"S5_Prog", None));
        ___qtablewidgetitem11 = self.tbl_prod.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("SettingWindow", u"S5_Tool", None));
        ___qtablewidgetitem12 = self.tbl_prod.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("SettingWindow", u"S6_Prog", None));
        ___qtablewidgetitem13 = self.tbl_prod.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("SettingWindow", u"S6_Tool", None));
        ___qtablewidgetitem14 = self.tbl_prod.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("SettingWindow", u"S7_Prog", None));
        ___qtablewidgetitem15 = self.tbl_prod.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("SettingWindow", u"S7_Tool", None));
        ___qtablewidgetitem16 = self.tbl_prod.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("SettingWindow", u"S8_Prog", None));
        ___qtablewidgetitem17 = self.tbl_prod.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("SettingWindow", u"S8_Tool", None));
        ___qtablewidgetitem18 = self.tbl_prod.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("SettingWindow", u"Neue Zeile", None));
        self.btn_save.setText(QCoreApplication.translate("SettingWindow", u"Speichern", None))
        ___qtablewidgetitem19 = self.tbl_tool.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("SettingWindow", u"Bezeichnung", None));
        ___qtablewidgetitem20 = self.tbl_tool.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("SettingWindow", u"Neue Zeile", None));
        ___qtablewidgetitem21 = self.tbl_prog.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("SettingWindow", u"Bezeichnung", None));
        ___qtablewidgetitem22 = self.tbl_prog.verticalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("SettingWindow", u"Neue Zeile", None));
        self.btn_new.setText(QCoreApplication.translate("SettingWindow", u"Neue Zeile hinzuf\u00fcgen", None))
        self.btn_delete.setText(QCoreApplication.translate("SettingWindow", u"Markierte Zeile l\u00f6schen", None))
        self.btn_close.setText(QCoreApplication.translate("SettingWindow", u"Schlie\u00dfen", None))
    # retranslateUi

