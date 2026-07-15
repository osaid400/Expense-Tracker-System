# Expense Tracker System

A beginner-friendly console-based Expense Tracker built with Python. This project demonstrates the use of JSON file handling, CRUD operations, searching, data analysis, and menu-driven programming to manage personal expenses.

---

## Features

* Add a new expense
* View all expenses
* Search expenses by Expense ID
* Search expenses by Category
* Update expense details
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

---

## Concepts Covered

* Functions
* Lists
* Dictionaries
* JSON File Handling
* File Read/Write
* CRUD Operations
* Loops
* Conditional Statements
* Input Validation
* Exception Handling (`try` / `except`)
* Searching
* Data Analysis

---

## Project Structure

```text
Expense-Tracker-System/
│
├── expense_tracker.py
├── expenses.json
├── .gitignore
└── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/osaid400/Expense-Tracker-System.git
```

2. Navigate to the project folder.

```bash
cd Expense-Tracker-System
```

3. Run the program.

```bash
python expense_tracker.py
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

---

### View Expenses

```text
==============================================================================================================
Expense ID          Title                    Category                  Amount
==============================================================================================================
101                 Groceries                Food                      Rs. 3,500.0
102                 Bus Fare                 Transport                 Rs. 800.0
103                 Electricity Bill         Bills                     Rs. 5,200.0
==============================================================================================================
```

---

### Search Expense

```text
Search By:
1. Search by ID
2. Search by Category

Enter your choice: 2
Enter the Expense Category: Food

==============================================================================================================
Expense ID          Title                    Category                  Amount
==============================================================================================================
101                 Groceries                Food                      Rs. 3,500.0
107                 Restaurant               Food                      Rs. 2,700.0
112                 Coffee                   Food                      Rs. 650.0
==============================================================================================================
```

---

### Add Expense

```text
Enter the Expense ID: 121
Enter the Expense Title: Printer Ink
Enter the Expense Category: Office
Enter the amount: 2500

New Expense Added Successfully!
```

---

### Expense Summary

```text
---------------------------------------------------
Total Expenses: Rs. 62,350.0
---------------------------------------------------

---------------------------------------------------
Average Expense: Rs. 3,117.5
---------------------------------------------------
```

---

### Highest Expense

```text
Highest Expense

Expense ID          Title                    Category                  Amount
113                 Laptop Repair            Electronics               Rs. 8,500.0
```

---

### Lowest Expense

```text
Lowest Expense

Expense ID          Title                    Category                  Amount
112                 Coffee                   Food                      Rs. 650.0
```

---

## Future Improvements

* Monthly expense reports
* Search by Title
* Filter expenses by amount range
* Expense statistics by category
* Export reports to CSV
* Date and time for each expense
* Budget tracking
* SQLite database integration
* Object-Oriented Programming (OOP) version

---

## Learning Outcomes

This project helped me practice:

* Building menu-driven console applications
* Managing structured data using JSON
* CRUD operations
* Searching records
* Data analysis using Python
* File handling
* Input validation
* Writing clean and reusable functions

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
