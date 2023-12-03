# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QDialogButtonBox, QTableWidgetItem

from UI.ui_mainwindow import Ui_MainWindow
from UI.ui_settingwindow import Ui_SettingWindow
from UI.ui_pwdialog import Ui_PasswordDialog
from UI.ui_newdialog import Ui_NewDialog

import cvir
from toolbox import Toolbox
from product import Product

toolbox = Toolbox()
product = Product()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sb_artno.valueChanged.connect(self.product_change)
        self.ui.btn_skip.clicked.connect(next_step)
        self.ui.btn_exit.clicked.connect(self.product_change)
        self.ui.btn_settings.clicked.connect(self.open_settings)

    def product_change(self):
        if product.select_product(self.ui.sb_artno.value()):
            self.ui.txt_name.setText(product.get_name())
            cvir.step = 1
            update_process(cvir.step)
        else:
            self.ui.txt_name.setText("Produkt nicht bekannt")
            self.ui.txt_tool.setText("")
            self.ui.txt_process.setText("")

    def open_settings(self):
        password_dialog = PasswordDialog()
        if password_dialog.exec() == QDialog.accepted:
            setting_window = SettingWindow()
            setting_window.show()

    def false_tool(self):
        self.ui.lbl_false_tool.show()
        cvir.lock_start()

    def right_tool(self):
        self.ui.lbl_false_tool.hide()
        cvir.release_start()


class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(WindowCloseButtonHint)
        self.read_csv_file("Lists/Produktliste_V03.csv", self.ui.tbl_prod)
        self.read_csv_file("Lists/Toolliste_V03.csv", self.ui.tbl_tool)
        self.read_csv_file("Lists/Programmliste_V03.csv", self.ui.tbl_prog)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save_all)
        self.ui.btn_delete.clicked.connect(self.delete_row)
        self.ui.btn_new_prod.clicked.connect(self.new_item)
        self.ui.btn_new_tool.clicked.connect(self.new_item)
        self.ui.btn_new_prog.clicked.connect(self.new_item)

    def new_item(self):
        new_dialog = NewDialog()
        new_item = QTableWidgetItem()
        if new_dialog.exec() == QDialog.accepted:
            new_item.setText("1")
            self.ui.tbl_prog.insertRow(0)
            self.ui.tbl_prog.setVerticalHeaderItem(0, new_item)
            print("Hallo")
        else:
            print("Nicht Hallo")

    def read_csv_file(self, filepath, table):
        df = pd.read_csv(filepath, delimiter=";", index_col=0)
        headers = list(df)
        index = df.index.tolist()
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(headers)
        table.setVerticalHeaderLabels(map(str, index))

        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, QTableWidgetItem(str(df_array[row, col])))

    def save_csv_file(self, filepath, table):
        headers = []
        index = []

        for i in range(table.model().columnCount()):
            headers.append(table.horizontalHeaderItem(i).text())
        for j in range(table.model().rowCount()):
            index.append(table.verticalHeaderItem(j).text())

        df = pd.DataFrame(columns=headers, index=index)

        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                df.at[index[row], headers[col]] = table.item(row, col).text()

        df.to_csv(filepath, sep=";")

    def save_all(self):
        self.save_csv_file("Lists/Produktliste_V03.csv", self.ui.tbl_prod)
        self.save_csv_file("Lists/Toolliste_V03.csv", self.ui.tbl_tool)
        self.save_csv_file("Lists/Programmliste_V03.csv", self.ui.tbl_prog)

    def delete_row(self):
        index = self.ui.tbl_prod.selectionModel().selectedIndexes()
        if not len(index) == 0:
            self.ui.tbl_prod.removeRow(index[0].row())
        index = self.ui.tbl_tool.selectionModel().selectedIndexes()
        if not len(index) == 0:
            self.ui.tbl_tool.removeRow(index[0].row())
        index = self.ui.tbl_prog.selectionModel().selectedIndexes()
        if not len(index) == 0:
            self.ui.tbl_prog.removeRow(index[0].row())


class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PasswordDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handleLogin)

    def handleLogin(self):
        if self.ui.txt_password.text() == '1000':
            setting_window.show()
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Falsches Servicepassword')


class NewDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewDialog()
        self.ui.setupUi(self)
        self.ui.btnbox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_new)

    def handle_new(self):
        self.accept()

def check_tool():
    if toolbox.get_tool() != product.get_toolno(cvir.step):
        window.false_tool()
        return 1
    else:
        window.right_tool()
        return 0


def update_process(step):
    window.ui.txt_process.setText(str(step) + " von " + str(product.get_steps()))
    cyc = product.get_cyc(step)
    cvir.set_cyc(cyc)
    tool = product.get_toolname(step)
    window.ui.txt_tool.setText(str(tool))
    check_tool()


def next_step():
    window.ui.lbl_io.show()
    if cvir.step < product.get_steps():
        cvir.step = cvir.step + 1
    else:
        cvir.step = 1
    update_process(cvir.step)

#Start Application
app = QApplication(sys.argv)
#Start MainWindoww
window = MainWindow()
window.show()
setting_window = SettingWindow()
#Interupts
#Toolbox - Tool changed
toolbox.outBit0.when_activated = check_tool
toolbox.outBit1.when_activated = check_tool
toolbox.outBit2.when_activated = check_tool
#CVIR - Statusmeldung
cvir.__outIO.when_activated = next_step
cvir.__outIO.when_deactivated = window.ui.lbl_io.hide
cvir.__outNIO.when_activated = window.ui.lbl_nio.show
cvir.__outNIO.when_deactivated = window.ui.lbl_nio.hide
#Bedienelement
cvir.__outSF1.when_activated = cvir.button_press
cvir.__outSF1.when_deactivated = cvir.button_press
cvir.__outSF2.when_activated = cvir.button_release
cvir.__outSF2.when_deactivated = cvir.button_release

sys.exit(app.exec())
