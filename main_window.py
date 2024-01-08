from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox

from UI.ui_mainwindow import Ui_MainWindow
from UI.ui_pwdialog import Ui_PasswordDialog

class MainWindow(QMainWindow):
    def __init__(self, setting_window, product, toolbox, cvir):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setting_window = setting_window
        self.product = product
        self.toolbox = toolbox
        self.cvir = cvir

        self.ui.sb_artno.valueChanged.connect(self.product_change)
        self.ui.btn_skip.clicked.connect(self.next_step)
        self.ui.btn_exit.clicked.connect(self.product_change)
        self.ui.btn_settings.clicked.connect(self.open_settings)
        # Interupt
        # Toolbox - Act when Tool is changed
        self.toolbox.outBit0.when_activated = self.check_tool
        self.toolbox.outBit0.when_deactivated = self.check_tool
        self.toolbox.outBit1.when_activated = self.check_tool
        self.toolbox.outBit1.when_deactivated = self.check_tool
        self.toolbox.outBit2.when_activated = self.check_tool
        self.toolbox.outBit2.when_deactivated = self.check_tool
        # CVIR - Act when CVIR state is changed
        self.cvir.outIO.when_activated = self.show_cvir_state
        self.cvir.outNIO.when_activated = self.show_cvir_state
        self.cvir.outNIO.when_deactivated = self.reset_nio
        self.cvir.outZLAEUF.when_activated = self.show_cvir_state

    # React on change of product number
    def product_change(self):
        # valid product number
        if self.product.select_product(self.ui.sb_artno.value()):
            self.ui.txt_name.setText(self.product.get_name())
            self.cvir.step = 1
            self.update_process(self.cvir.step)
        # invalid product number
        else:
            self.ui.txt_name.setText("Produkt nicht bekannt")
            self.ui.txt_tool.setText("")
            self.ui.txt_process.setText("")

    def tool_is_false(self):
        self.ui.lbl_process_state.setText("Einsatz wechseln!")
        self.cvir.lock_start()

    def tool_is_right(self):
        self.ui.lbl_process_state.setText("Schrauben starten!")
        self.cvir.release_start()

    # Go to next step if CVIR state is IO
    def next_step(self):
        if self.cvir.step < self.product.get_steps():
            self.cvir.step = self.cvir.step + 1
        else:
            self.cvir.step = 1
        self.update_process(self.cvir.step)
    
    # Update Process depending on product and step
    def update_process(self, step):
        self.ui.txt_process.setText(str(step) + " von " + str(self.product.get_steps()))
        cyc = self.product.get_cyc(step)
        self.cvir.set_cyc(cyc)
        tool = self.product.get_toolname(step)
        self.ui.txt_tool.setText(str(tool))
        self.check_tool()

    # Check if selected Tool fits to Product and Step
    # Show label and lock/release CVIR
    def check_tool(self):
        if self.toolbox.get_tool() != self.product.get_toolno(self.cvir.step):
            self.tool_is_false()
        else:
            self.tool_is_right()

    # Open Settings protected with Password Dialog
    def open_settings(self):
        password_dialog = PasswordDialog(self.setting_window)
        password_dialog.exec()

    # Show CVIR state in label
    def show_cvir_state(self):
        if self.cvir.outIO.value:
            self.ui.lbl_cvir_state.setText("In Ordnung")
            self.ui.lbl_process_state.setText("")
            self.next_step()
        elif self.cvir.outNIO.value:
            self.ui.lbl_cvir_state.setText("Nicht in Ordnung")
            self.ui.lbl_process_state.setText("Fehler quittieren!")
        elif self.cvir.outZLAEUF.value:
            self.ui.lbl_cvir_state.setText("")
            self.ui.lbl_process_state.setText("Schrauber läuft!")

    def reset_nio(self):
        self.ui.lbl_process_state.setText("Schrauben wiederholen!")

class PasswordDialog(QDialog):
    def __init__(self, setting_window):
        super().__init__()
        self.ui = Ui_PasswordDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.handle_login)
        self.setting_window = setting_window

    # Update and show Setting Window if Password is valid
    def handle_login(self):
        if self.ui.txt_password.text() == '1000':
            self.setting_window.read_all()
            self.setting_window.show()
        else:
            QMessageBox.warning(self, 'Error', 'Falsches Servicepassword')
