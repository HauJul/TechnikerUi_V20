# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_NewDialog(object):
    def setupUi(self, NewDialog):
        if not NewDialog.objectName():
            NewDialog.setObjectName(u"NewDialog")
        NewDialog.resize(400, 300)
        NewDialog.setStyleSheet(u"")
        self.widget = QWidget(NewDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 401, 301))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 167, 146, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.btnbox = QDialogButtonBox(self.widget)
        self.btnbox.setObjectName(u"btnbox")
        self.btnbox.setGeometry(QRect(50, 260, 341, 32))
        self.btnbox.setOrientation(Qt.Horizontal)
        self.btnbox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lbl_new = QLabel(self.widget)
        self.lbl_new.setObjectName(u"lbl_new")
        self.lbl_new.setGeometry(QRect(20, 70, 331, 121))
        font = QFont()
        font.setPointSize(20)
        self.lbl_new.setFont(font)
        self.lbl_new.setWordWrap(True)
        self.txt_new = QLineEdit(self.widget)
        self.txt_new.setObjectName(u"txt_new")
        self.txt_new.setGeometry(QRect(20, 200, 311, 51))
        self.txt_new.setFont(font)
        self.txt_new.setInputMethodHints(Qt.ImhNone)
        self.txt_new.setMaxLength(8)
        self.txt_new.setEchoMode(QLineEdit.Normal)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 311, 41))
        self.comboBox.setFont(font)

        self.retranslateUi(NewDialog)
        self.btnbox.accepted.connect(NewDialog.accept)
        self.btnbox.rejected.connect(NewDialog.reject)

        QMetaObject.connectSlotsByName(NewDialog)
    # setupUi

    def retranslateUi(self, NewDialog):
        NewDialog.setWindowTitle(QCoreApplication.translate("NewDialog", u"Dialog", None))
        self.lbl_new.setText(QCoreApplication.translate("NewDialog", u"Material-/Program-/Einsatznummer eingeben oder scannen:", None))
        self.txt_new.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("NewDialog", u"Neues Produkt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("NewDialog", u"Neuer Einsatz", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("NewDialog", u"Neues Programm", None))

    # retranslateUi

