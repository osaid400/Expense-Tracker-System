# src/models.py

import json
from datetime import date


class Expense:
    def __init__(self, expense_id, title, category, amount, expense_date=None):
        self.expense_id = int(expense_id)
        self.title = title.strip()
        self.category = category.strip().capitalize()
        self.amount = float(amount)
        self.date = expense_date if expense_date else date.today().strftime("%d-%m-%Y")

    def to_dict(self):
        return {
            "Expense ID": self.expense_id,
            "Title": self.title,
            "Category": self.category,
            "Amount": self.amount,
            "Date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            expense_id=data.get("Expense ID", 0),
            title=data.get("Title", "Untitled"),
            category=data.get("Category", "General"),
            amount=data.get("Amount", 0.0),
            expense_date=data.get("Date")
        )