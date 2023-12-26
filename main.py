# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from UI.ui_mainwindow import Ui_MainWindow
from setting_window import SettingWindow, PasswordDialog

from cvir import CVIR
from toolbox import Toolbox
from product import Product

toolbox = Toolbox()
product = Product()
cvir = CVIR()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sb_artno.valueChanged.connect(self.product_change)
        self.ui.btn_skip.clicked.connect(next_step)
        self.ui.btn_exit.clicked.connect(self.product_change)
        self.ui.btn_settings.clicked.connect(open_settings)

    # React on change of product number
    def product_change(self):
        # valid product number
        if product.select_product(self.ui.sb_artno.value()):
            self.ui.txt_name.setText(product.get_name())
            cvir.step = 1
            update_process(cvir.step)
        # invalid product number
        else:
            self.ui.txt_name.setText("Produkt nicht bekannt")
            self.ui.txt_tool.setText("")
            self.ui.txt_process.setText("")

    def tool_is_false(self):
        self.ui.lbl_process_state.setText("Einsatz wechseln!")
        cvir.lock_start()

    def tool_is_right(self):
        self.ui.lbl_process_state.setText("Schrauben starten!")
        cvir.release_start()


# Check if selected Tool fits to Product and Step
# Show label and lock/release CVIR
def check_tool():
    if toolbox.get_tool() != product.get_toolno(cvir.step):
        window.tool_is_false()
    else:
        window.tool_is_right()


# Open Settings protected with Password Dialog
def open_settings():
    password_dialog = PasswordDialog(setting_window)
    password_dialog.exec()


# Update Process depending on product and step
def update_process(step):
    window.ui.txt_process.setText(str(step) + " von " + str(product.get_steps()))
    cyc = product.get_cyc(step)
    cvir.set_cyc(cyc)
    tool = product.get_toolname(step)
    window.ui.txt_tool.setText(str(tool))
    check_tool()


# Show CVIR state in label
def show_cvir_state():
    if cvir.outIO.value:
        window.ui.lbl_cvir_state.setText("In Ordnung")
        next_step()
    elif cvir.outNIO.value:
        window.ui.lbl_cvir_state.setText("Nicht in Ordnung")
    elif cvir.outZLAEUF.value:
        window.ui.lbl_cvir_state.setText("")
        window.ui.lbl_process_state.setText("Schrauber läuft!")


# Go to next step if CVIR state is IO
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
# Initialized SettingWindow
setting_window = SettingWindow(product)
# Interupt
# Toolbox - Act when Tool is changed
toolbox.outBit0.when_activated = check_tool
toolbox.outBit0.when_deactivated = check_tool
toolbox.outBit1.when_activated = check_tool
toolbox.outBit1.when_deactivated = check_tool
toolbox.outBit2.when_activated = check_tool
toolbox.outBit2.when_deactivated = check_tool
# CVIR - Act when CVIR state is changed
cvir.outIO.when_activated = show_cvir_state
cvir.outNIO.when_activated = show_cvir_state
cvir.outZLAEUF.when_activated = show_cvir_state

# Execute Application
sys.exit(app.exec())
