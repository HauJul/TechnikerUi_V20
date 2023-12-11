import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QDialogButtonBox, QTableWidgetItem

from UI.ui_settingwindow import Ui_SettingWindow
from UI.ui_pwdialog import Ui_PasswordDialog
from UI.ui_newdialog import Ui_NewDialog


class SettingWindow(QMainWindow):
    def __init__(self, product):
        super().__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)

        self.product = product

        self.read_all()
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save_all)
        self.ui.btn_delete.clicked.connect(self.delete_row)
        self.ui.btn_new.clicked.connect(self.create_new_item)

    def create_new_item(self):
        new_item_values = {"table": "", "number": ""}
        new_item = QTableWidgetItem()

        new_dialog = NewDialog(new_item_values)
        new_dialog.exec()

        new_item.setText(new_item_values["number"])

        match new_item_values["table"]:
            case "Neues Produkt":
                self.ui.tbl_prod.insertRow(self.ui.tbl_prod.rowCount())
                self.ui.tbl_prod.setVerticalHeaderItem(self.ui.tbl_prod.rowCount() - 1, new_item)
            case "Neuer Einsatz":
                self.ui.tbl_tool.insertRow(self.ui.tbl_tool.rowCount())
                self.ui.tbl_tool.setVerticalHeaderItem(self.ui.tbl_tool.rowCount() - 1, new_item)
            case "Neues Programm":
                self.ui.tbl_prog.insertRow(self.ui.tbl_prog.rowCount())
                self.ui.tbl_prog.setVerticalHeaderItem(self.ui.tbl_prog.rowCount() - 1, new_item)

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
                try:
                    df.at[index[row], headers[col]] = table.item(row, col).text()
                except:
                    df.at[index[row], headers[col]] = ""

        df.to_csv(filepath, sep=";")

    def save_all(self):
        self.save_csv_file("Lists/Produktliste_V03.csv", self.ui.tbl_prod)
        self.save_csv_file("Lists/Toolliste_V03.csv", self.ui.tbl_tool)
        self.save_csv_file("Lists/Programmliste_V03.csv", self.ui.tbl_prog)
        self.product.read_csv()

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
    def __init__(self, setting_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_PasswordDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_login)
        self.setting_window = setting_window

    def handle_login(self):
        if self.ui.txt_password.text() == '1000':
            self.setting_window.read_all()
            self.setting_window.show()
        else:
            QMessageBox.warning(
                self, 'Error', 'Falsches Servicepassword')


class NewDialog(QDialog):
    def __init__(self, new_item_values, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewDialog()
        self.ui.setupUi(self)

        self.new_item_values = new_item_values

        self.ui.btnbox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_new)

    def handle_new(self):
        self.new_item_values["number"] = self.ui.txt_new.text()
        self.new_item_values["table"] = self.ui.comboBox.currentText()
