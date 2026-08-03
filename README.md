# Expense Tracker System

A console-based **Expense Tracker System** built with Python using **Object-Oriented Programming (OOP)**. This project demonstrates clean class design, automatic timestamping, JSON-based data persistence, CRUD operations, and expense analysis.

---

## Features

* Add a new expense (automatically timestamped)
* View all expenses (auto-sorted by Expense ID)
* Search expenses by:
  * Expense ID
  * Title
  * Category
* Update expense details (leave a field blank to keep its current value)
* Delete expenses with confirmation
* Calculate total expenses
* Display highest expense
* Display lowest expense
* Calculate average expense
* Prevent duplicate Expense IDs
* Store records using JSON
* Automatically sort expenses by Expense ID

---

## Technologies Used

* Python 3
* JSON
* `datetime` Module

---

## Concepts Covered

* Object-Oriented Programming (OOP)
* Classes & Objects (`Expense`, `Expense_Manager`)
* Constructors (`__init__`)
* Class Methods (`@classmethod`) — `from_dict()`
* Static Methods (`@staticmethod`) — `format_currency()`
* Object Serialization (`to_dict()` / `from_dict()`)
* Automatic Timestamping with `datetime`
* JSON File Handling
* CRUD Operations
* Exception Handling
* Input Validation
* Menu-Driven Applications

---

## Project Structure

```text
Expense-Tracker-System/
│
├── Expense Tracker.py
├── .gitignore
└── README.md
```

> **Note:** `expenses.json` is created automatically when the program runs. It stores expense records locally and is excluded from the repository via `.gitignore` because it contains runtime data rather than source code.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/Expense-Tracker-System.git
```

2. Navigate to the project folder:

```bash
cd Expense-Tracker-System
```

3. Run the program:

```bash
python "Expense Tracker.py"
```

---

## Example Output

### Main Menu

```text
=============== Select the Option (0-9) ===============
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Total Expenses
7. Highest Expense
8. Lowest Expense
9. Average Expense
0. Exit
========================================================
```

### View Expenses

```text
==========================================================================================================================
Expense ID           Title                    Category                     Amount                    Date and Time
==========================================================================================================================

101                  Groceries                Food                         Rs. 3,500                2023-03-01 12:00:00
102                  Bus Fare                 Transport                    Rs. 800                  2023-03-02 08:00:00
103                  Electricity Bill         Bills                        Rs. 5,200                2023-03-03 10:00:00
==========================================================================================================================

```

### Add Expense

```text
Enter the Expense ID: 121
Enter the Expense Title: Printer Ink
Enter the Expense Category: Office

Enter the amount: 2500

New Expense Added Successfully!
```

### Search Expense

```text
Search By:
1. Search by ID
2. Search by Title
3. Search by Category
Enter your choice: 3
Enter the Expense Category: Food

=============================================================================================================================
Expense ID           Title                    Category                     Amount                    Date and Time
============================================================================================================================
101                  Groceries                Food                         Rs. 3,500                2023-03-01 12:00:00
107                  Restaurant               Food                         Rs. 2,700                2023-03-07 19:00:00
112                  Coffee                   Food                         Rs. 650                  2023-03-12 10:00:00
=============================================================================================================================
```

### Expense Summary

```text
---------------------------------------------------
Total Expenses: Rs. 62,350
---------------------------------------------------

---------------------------------------------------
Average Expense: Rs. 3,118
---------------------------------------------------
```

### Highest / Lowest Expense

```text
----------------------------------------------- Highest Expense ----------------------------------------------
Expense ID           Title                    Category                     Amount                    Date and Time
113                  Laptop Repair            Electronics                  Rs. 8,500                2023-03-13 13:00:00
```

---

## How Data Persistence Works

* On startup, the program checks whether `expenses.json` exists.
* If the file exists, all expense records are loaded and converted into `Expense` objects.
* If it doesn't exist, a default set of sample expenses is created and saved.
* Every expense is automatically stamped with the date and time it was added.
* Every time an expense is added, updated, or deleted, the full expense list is saved back to `expenses.json`.

---

## Future Improvements

* Monthly expense reports
* Filter expenses by amount range
* Expense statistics broken down by category
* Export reports to CSV
* Budget tracking with alerts
* SQLite database integration
* Build a GUI version using Tkinter

---

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Creating reusable classes and methods (`@classmethod`, `@staticmethod`)
* Managing persistent data using JSON
* Working with the `datetime` module for automatic timestamping
* Performing CRUD (Create, Read, Update, Delete) operations
* Analyzing data (totals, highest, lowest, average)
* Validating user input and handling exceptions
* Building structured, menu-driven console applications

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400