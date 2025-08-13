#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = None

  def add_item(self, name, price, quantity=1):
    if name.strip() != "" and price > 0:
      for i in range(quantity):
        self.items.append(name)
      
      total_added = price * quantity

      self.total += total_added

      self.last_transaction = total_added

  def apply_discount(self):
    if self.discount > 0:
      total = self.total

      self.total = total - (total * (self.discount / 100))

      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
