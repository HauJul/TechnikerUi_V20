# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from UI.ui_mainwindow import Ui_MainWindow
from clsSettingWindow import SettingWindow, PasswordDialog

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
        password_dialog = PasswordDialog(setting_window)
        password_dialog.exec()

    def false_tool(self):
        self.ui.lbl_process_state.setText("Einsatz wechseln!")
        cvir.lock_start()

    def right_tool(self):
        self.ui.lbl_process_state.setText("Schrauben starten!")
        cvir.release_start()

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
    if cvir.outIO.value:
        window.ui.lbl_cvir_state.setText("In Ordnung")
        next_step()
    elif cvir.outNIO.value:
        window.ui.lbl_cvir_state.setText("Nicht in Ordnung")
    elif cvir.outZLAEUF.value:
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
setting_window = SettingWindow(product)
# Interupt
# Toolbox - Tool changed
toolbox.outBit0.when_activated = check_tool
toolbox.outBit1.when_activated = check_tool
toolbox.outBit2.when_activated = check_tool
# CVIR - Statusmeldung
cvir.outIO.when_activated = io_activated
cvir.outNIO.when_activated = io_activated
cvir.outZLAEUF.when_activated = io_activated

sys.exit(app.exec())
