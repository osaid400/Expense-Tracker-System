# EXPENSE TRACKER SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python

import json
import sys
from datetime import datetime


class Expense:

    def __init__(self, expense_id, title, category, amount, date_time=None):
        self.expense_id = expense_id
        self.title = title
        self.category = category
        self.amount = amount
        if date_time is None:
            self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date_time = date_time

    def to_dict(self):
        return {
            "Title": self.title,
            "Expense ID": self.expense_id,
            "Category": self.category,
            "Amount": self.amount,
            "Date and Time": self.date_time

        }

    @classmethod
    def from_dict(cls, expense_data):
        return cls(
            title = expense_data["Title"],
            expense_id = expense_data["Expense ID"],
            category = expense_data["Category"],
            amount = expense_data["Amount"],
            date_time=expense_data["Date and Time"]
        )


class Expense_Manager:

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()
        if not self.expenses:
            self.expenses = [
                Expense(101, "Groceries", "Food", 3500.0, "2023-03-01 12:00:00"),
                Expense(102, "Bus Fare", "Transport", 800.0, "2023-03-02 08:00:00"),
                Expense(103, "Electricity Bill", "Bills", 5200.0, "2023-03-03 10:00:00"),
                Expense(104, "Internet Bill", "Bills", 2500.0, "2023-03-04 14:00:00"),
                Expense(105, "Mobile Recharge", "Bills", 1200.0, "2023-03-05 16:00:00"),
                Expense(106, "Movie Ticket", "Entertainment", 1800.0, "2023-03-06 20:00:00"),
                Expense(107, "Restaurant", "Food", 2700.0, "2023-03-07 19:00:00"),
                Expense(108, "Books", "Education", 4500.0, "2023-03-08 11:00:00"),
                Expense(109, "Petrol", "Fuel", 6000.0, "2023-03-09 09:00:00"),
                Expense(110, "Medicine", "Health", 2200.0, "2023-03-10 15:00:00"),
                Expense(111, "Gym Fee", "Health", 3000.0, "2023-03-11 18:00:00"),
                Expense(112, "Coffee", "Food", 650.0, "2023-03-12 10:00:00"),
                Expense(113, "Laptop Repair", "Electronics", 8500.0, "2023-03-13 13:00:00"),
                Expense(114, "Clothes", "Shopping", 7200.0, "2023-03-14 17:00:00"),
                Expense(115, "Shoes", "Shopping", 4800.0, "2023-03-15 12:00:00"),
                Expense(116, "Streaming Sub", "Entertainment", 900.0, "2023-03-16 09:00:00"),
                Expense(117, "Stationery", "Education", 1100.0, "2023-03-17 11:00:00"),
                Expense(118, "Water Bill", "Bills", 1400.0, "2023-03-18 14:00:00"),
                Expense(119, "Gift", "Miscellaneous", 2600.0, "2023-03-19 16:00:00"),
                Expense(120, "Taxi", "Transport", 1500.0, "2023-03-20 18:00:00")
            ]
            self.save_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(emp) for emp in data]
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump([exp.to_dict() for exp in self.expenses], f, indent=5)

    def _find_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:  
                return expense
        return None

    @staticmethod
    def format_currency(salary):
        return f"Rs. {salary:,.0f}"

    def print_expense(self, expense):
        print(f"{expense.expense_id:<20} {expense.title:<24} {expense.category:<28} {self.format_currency(expense.amount):<25} {expense.date_time:<25}")

    def total_expense(self):
        if len(self.expenses) == 0:
            print("No Expenses in record!")
            return
        total = sum(expense.amount for expense in self.expenses)
        print("---------------------------------------------------")
        print(f"Total Expenses: {self.format_currency(total)}")
        print("---------------------------------------------------")

    def highest_expense(self):
        if len(self.expenses) == 0:
            print("No Expenses in record!")
            return
        
        highest = max(self.expenses, key=lambda x: x.amount)
        print("----------------------------------------------- Highest Expense ---------------------------------------------- ")
        print("="*120)
        print("{:<20} {:<24} {:<28} {:<25} {:<25} ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
        print("="*120)
        self.print_expense(highest)
        print("="*120)

    def lowest_expense(self):
        if len(self.expenses) == 0:
            print("No Expenses in record!")
            return
        lowest = min(self.expenses, key=lambda x: x.amount)

        print("----------------------------------------------- Lowest Expense ----------------------------------------------- ")
        print("="*120)
        print("{:<20} {:<24} {:<28} {:<25} {:<25}  ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
        print("="*120)
        self.print_expense(lowest)
        print("="*120)

    def average_expense(self):
        if len(self.expenses) == 0:
            print("No Expenses in record!")
            return

        average = sum(expense.amount for expense in self.expenses) / len(self.expenses)
        print("---------------------------------------------------")
        print(f"Average Expense: {self.format_currency(average)}")
        print("---------------------------------------------------")

    def add_expense(self):
        try:
            expense_id = int(input("Enter the Expense ID: "))
        except ValueError:
            print("Invalid Expense ID! Please enter a number.")
            return
        if expense_id <= 0:
            print("Enter a valid Expense ID!")
            return
        if self._find_by_id(expense_id):
            print("Expense ID already exists!")
            return

        title = input("Enter the Expense Title: ")
        category = input("Enter the Expense Category: ")

        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be a positive number!")
                return
        except ValueError:
            print("Invalid Amount! Please enter a number.")
            return

        title = title.strip()
        category = category.strip()

        if title == "":
            print("Expense Title cannot be empty!")
            return

        if category == "":
            print("Category cannot be empty!")
            return

        new_expense = Expense(expense_id, title, category, amount)
        self.expenses.append(new_expense)
        self.save_expenses()
        print("New Expense Added Successfully!")    

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
                print("Invalid Expense ID! Please enter a number.")
                return
            found = self._find_by_id(search_id)
            if found:
                print("="*120)
                print("{:<20} {:<24} {:<28} {:<25} {:<25} ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
                print("="*120)
                self.print_expense(found)
                print("="*120)
            else:
                print("Expense Not Found!")
        elif search_option == 2:
            search_title = input("Enter the Expense Title: ").strip()
            if search_title == "":
                print("Title cannot be empty!")
                return
            matches = [expense for expense in self.expenses if search_title.lower() in expense.title.lower()]
            if matches:
                print("="*120)
                print("{:<20} {:<24} {:<28} {:<25} {:<25} ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
                print("="*120)
                for match in matches:
                    self.print_expense(match)
                print("="*120)
            else:
                print("Expense Not Found!")
        elif search_option == 3:
            search_category = input("Enter the Expense Category: ").strip()
            if search_category == "":
                print("Category cannot be empty!")
                return
            matches = [expense for expense in self.expenses if search_category.lower() in expense.category.lower()]
            if matches:
                print("="*120)
                print("{:<20} {:<24} {:<28} {:<25} {:<25} ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
                print("="*120)
                for match in matches:
                    self.print_expense(match)
                print("="*120)
            else:
                print("Expense Not Found!")
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

    def view_expense(self):
        if not self.expenses:            
            print("No Expenses in record!")
            return
        self.expenses.sort(key=lambda emp: emp.expense_id)
        print("="*120)
        print("{:<20} {:<24} {:<28} {:<25} {:<25} "
                .format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
        print("="*120)
        for expense in self.expenses:
            self.print_expense(expense)
        print("="*120)

    def exit_system(self):
        print("---------------------------------------------------")
        print("Exiting the Expense Tracker.")
        print("Thank you for using the system. Goodbye!")
        print("---------------------------------------------------")
        sys.exit()

    def update_expense(self):
        try:
            search_id = int(input("Enter the Expense ID: "))
        except ValueError:
            print("Invalid Expense ID! Please enter a number.")
            return

        expense = self._find_by_id(search_id)
        if expense:
            print("-"*110)
            print("Current Details")
            print("="*110)
            print("{:<20} {:<24} {:<28} {:<25} {:<25} ".format("Expense ID", "Title", "Category", "Amount", "Date and Time"))
            print("="*110)
            self.print_expense(expense)
            print("="*110)

            title = input("Enter the new Expense title (leave blank to keep current): ")
            category = input("Enter the new Category title (leave blank to keep current): ")
            amount_input = input("Enter the new expense amount (leave blank to keep current): ")

            if title.strip():
                expense.title = title.strip()
            if category.strip():
                expense.category = category.strip()
            if amount_input.strip():

                try:
                    amount_input = float(amount_input)
                    if amount_input <= 0:
                        print("Amount must be a positive number! Keeping current amount.")
                    else:
                        expense.amount = amount_input
                except ValueError:

                    print("Invalid Amount! Keeping current amount.")
            self.save_expenses()
            print("Expense Updated Successfully!")

        else:
            print("Expense Not Found!")

    def delete_expense(self):
        try:
            search_id = int(input("Enter the Expense ID: "))
        except ValueError:
            print("Invalid Expense ID! Please enter a number.")
            return
        expense = self._find_by_id(search_id)
        if expense:
            confirm = input(f"Are you sure you want to delete expense {expense.title}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            self.expenses.remove(expense)
            self.save_expenses()
            print("Expense Deleted Successfully!")
        else:
            print("Expense Not Found!")


def main ():

    print ("============ Welcome to Expense Tracker SYSTEM =============")

    expense  = Expense_Manager()

    while True:
        print()
        print("=============== Select the Option (0-9) ===============")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Total Expenses")
        print("7. Highest Expense")
        print("8. Lowest Expense")
        print("9. Average Expense")
        print("0. Exit")
        print("========================================================")

        try:
            choice = int(input("Enter the number: "))
        except ValueError:
            print("Invalid Choice! Please enter a number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        if choice == 1:
            expense.add_expense()
        elif choice == 2:
            expense.view_expense()
        elif choice == 3:
            expense.search_expense()
        elif choice == 4:
            expense.update_expense()
        elif choice == 5:
            expense.delete_expense()
        elif choice == 6:
            expense.total_expense()
        elif choice == 7:
            expense.highest_expense()
        elif choice == 8:
            expense.lowest_expense()
        elif choice == 9:
            expense.average_expense()
        elif choice == 0:
            expense.exit_system()
        else:
            print("Invalid Choice! Choose between 0 to 9")


if __name__ == "__main__":
    main()