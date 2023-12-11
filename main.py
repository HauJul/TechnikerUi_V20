# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QDialogButtonBox, QTableWidgetItem
from PySide6.QtCore import Qt

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
        password_dialog.exec()

    def false_tool(self):
        self.ui.lbl_process_state.setText("Einsatz wechseln!")
        cvir.lock_start()

    def right_tool(self):
        self.ui.lbl_process_state.setText("Schrauben starten!")
        cvir.release_start()


class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)
        self.read_all()
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save_all)
        self.ui.btn_delete.clicked.connect(self.delete_row)
        self.ui.btn_new.clicked.connect(self.new_item)

    def new_item(self):
        new_dialog = NewDialog()
        new_dialog.exec()

    def read_csv_file(self, filepath, table):
        file = open(filepath, 'r')
        df = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()
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
    def read_all(self):
        self.read_csv_file("Lists/Produktliste_V03.csv", self.ui.tbl_prod)
        self.read_csv_file("Lists/Toolliste_V03.csv", self.ui.tbl_tool)
        self.read_csv_file("Lists/Programmliste_V03.csv", self.ui.tbl_prog)

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
        product.read_csv()

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
            setting_window.read_all()
            setting_window.show()
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
        new_item = QTableWidgetItem()
        new_item.setText(self.ui.txt_new.text())
        match self.ui.comboBox.currentText():
            case "Neues Produkt":
                setting_window.ui.tbl_prod.insertRow(setting_window.ui.tbl_prod.rowCount())
                setting_window.ui.tbl_prod.setVerticalHeaderItem(setting_window.ui.tbl_prod.rowCount()-1, new_item)
            case "Neuer Einsatz":
                setting_window.ui.tbl_tool.insertRow(setting_window.ui.tbl_tool.rowCount())
                setting_window.ui.tbl_tool.setVerticalHeaderItem(setting_window.ui.tbl_tool.rowCount()-1, new_item)
            case "Neues Programm":
                setting_window.ui.tbl_prog.insertRow(setting_window.ui.tbl_prog.rowCount())
                setting_window.ui.tbl_prog.setVerticalHeaderItem(setting_window.ui.tbl_prog.rowCount()-1, new_item)


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


def io_activated():
    if cvir.__outIO.value:
        window.ui.lbl_cvir_state.setText("In Ordnung")
        next_step()
    elif cvir.__outNIO.value:
        window.ui.lbl_cvir_state.setText("Nicht in Ordnung")
    elif cvir.__outZLAEUF.value:
        window.ui.lbl_cvir_state.setText("")
        window.ui.lbl_process_state.setText("Schrauber läuft!")


def next_step():
    if cvir.step < product.get_steps():
        cvir.step = cvir.step + 1
    else:
        cvir.step = 1
    update_process(cvir.step)


# Start Application
app = QApplication(sys.argv)
# Start MainWindow
window = MainWindow()
window.show()
setting_window = SettingWindow()
# Interupt
# Toolbox - Tool changed
toolbox.outBit0.when_activated = check_tool
toolbox.outBit1.when_activated = check_tool
toolbox.outBit2.when_activated = check_tool
# CVIR - Statusmeldung
cvir.__outIO.when_activated = io_activated
cvir.__outNIO.when_activated = io_activated
cvir.__outZLAEUF.when_activated = io_activated
# Bedienelement
cvir.__outSF1.when_activated = cvir.button_press
cvir.__outSF1.when_deactivated = cvir.button_release
cvir.__outSF2.when_activated = cvir.button_press
cvir.__outSF2.when_deactivated = cvir.button_release

sys.exit(app.exec())
