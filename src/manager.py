# src/manager.py

import json
import os
from datetime import date, datetime
from src.models import Expense


class Expense_Manager:

    def __init__(self, filename="expenses.json"):
        os.makedirs("data", exist_ok=True)
        self.filename = os.path.join("data", filename)
        self.budget_file = os.path.join("data", "budget.json")
        self.expenses = []
        self.monthly_budget = self.load_budget()
        self.load_expenses()
        if not self.expenses:
            today_str = date.today().strftime("%d-%m-%Y")
            self.expenses = [
                Expense(101, "Groceries", "Food", 3500.0, today_str),
                Expense(102, "Bus Fare", "Transport", 800.0, today_str),
                Expense(103, "Electricity Bill", "Bills", 5200.0, today_str),
                Expense(104, "Internet Bill", "Bills", 2500.0, today_str),
                Expense(105, "Mobile Recharge", "Bills", 1200.0, today_str),
                Expense(106, "Movie Ticket", "Entertainment", 1800.0, today_str),
                Expense(107, "Restaurant", "Food", 2700.0, today_str),
                Expense(108, "Books", "Education", 4500.0, today_str),
                Expense(109, "Petrol", "Fuel", 6000.0, today_str),
                Expense(110, "Medicine", "Health", 2200.0, today_str)
            ]
            self.save_expenses()

    def load_budget(self):
        try:
            with open(self.budget_file, 'r') as f:
                data = json.load(f)
                return data.get("budget", 50000.0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 50000.0

    def save_budget(self):
        with open(self.budget_file, 'w') as f:
            json.dump({"budget": self.monthly_budget}, f, indent=4)

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump([exp.to_dict() for exp in self.expenses], f, indent=4)

    def find_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None

    @staticmethod
    def parse_date(date_str):
        for fmt in ("%d-%m-%Y", "%B %Y", "%m-%Y", "%Y"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None

    def filter_by_month(self, year, month):
        result = []
        for e in self.expenses:
            dt = self.parse_date(e.date)
            if dt and dt.year == year and dt.month == month:
                result.append(e)
        return result

    @staticmethod
    def format_currency(amount):
        return f"Rs. {amount:,.0f}"

    def get_monthly_totals(self):
        monthly_totals = {}
        for exp in self.expenses:
            dt = self.parse_date(exp.date)
            if dt:
                key = (dt.year, dt.month)
                monthly_totals[key] = monthly_totals.get(key, 0.0) + exp.amount
        return monthly_totals

    def add_expense_data(self, title, category, amount, expense_date=None):
        expense_id = max((e.expense_id for e in self.expenses), default=100) + 1
        if not expense_date:
            expense_date = date.today().strftime("%d-%m-%Y")
        new_expense = Expense(expense_id, title, category, amount, expense_date)
        self.expenses.append(new_expense)
        self.save_expenses()
        return expense_id

    def update_expense_data(self, expense_id, title=None, category=None, amount=None, expense_date=None):
        expense = self.find_by_id(expense_id)
        if not expense:
            return False
        if title:
            expense.title = title.strip()
        if category:
            expense.category = category.strip().capitalize()
        if amount is not None:
            expense.amount = float(amount)
        if expense_date:
            expense.date = expense_date
        self.save_expenses()
        return True

    def delete_expense_data(self, expense_id):
        expense = self.find_by_id(expense_id)
        if expense:
            self.expenses.remove(expense)
            self.save_expenses()
            return True
        return False

    def generate_monthly_report_file(self, year, month):
        filtered = self.filter_by_month(year, month)
        dt_obj = datetime(year, month, 1)
        month_name = dt_obj.strftime("%B")
        month_year_str = f"{month_name} {year}"

        total_spent = sum(e.amount for e in filtered)
        budget = self.monthly_budget

        if budget > 0:
            pct_used = (total_spent / budget) * 100
        else:
            pct_used = 0.0

        if total_spent <= budget:
            diff = budget - total_spent
            budget_status = f"Rs. {diff:,.0f} remaining ({pct_used:.1f}% used)"
        else:
            diff = total_spent - budget
            budget_status = f"Rs. {diff:,.0f} exceeded ({pct_used:.1f}% used)"

        cat_summary = {}
        for e in filtered:
            cat_summary[e.category] = cat_summary.get(e.category, 0.0) + e.amount

        sorted_expenses = sorted(filtered, key=lambda x: x.amount, reverse=True)
        top_3 = sorted_expenses[:3]
        chrono_expenses = sorted(filtered, key=lambda x: self.parse_date(x.date) if self.parse_date(x.date) else datetime.min)

        report_lines = []
        report_lines.append("=" * 53)
        report_lines.append(f"{'MONTHLY EXPENSE REPORT':^53}")
        report_lines.append(f"{month_year_str:^53}")
        report_lines.append("=" * 53)
        report_lines.append(f"Generated On: {date.today().strftime('%d-%m-%Y')}")
        report_lines.append("")
        report_lines.append("-" * 53)
        report_lines.append("BUDGET OVERVIEW")
        report_lines.append("-" * 53)
        report_lines.append(f"Monthly Budget    : Rs. {budget:,.0f}")
        report_lines.append(f"Total Spent       : Rs. {total_spent:,.0f}")
        report_lines.append(f"Remaining/Exceeded: {budget_status}")
        report_lines.append("-" * 53)
        report_lines.append("")
        report_lines.append("-" * 53)
        report_lines.append("CATEGORY BREAKDOWN")
        report_lines.append("-" * 53)
        report_lines.append(f"{'Category':<18} {'Amount':<15} {'% of Total':<15}")
        for cat, amt in cat_summary.items():
            pct = (amt / total_spent * 100) if total_spent > 0 else 0.0
            report_lines.append(f"{cat:<18} {amt:<15,.0f} {pct:.1f}%")
        report_lines.append("-" * 53)
        report_lines.append("")
        report_lines.append("-" * 53)
        report_lines.append("TOP 3 EXPENSES THIS MONTH")
        report_lines.append("-" * 53)
        if top_3:
            for idx, exp in enumerate(top_3, 1):
                report_lines.append(f"{idx}. {exp.title:<18} Rs. {exp.amount:,.0f}    {exp.date}")
        else:
            report_lines.append("No expenses recorded for this month.")
        report_lines.append("-" * 53)
        report_lines.append("")
        report_lines.append("-" * 53)
        report_lines.append("ALL TRANSACTIONS (chronological)")
        report_lines.append("-" * 53)
        if chrono_expenses:
            report_lines.append(f"{'Title':<22} {'Amount':<16} {'Date':<13}")
            report_lines.append("-" * 53)
            for exp in chrono_expenses:
                report_lines.append(f"{exp.title:<22} {self.format_currency(exp.amount):<16} {exp.date:<13}")
        else:
            report_lines.append("No transactions found.")
        report_lines.append("=" * 53)

        report_content = "\n".join(report_lines)
        os.makedirs("Reports", exist_ok=True)
        filename = f"report_{month_name.lower()}_{year}.txt"
        filepath = os.path.join("Reports", filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_content)

        return filepath