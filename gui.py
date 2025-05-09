from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from logic import ATMLogic

class ATMApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("atm.ui", self)
        self.logic = ATMLogic()
        self.login_button.clicked.connect(self.login)
        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)

    def login(self):
        username = self.login_input.text().strip()
        if self.logic.login(username):
            self.update_balance()
            self.show_message("Login successful", "info")
        else:
            self.show_message("User not found", "error")

    def update_balance(self):
        self.balance_label.setText(f"Balance: ${self.logic.get_balance():.2f}")

    def deposit(self):
        try:
            amount = float(self.amount_input.text())
            self.logic.deposit(amount)
            self.update_balance()
            self.show_message("Deposit successful", "success")
        except ValueError:
            self.show_message("Invalid amount", "error")

    def withdraw(self):
        try:
            amount = float(self.amount_input.text())
            if not self.logic.withdraw(amount):
                self.show_message("Insufficient funds or invalid input", "error")
            self.update_balance()
        except ValueError:
            self.show_message("Invalid amount", "error")

    def show_message(self, message: str, level: str):
        colors = {
            "info": "#2196F3",
            "success": "#4CAF50",
            "error": "#F44336"
        }
        QMessageBox.information(self, "Message", message)
        self.balance_label.setStyleSheet(f"color: {colors.get(level, 'black')}")
