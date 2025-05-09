
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMessageBox
from logic import ATMLogic

class ATMApp(QWidget):
    def __init__(self):
        super().__init__()
        self.logic = ATMLogic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ATM App")
        self.login_label = QLabel("Enter Username:")
        self.login_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.balance_label = QLabel("Balance: Hidden")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.deposit_button = QPushButton("Deposit")
        self.withdraw_button = QPushButton("Withdraw")
        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.balance_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.deposit_button)
        layout.addWidget(self.withdraw_button)
        self.setLayout(layout)

    def login(self):
        username = self.login_input.text().strip()
        if self.logic.login(username):
            self.update_balance()
            QMessageBox.information(self, "Login", f"Welcome {username}!")
        else:
            QMessageBox.warning(self, "Login Failed", "User not found.")

    def update_balance(self):
        self.balance_label.setText(f"Balance: ${self.logic.get_balance():.2f}")

    def deposit(self):
        try:
            amount = float(self.amount_input.text())
            self.logic.deposit(amount)
            self.update_balance()
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount")

    def withdraw(self):
        try:
            amount = float(self.amount_input.text())
            if not self.logic.withdraw(amount):
                QMessageBox.warning(self, "Error", "Insufficient funds or invalid input")
            self.update_balance()
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount")
