# src/ UI.py

import sys
from datetime import date, datetime
from src.manager import Expense_Manager


class UI:

    def __init__(self):
        self.manager = Expense_Manager()

    @staticmethod
    def print_expense(expense):
        try:
            print(f"{expense.expense_id:<12} {expense.title:<20} {expense.category:<18} {Expense_Manager.format_currency(expense.amount):<18} {expense.date:<15}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def print_table_header():
        print("="*88)
        print("{:<12} {:<20} {:<18} {:<18} {:<15}".format("Expense ID", "Title", "Category", "Amount", "Date"))
        print("="*88)

    def add_expense(self):
        title = input("Enter the Expense Title: ")
        if not title.strip():
            print("Expense Title cannot be empty!")
            return

        category = input("Enter the Expense Category: ")
        if not category.strip():
            print("Category cannot be empty!")
            return

        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be a positive number!")
                return
        except ValueError:
            print("Invalid Amount! Please enter a number.")
            return

        date_input = input("Enter date (DD-MM-YYYY) [Leave blank for today]: ").strip()
        expense_date = None
        if date_input:
            parsed_date = self.manager.parse_date(date_input)
            if parsed_date:
                expense_date = parsed_date.strftime("%d-%m-%Y")
            else:
                print("Invalid date format! Using today's date.")
                expense_date = date.today().strftime("%d-%m-%Y")
        else:
            expense_date = date.today().strftime("%d-%m-%Y")

        exp_dt = self.manager.parse_date(expense_date)
        current_month_total = sum(exp.amount for exp in self.manager.filter_by_month(exp_dt.year, exp_dt.month))
        if current_month_total + amount > self.manager.monthly_budget:
            print(f"⚠️ WARNING: Adding this expense exceeds your monthly budget of {self.manager.format_currency(self.manager.monthly_budget)}!")

        new_id = self.manager.add_expense_data(title, category, amount, expense_date)
        print(f"New Expense Added Successfully! Assigned ID: {new_id}")

    def view_expense(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return

        print("View Options:")
        print("1. Overall Expenses")
        print("2. View Per Year")
        print("3. View Per Month")

        try:
            sub_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice!")
            return

        filtered_expenses = []
        view_title = ""

        if sub_choice == 1:
            filtered_expenses = self.manager.expenses
            view_title = "Overall Expenses"
        elif sub_choice == 2:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
            except ValueError:
                print("Invalid year!")
                return
            for e in self.manager.expenses:
                dt = self.manager.parse_date(e.date)
                if dt and dt.year == year:
                    filtered_expenses.append(e)
            view_title = f"Expenses for Year {year}"
        elif sub_choice == 3:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
                month = int(input("Enter Month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    return
            except ValueError:
                print("Invalid input!")
                return
            filtered_expenses = self.manager.filter_by_month(year, month)
            month_name = datetime(year, month, 1).strftime("%B %Y")
            view_title = f"Expenses for {month_name}"
        else:
            print("Invalid choice!")
            return

        if not filtered_expenses:
            print("No expenses found for the selected option.")
            return

        print(f"\n---------------- {view_title} ----------------")
        self.print_table_header()
        for expense in filtered_expenses:
            self.print_expense(expense)
        print("="*88)

        total_amount = sum(e.amount for e in filtered_expenses)
        unique_years = set()
        unique_months = set()
        for e in filtered_expenses:
            dt = self.manager.parse_date(e.date)
            if dt:
                unique_years.add(dt.year)
                unique_months.add((dt.year, dt.month))

        print(f"Total Amount: {self.manager.format_currency(total_amount)}")
        print(f"Total Years: {len(unique_years)} ({', '.join(map(str, sorted(unique_years)))})")
        print(f"Total Months: {len(unique_months)}")
        print("-" * 50)

    def search_expense(self):
        print("Search By:")
        print("1. Search by ID")
        print("2. Search by Title")
        print("3. Search by Category")
        try:
            search_option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            return

        if search_option == 1:
            try:
                search_id = int(input("Enter the Expense ID: "))
            except ValueError:
                print("Invalid Expense ID!")
                return
            found = self.manager.find_by_id(search_id)
            if found:
                self.print_table_header()
                self.print_expense(found)
                print("="*88)
            else:
                print("Expense Not Found!")
        elif search_option == 2:
            search_title = input("Enter the Expense Title: ").strip()
            if not search_title:
                print("Title cannot be empty!")
                return
            matches = [e for e in self.manager.expenses if search_title.lower() in e.title.lower()]
            if matches:
                self.print_table_header()
                for m in matches:
                    self.print_expense(m)
                print("="*88)
            else:
                print("Expense Not Found!")
        elif search_option == 3:
            search_category = input("Enter the Expense Category: ")
            if not search_category.strip():
                print("Category cannot be empty!")
                return
            cat_normalized = search_category.strip().capitalize()
            matches = [e for e in self.manager.expenses if cat_normalized in e.category]
            if matches:
                self.print_table_header()
                for m in matches:
                    self.print_expense(m)
                print("="*88)
            else:
                print("Expense Not Found!")
        else:
            print("Invalid choice!")

    def update_expense(self):
        try:
            search_id = int(input("Enter the Expense ID: "))
        except ValueError:
            print("Invalid Expense ID!")
            return
        expense = self.manager.find_by_id(search_id)
        if expense:
            print("Current Details:")
            self.print_table_header()
            self.print_expense(expense)
            print("="*88)

            title = input("Enter new title (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            amount_input = input("Enter new amount (leave blank to keep current): ")
            date_input = input("Enter new date DD-MM-YYYY (leave blank to keep current): ")

            new_title = title.strip() if title.strip() else None
            new_category = category.strip().capitalize() if category.strip() else None
            new_amount = None
            if amount_input.strip():
                try:
                    amt = float(amount_input)
                    if amt > 0:
                        new_amount = amt
                    else:
                        print("Amount must be positive! Keeping current.")
                except ValueError:
                    print("Invalid amount! Keeping current.")

            new_date = None
            if date_input.strip():
                parsed = self.manager.parse_date(date_input.strip())
                if parsed:
                    new_date = parsed.strftime("%d-%m-%Y")
                else:
                    print("Invalid date format! Keeping current.")

            self.manager.update_expense_data(search_id, new_title, new_category, new_amount, new_date)
            print("Expense Updated Successfully!")
        else:
            print("Expense Not Found!")

    def delete_expense(self):
        try:
            search_id = int(input("Enter the Expense ID: "))
        except ValueError:
            print("Invalid Expense ID!")
            return
        expense = self.manager.find_by_id(search_id)
        if expense:
            confirm = input(f"Are you sure you want to delete {expense.title}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            self.manager.delete_expense_data(search_id)
            print("Expense Deleted Successfully!")
        else:
            print("Expense Not Found!")

    def total_expense(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return
        print("\nTotal Expense Options:")
        print("1. Overall Total")
        print("2. Yearly Total")
        print("3. Monthly Total")
        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            total = sum(e.amount for e in self.manager.expenses)
            print("-" * 50)
            print(f"Total Expenses (Overall): {self.manager.format_currency(total)}")
            print("-" * 50)
        elif choice == 2:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
            except ValueError:
                print("Invalid year!")
                return
            filtered = []
            for e in self.manager.expenses:
                dt = self.manager.parse_date(e.date)
                if dt and dt.year == year:
                    filtered.append(e)
            total = sum(e.amount for e in filtered)
            print("-" * 50)
            print(f"Total Expenses for Year {year}: {self.manager.format_currency(total)}")
            print("-" * 50)
        elif choice == 3:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
                month = int(input("Enter Month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    return
            except ValueError:
                print("Invalid input!")
                return
            filtered = self.manager.filter_by_month(year, month)
            total = sum(e.amount for e in filtered)
            month_name = datetime(year, month, 1).strftime("%B %Y")
            print("-" * 50)
            print(f"Total Expenses for {month_name}: {self.manager.format_currency(total)}")
            print("-" * 50)
        else:
            print("Invalid choice!")

    def highest_expense_menu(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return
        print("\nHighest Expense Options:")
        print("1. Highest Single Transaction (Overall)")
        print("2. Highest Spending Month (Overall)")
        print("3. Highest Expense in a Specific Month")
        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            highest = max(self.manager.expenses, key=lambda x: x.amount)
            print("------------------------- Highest Single Expense -------------------------")
            self.print_table_header()
            self.print_expense(highest)
            print("="*88)
        elif choice == 2:
            monthly_totals = self.manager.get_monthly_totals()
            if not monthly_totals:
                print("No records found!")
                return
            max_month = max(monthly_totals, key=monthly_totals.get)
            year, month = max_month
            month_name = datetime(year, month, 1).strftime("%B %Y")
            print("------------------------- Highest Spending Month -------------------------")
            print(f"Month: {month_name}")
            print(f"Total Spent: {self.manager.format_currency(monthly_totals[max_month])}")
            print("="*75)
        elif choice == 3:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
                month = int(input("Enter Month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    return
            except ValueError:
                print("Invalid input!")
                return
            filtered = self.manager.filter_by_month(year, month)
            if not filtered:
                month_name = datetime(year, month, 1).strftime("%B %Y")
                print(f"No expenses found for {month_name}.")
                return
            highest = max(filtered, key=lambda x: x.amount)
            month_name = datetime(year, month, 1).strftime("%B %Y")
            print(f"------------------------- Highest Expense for {month_name} -------------------------")
            self.print_table_header()
            self.print_expense(highest)
            print("="*88)
        else:
            print("Invalid choice!")

    def lowest_expense_menu(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return
        print("\nLowest Expense Options:")
        print("1. Lowest Single Transaction (Overall)")
        print("2. Lowest Spending Month (Overall)")
        print("3. Lowest Expense in a Specific Month")
        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            lowest = min(self.manager.expenses, key=lambda x: x.amount)
            print("------------------------- Lowest Single Expense -------------------------")
            self.print_table_header()
            self.print_expense(lowest)
            print("="*88)
        elif choice == 2:
            monthly_totals = self.manager.get_monthly_totals()
            if not monthly_totals:
                print("No records found!")
                return
            min_month = min(monthly_totals, key=monthly_totals.get)
            year, month = min_month
            month_name = datetime(year, month, 1).strftime("%B %Y")
            print("------------------------- Lowest Spending Month -------------------------")
            print(f"Month: {month_name}")
            print(f"Total Spent: {self.manager.format_currency(monthly_totals[min_month])}")
            print("="*75)
        elif choice == 3:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
                month = int(input("Enter Month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    return
            except ValueError:
                print("Invalid input!")
                return
            filtered = self.manager.filter_by_month(year, month)
            if not filtered:
                month_name = datetime(year, month, 1).strftime("%B %Y")
                print(f"No expenses found for {month_name}.")
                return
            lowest = min(filtered, key=lambda x: x.amount)
            month_name = datetime(year, month, 1).strftime("%B %Y")
            print(f"------------------------- Lowest Expense for {month_name} -------------------------")
            self.print_table_header()
            self.print_expense(lowest)
            print("="*88)
        else:
            print("Invalid choice!")

    def average_expense_menu(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return
        print("\nAverage Expense Options:")
        print("1. Overall Monthly Average")
        print("2. Average Per Transaction")
        try:
            choice = int(input("Enter choice (1-2): "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            monthly_totals = self.manager.get_monthly_totals()
            if not monthly_totals:
                print("No records found!")
                return
            avg_monthly = sum(monthly_totals.values()) / len(monthly_totals)
            print("-" * 50)
            print(f"Average Monthly Expense: {self.manager.format_currency(avg_monthly)}")
            print("-" * 50)
        elif choice == 2:
            avg_trans = sum(e.amount for e in self.manager.expenses) / len(self.manager.expenses)
            print("-" * 50)
            print(f"Average Per Transaction: {self.manager.format_currency(avg_trans)}")
            print("-" * 50)
        else:
            print("Invalid choice!")

    def category_summary(self):
        if not self.manager.expenses:
            print("No Expenses in record!")
            return
        print("\nCategory Summary Options:")
        print("1. Overall Category Summary")
        print("2. Yearly Category Summary")
        print("3. Monthly Category Summary")
        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid choice!")
            return

        filtered = []
        title = ""
        if choice == 1:
            filtered = self.manager.expenses
            title = "Overall Category Summary"
        elif choice == 2:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
            except ValueError:
                print("Invalid year!")
                return
            for e in self.manager.expenses:
                dt = self.manager.parse_date(e.date)
                if dt and dt.year == year:
                    filtered.append(e)
            title = f"Category Summary for Year {year}"
        elif choice == 3:
            try:
                year = int(input("Enter Year (e.g., 2026): "))
                month = int(input("Enter Month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    return
            except ValueError:
                print("Invalid input!")
                return
            filtered = self.manager.filter_by_month(year, month)
            month_name = datetime(year, month, 1).strftime("%B %Y")
            title = f"Category Summary for {month_name}"
        else:
            print("Invalid choice!")
            return

        if not filtered:
            print("No expenses found for the selected option.")
            return

        summary = {}
        for e in filtered:
            summary[e.category] = summary.get(e.category, 0.0) + e.amount

        print(f"\n================ {title} ================")
        print(f"{'Category':<30} {'Total Amount':<20}")
        print("="*50)
        for cat, amt in summary.items():
            print(f"{cat:<30} {self.manager.format_currency(amt):<20}")
        print("="*50)

    def manage_budget(self):
        print(f"Current Monthly Budget: {self.manager.format_currency(self.manager.monthly_budget)}")
        try:
            new_budget = float(input("Enter new monthly budget: "))
            if new_budget > 0:
                self.manager.monthly_budget = new_budget
                self.manager.save_budget()
                print("Monthly Budget Updated Successfully!")
            else:
                print("Budget must be greater than zero!")
        except ValueError:
            print("Invalid input!")

    def generate_monthly_report(self):
        try:
            year = int(input("Enter Year (e.g., 2026): "))
            month = int(input("Enter Month (1-12): "))
            if not (1 <= month <= 12):
                print("Invalid month!")
                return
        except ValueError:
            print("Invalid input!")
            return

        filepath = self.manager.generate_monthly_report_file(year, month)
        print(f"\nMonthly Report Generated Successfully!")
        print(f"Saved to: {filepath}")

    def exit_system(self):
        print("-" * 50)
        print("Exiting the Expense Tracker. Goodbye!")
        print("-" * 50)
        sys.exit()

    def run(self):
        print("============ Welcome to Expense Tracker SYSTEM =============")
        while True:
            print()
            print("=============== Select the Option (0-12) ================")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Search Expense")
            print("4. Update Expense")
            print("5. Delete Expense")
            print("6. Total Expenses")
            print("7. Highest Expense Analytics")
            print("8. Lowest Expense Analytics")
            print("9. Average Expense Analytics")
            print("10. Category-wise Summary")
            print("11. Set / Check Monthly Budget")
            print("12. Generate Monthly Report")
            print("0. Exit")
            print("=========================================================")

            try:
                choice = int(input("Enter the number: "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                continue

            if choice == 1:
                self.add_expense()
            elif choice == 2:
                self.view_expense()
            elif choice == 3:
                self.search_expense()
            elif choice == 4:
                self.update_expense()
            elif choice == 5:
                self.delete_expense()
            elif choice == 6:
                self.total_expense()
            elif choice == 7:
                self.highest_expense_menu()
            elif choice == 8:
                self.lowest_expense_menu()
            elif choice == 9:
                self.average_expense_menu()
            elif choice == 10:
                self.category_summary()
            elif choice == 11:
                self.manage_budget()
            elif choice == 12:
                self.generate_monthly_report()
            elif choice == 0:
                self.exit_system()
            else:
                print("Invalid Choice! Choose between 0 to 12.")