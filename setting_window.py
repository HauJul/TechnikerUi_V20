import pandas as pd
from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem

from UI.ui_settingwindow import Ui_SettingWindow
from UI.ui_newdialog import Ui_NewDialog


# Read Product, Tool and Programm values and show in Tablewidgets
def read_csv_file(filepath, table):
    # Read file and create DataFrame
    file = open(filepath, 'r')
    df = pd.read_csv(file, delimiter=";", index_col=0)
    file.close()
    # Set table size
    table.setRowCount(df.shape[0])
    table.setColumnCount(df.shape[1])
    # Set table headers
    headers = list(df)
    table.setHorizontalHeaderLabels(headers)
    # Set index values
    index = df.index.tolist()
    table.setVerticalHeaderLabels(map(str, index))
    # Set table values
    df_array = df.values
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            table.setItem(row, col, QTableWidgetItem(str(df_array[row, col])))


# Save actual table values in file when button 'save' is pressed
def save_csv_file(filepath, table):
    headers = []
    index = []

    for i in range(table.model().columnCount()):
        headers.append(table.horizontalHeaderItem(i).text())
    for j in range(table.model().rowCount()):
        index.append(table.verticalHeaderItem(j).text())
    # Create DataFrame with Headers and Indexes
    df = pd.DataFrame(columns=headers, index=index)
    # Save values in DataFrame
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            # If value is a number save as integer
            try:
                df.at[index[row], headers[col]] = int(table.item(row, col).text())
            # If value is a  text save as string
            except ValueError:
                df.at[index[row], headers[col]] = table.item(row, col).text()
            # If no value safe empty string
            except AttributeError:
                df.at[index[row], headers[col]] = 0
    # Save DataFrame in CSV file
    df.to_csv(filepath, sep=";")


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

    # Create new Product, Tool or Programm
    def create_new_item(self):
        new_item_values = {"table": "", "number": ""}
        new_item = QTableWidgetItem()
        # Open Dialog to selecet table and set index
        new_dialog = NewDialog(new_item_values)
        new_dialog.exec()
        # Create new tablerow depending on Dialog values
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

    # Read all csv files to tables
    def read_all(self):
        read_csv_file("Lists/Produktliste.csv", self.ui.tbl_prod)
        read_csv_file("Lists/Toolliste.csv", self.ui.tbl_tool)
        read_csv_file("Lists/Programmliste.csv", self.ui.tbl_prog)

    # Save all tables to csv files and update product values
    def save_all(self):
        save_csv_file("Lists/Produktliste.csv", self.ui.tbl_prod)
        save_csv_file("Lists/Toolliste.csv", self.ui.tbl_tool)
        save_csv_file("Lists/Programmliste.csv", self.ui.tbl_prog)
        self.product.read_csv()

    # Delete selected row TODO?
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





class NewDialog(QDialog):
    def __init__(self, new_item_values):
        super().__init__()
        self.ui = Ui_NewDialog()
        self.ui.setupUi(self)

        self.new_item_values = new_item_values

        self.ui.btnbox.accepted.connect(self.handle_new)

    # Set table and index for new table
    def handle_new(self):
        self.new_item_values["number"] = self.ui.txt_new.text()
        self.new_item_values["table"] = self.ui.comboBox.currentText()
