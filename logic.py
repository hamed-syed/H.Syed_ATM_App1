
import csv
from account import SavingAccount

class ATMLogic:
    def __init__(self):
        self.account = None

    def login(self, username: str) -> bool:
        try:
            with open("users.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username:
                        balance = float(row[1])
                        self.account = SavingAccount(username)
                        self.account.set_balance(balance)
                        return True
        except FileNotFoundError:
            pass
        return False

    def get_balance(self) -> float:
        return self.account.get_balance() if self.account else 0.0

    def deposit(self, amount: float) -> None:
        if self.account:
            self.account.deposit(amount)
            self.save()

    def withdraw(self, amount: float) -> bool:
        if self.account:
            result = self.account.withdraw(amount)
            self.save()
            return result
        return False

    def save(self):
        rows = []
        try:
            with open("users.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == self.account.get_name():
                        row[1] = str(self.account.get_balance())
                    rows.append(row)
        except FileNotFoundError:
            pass
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
