import tkinter as tk
from tkinter import messagebox
import csv

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM App")
        self.username = tk.StringVar()
        self.amount = tk.StringVar()
        self.balance = 0.0
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username:").pack()
        tk.Entry(self.root, textvariable=self.username).pack()
        tk.Button(self.root, text="Login", command=self.login).pack()

        self.balance_label = tk.Label(self.root, text="Balance: Hidden")
        self.balance_label.pack()

        tk.Entry(self.root, textvariable=self.amount).pack()
        tk.Button(self.root, text="Deposit", command=self.deposit).pack()
        tk.Button(self.root, text="Withdraw", command=self.withdraw).pack()

    def login(self):
        name = self.username.get().strip()
        try:
            with open("users.csv") as file:
                for row in csv.reader(file):
                    if row[0] == name:
                        self.balance = float(row[1])
                        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
                        return
            messagebox.showerror("Login Failed", "User not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "users.csv file not found.")

    def deposit(self):
        try:
            amt = float(self.amount.get())
            if amt > 0:
                self.balance += amt
                self.update_balance()
                messagebox.showinfo("Success", "Deposit successful.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        try:
            amt = float(self.amount.get())
            if 0 < amt <= self.balance:
                self.balance -= amt
                self.update_balance()
                messagebox.showinfo("Success", "Withdrawal successful.")
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid input.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        rows = []
        try:
            with open("users.csv") as file:
                for row in csv.reader(file):
                    if row[0] == self.username.get().strip():
                        row[1] = str(self.balance)
                    rows.append(row)
        except FileNotFoundError:
            rows = [[self.username.get().strip(), str(self.balance)]]
        with open("users.csv", "w", newline="") as file:
            csv.writer(file).writerows(rows)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
