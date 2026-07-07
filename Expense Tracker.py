# EXPENSE TRACKER SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

print ("============ Welcome to Expense Tracker SYSTEM =============")

expenses = [
    {"Expense ID": 101, "Title": "Groceries", "Category": "Food", "Amount": 3500.0},
    {"Expense ID": 102, "Title": "Bus Fare", "Category": "Transport", "Amount": 800.0},
    {"Expense ID": 103, "Title": "Electricity Bill", "Category": "Bills", "Amount": 5200.0},
    {"Expense ID": 104, "Title": "Internet Bill", "Category": "Bills", "Amount": 2500.0},
    {"Expense ID": 105, "Title": "Mobile Recharge", "Category": "Bills", "Amount": 1200.0},
    {"Expense ID": 106, "Title": "Movie Ticket", "Category": "Entertainment", "Amount": 1800.0},
    {"Expense ID": 107, "Title": "Restaurant", "Category": "Food", "Amount": 2700.0},
    {"Expense ID": 108, "Title": "Books", "Category": "Education", "Amount": 4500.0},
    {"Expense ID": 109, "Title": "Petrol", "Category": "Fuel", "Amount": 6000.0},
    {"Expense ID": 110, "Title": "Medicine", "Category": "Health", "Amount": 2200.0},
    {"Expense ID": 111, "Title": "Gym Fee", "Category": "Health", "Amount": 3000.0},
    {"Expense ID": 112, "Title": "Coffee", "Category": "Food", "Amount": 650.0},
    {"Expense ID": 113, "Title": "Laptop Repair", "Category": "Electronics", "Amount": 8500.0},
    {"Expense ID": 114, "Title": "Clothes", "Category": "Shopping", "Amount": 7200.0},
    {"Expense ID": 115, "Title": "Shoes", "Category": "Shopping", "Amount": 4800.0},
    {"Expense ID": 116, "Title": "Streaming Subscription", "Category": "Entertainment", "Amount": 900.0},
    {"Expense ID": 117, "Title": "Stationery", "Category": "Education", "Amount": 1100.0},
    {"Expense ID": 118, "Title": "Water Bill", "Category": "Bills", "Amount": 1400.0},
    {"Expense ID": 119, "Title": "Gift", "Category": "Miscellaneous", "Amount": 2600.0},
    {"Expense ID": 120, "Title": "Taxi", "Category": "Transport", "Amount": 1500.0}
]

# ----------------  FUNCTIONS:   ----------------

def add_expense():
    try:
        expense_id = int(input("Enter the Expense ID: "))
    except ValueError:
        print("Invalid Expense ID! Please enter a number.")
        return
    if expense_id <= 0:
        print("Enter a valid Expense ID!")
        return

    for expense in expenses:
        if expense["Expense ID"] == expense_id:
            print("Expense ID already exists!")
            return

    Title = input("Enter the Expense Title: ")
    Category = input("Enter the Expense Category: ")

    try:
        amount = float(input("Enter the amount: "))
        if amount <=0:
            print("Amount must be a positive number!")
            return
    except ValueError:
        print("Invalid Amount! Please enter a number.")
        return   

    Title = Title.strip()
    Category = Category.strip()

    if Title == "":
        print("Expense Title cannot be empty!")
        return

    if Category == "":
        print("Category cannot be empty!")
        return

    new_expense = {
        "Title": Title,
        "Category": Category,
        "Expense ID": expense_id,
        "Amount": amount,
    }

    expenses.append(new_expense)
    print("New Expense Added Successfully!")

def view_expense():
    if len(expenses) == 0:
        print("No Expenses in record!")
        return
    for expense in expenses:
            print("---------------------------------------------------")
            print("Title:", expense["Title"])
            print("Category:", expense["Category"])
            print("Expense ID:", expense["Expense ID"])
            print("Amount:", expense["Amount"])
            print("---------------------------------------------------")

