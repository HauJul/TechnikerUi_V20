# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_PasswordDialog(object):
    def setupUi(self, PasswordDialog):
        if not PasswordDialog.objectName():
            PasswordDialog.setObjectName(u"PasswordDialog")
        PasswordDialog.resize(487, 300)
        PasswordDialog.setStyleSheet(u"")
        self.widget = QWidget(PasswordDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 491, 301))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 167, 146, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(130, 260, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lbl_password = QLabel(self.widget)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setGeometry(QRect(20, 60, 441, 61))
        font = QFont()
        font.setPointSize(20)
        self.lbl_password.setFont(font)
        self.txt_password = QLineEdit(self.widget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(20, 120, 441, 51))
        self.txt_password.setFont(font)
        self.txt_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.retranslateUi(PasswordDialog)
        self.buttonBox.rejected.connect(PasswordDialog.reject)
        self.buttonBox.accepted.connect(PasswordDialog.accept)

        QMetaObject.connectSlotsByName(PasswordDialog)
    # setupUi

    def retranslateUi(self, PasswordDialog):
        PasswordDialog.setWindowTitle(QCoreApplication.translate("PasswordDialog", u"Dialog", None))
        self.lbl_password.setText(QCoreApplication.translate("PasswordDialog", u"Servicepasswort eingeben:", None))
        self.txt_password.setText("")
    # retranslateUi

