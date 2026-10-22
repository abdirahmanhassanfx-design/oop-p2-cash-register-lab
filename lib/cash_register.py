#!/usr/bin/env python3

class CashRegister:
    """Simulates a cash register that can add items, apply a discount, and void the last sale."""

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount is a whole-number percent off the total, from 0 through 100.
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, title, price, quantity=1):
        """Add an item (and optional quantity) to the register."""
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        """Take the discount percent off the current total."""
        if self.discount:
            self.total = self.total * (100 - self.discount) / 100
            if self.total == int(self.total):
                self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the most recent transaction from the total and the item list."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            if self.items:
                self.items.pop()