def search_expense():
    try:
        search = int(input("Enter the Expense ID: "))
    except ValueError:
        print("Invalid Expense ID! Please enter a number.")
        return

    found = False
    for expense in expenses:
        if expense["Expense ID"] == search:
            print("---------------------------------------------------")
            print("Title:", expense["Title"])
            print("Category:", expense["Category"])
            print("Expense ID:", expense["Expense ID"])
            print("Amount:", expense["Amount"])
            print("---------------------------------------------------")
            found = True
            break
    if not found:
        print("Expense Not Found!")

def update_expense():
    try:
        search = int(input("Enter the Expense ID: "))
    except ValueError:
        print("Invalid Expense ID! Please enter a number.")
        return

    found = False
    for expense in expenses:
        if expense["Expense ID"] == search:
            print("---------------------------------------------------")
            print("Title:", expense["Title"])
            print("Category:", expense["Category"])
            print("Expense ID:", expense["Expense ID"])
            print("Amount:", expense["Amount"])
            print("---------------------------------------------------")

            Title = input("Enter the new Expense name (leave blank to keep current): ")
            Category= input("Enter the new Category name (leave blank to keep current): ")
            amount_input = input("Enter the new expense amount (leave blank to keep current): ")

            if Title.strip():
                expense["Title"] = Title.strip()
            if Category.strip():
                expense["Category"] = Category.strip()
            if amount_input.strip():
                try:
                    amount_input = float(amount_input)
                    if amount_input <= 0:
                        print("Amount must be a positive number! Keeping current amount.")
                    else:
                        expense["Amount"] = amount_input
                except ValueError:
                    print("Invalid Amount! Keeping current amount.")
            print("Expense Updated Successfully!")
            found = True
            break
    if not found:
        print("Expense Not Found!")

def delete_expense():
    try:
        search = int(input("Enter the Expense ID: "))
    except ValueError:
        print("Invalid Expense ID! Please enter a number.")
        return

    found = False
    for expense in expenses:
        if expense["Expense ID"] == search:
            confirm = input(f"Are you sure you want to delete expense {expense['Title']}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            expenses.remove(expense)
            print("Expense Deleted Successfully!")
            found = True
            break
    if not found:
        print("Expense Not Found!")

def total_expense():
    if len(expenses) == 0:
        print("No Expenses in record!")
        return
    total = sum(expense["Amount"] for expense in expenses)
    print("---------------------------------------------------")
    print("Total Expenses: ", total)
    print("---------------------------------------------------")

def highest_expense():
    if len(expenses) == 0:
        print("No Expenses in record!")
        return
    highest = max(expenses, key=lambda x: x["Amount"])
    print("---------------------------------------------------")
    print("Highest Expense:")
    print("Title:", highest["Title"])
    print("Category:", highest["Category"])
    print("Expense ID:", highest["Expense ID"])
    print("Amount:", highest["Amount"])
    print("---------------------------------------------------")

def lowest_expense():
    if len(expenses) == 0:
        print("No Expenses in record!")
        return
    lowest = min(expenses, key=lambda x: x["Amount"])
    print("---------------------------------------------------")
    print("Lowest Expense:")
    print("Title:", lowest["Title"])
    print("Category:", lowest["Category"])
    print("Expense ID:", lowest["Expense ID"])
    print("Amount:", lowest["Amount"])
    print("---------------------------------------------------")

def exit_system():
    print("---------------------------------------------------")
    print("Exiting the Expense Tracker.")
    print("Thank you for using the system. Goodbye!")
    print("---------------------------------------------------")
    import sys
    sys.exit()

# ----------------  MENU  ----------------
while True:
    print()
    print("=============== Select the Option (0-8) ===============")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Total Expenses")
    print("7. Highest Expense")
    print("8. Lowest Expense")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        search_expense()
    elif choice == 4:
        update_expense()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        total_expense()
    elif choice == 7:
        highest_expense()
    elif choice == 8:
        lowest_expense()
    elif choice == 0:
        exit_system()
    else:
        print("Invalid Choice! Choose between 0 to 8")

