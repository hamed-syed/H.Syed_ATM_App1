
class Account:
    def __init__(self, name: str, balance: float = 0):
        self.__account_name = name
        self.__account_balance = 0
        self.set_balance(balance)

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name

    def set_balance(self, value: float) -> None:
        if value >= 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0

    def set_name(self, value: str) -> None:
        self.__account_name = value

    def __str__(self) -> str:
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'

class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name: str):
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self) -> None:
        if self.__deposit_count % 5 == 0:
            balance = self.get_balance()
            self.set_balance(balance + (balance * SavingAccount.RATE))

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            success = super().deposit(amount)
            if success:
                self.__deposit_count += 1
                self.apply_interest()
            return success
        return False

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and self.get_balance() - amount >= SavingAccount.MINIMUM:
            return super().withdraw(amount)
        return False

    def set_balance(self, value: float) -> None:
        if value >= SavingAccount.MINIMUM:
            super().set_balance(value)
        else:
            super().set_balance(SavingAccount.MINIMUM)
