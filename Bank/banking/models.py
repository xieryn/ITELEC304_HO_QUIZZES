from django.db import models

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0)

    # Instance Method
    def display_info(self):
        return f"Account of {self.name} has balance {self._balance}"

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
            return f"Deposited {amount}"
        return "Invalid deposit amount"

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.save()
            return f"Withdrawn {amount}"
        return "Insufficient balance"

    # Getter
    def get_balance(self):
        return self._balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
            return "Balance updated"
        return "Negative balance is not allowed"

    def __str__(self):
        return self.name
