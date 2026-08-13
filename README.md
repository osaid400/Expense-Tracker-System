# Expense Tracker System

A console-based personal Expense Tracker built with Python using Object-Oriented Programming (OOP) principles. It goes beyond simple expense logging with genuinely month-aware budgeting, flexible analytics (overall vs. specific-month), and exportable monthly reports — all backed by JSON persistence and a modular package structure.

---

## Features

* **Expense Management:**
  * Add Expense (with auto category normalization and duplicate-ID protection)
  * View Expenses (Overall / Per Year / Per Month)
  * Search Expense (by ID, Title, or Category)
  * Update Expense
  * Delete Expense

* **Budgeting:**
  * Set / Check Monthly Budget
  * Real-time warning when adding an expense would exceed **the current month's** budget (not lifetime spending)

* **Analytics:**
  * Highest Expense — Highest Single Transaction (overall), Highest Spending Month (overall), or Highest Expense in a Specific Month
  * Lowest Expense — same three views as above
  * Average Expense — Overall Monthly Average or Average Per Transaction
  * Category-wise Summary (with totals per category)
  * Total Expenses (all-time)

* **Reporting:**
  * Generate Monthly Report (`.txt`) — Budget Overview, Category Breakdown with percentages, Top 3 Expenses of the month, and a clean transaction list

* **Data Features:**
  * Persistent JSON Storage for expenses and budget
  * Category input normalization (`.strip().capitalize()`) to prevent duplicate categories like `"food"` vs `"Food"`
  * Input validation and exception handling throughout, including corrupt-JSON recovery

---

## Technologies Used

* **Python 3** (Object-Oriented Programming)
* **JSON Module** (Data persistence)
* **Datetime Module** (Date validation, monthly filtering, report generation)
* **OS Module** (Directory and file handling)

---

## Project Structure

```text
Expense-Tracker-System/
│
├── data/
│   ├── expenses.json          # Persistent expense records (gitignored)
│   └── budget.json            # Persistent monthly budget (gitignored)
│
├── Reports/                    # Auto-generated monthly reports (gitignored)
│
├── src/                        # Source code package
│   ├── __init__.py
│   ├── models.py                 # Expense class — attributes, to_dict(), from_dict()
│   ├── manager.py                  # Expense_Manager class — persistence, filtering, analytics, report generation
│   └── UI.py                       # Menu loop and display formatting
│
├── .gitignore                  # Excludes __pycache__, Reports, and local data
├── main.py                     # Application entry point
└── README.md
```

> **Note:** `data/expenses.json` and `data/budget.json` are created automatically on first run with sample data and a default budget. They store expense records and budget locally and are excluded from the repository via `.gitignore`.

---

## How to Run

Clone the repository

```bash
git clone https://github.com/osaid400/Expense-Tracker-System.git
```

Move into the project folder

```bash
cd Expense-Tracker-System
```

Run the program

```bash
python main.py
```

---

## Example Outputs

### Main Menu

```text
============ Welcome to Expense Tracker SYSTEM =============

=============== Select the Option (0-12) ================
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Total Expenses
7. Highest Expense Analytics
8. Lowest Expense Analytics
9. Average Expense Analytics
10. Category-wise Summary
11. Set / Check Monthly Budget
12. Generate Monthly Report
0. Exit
=========================================================
```

### Adding an Expense (Budget Warning)

```text
Enter the Expense ID: 361
Enter the Expense Title: Guest Dinner
Enter the Expense Category: food
Enter the amount: 8500
Enter date (DD-MM-YYYY) [Leave blank for today]:

⚠️ WARNING: Adding this expense exceeds your monthly budget of Rs. 50,000!
New Expense Added Successfully!
```

### View Expenses (Per Month)

```text
View Options:
1. Overall Expenses
2. View Per Year
3. View Per Month
Enter your choice (1-3): 3
Enter Year (e.g., 2026): 2026
Enter Month (1-12): 7

------------------------------- Expenses for 07/2026 ------------------------------
===================================================================================
Expense ID   Title                Category           Amount             Date
===================================================================================
349          Lab Test             Health             Rs. 1,150          01-07-2026
350          Cleaning Supplies    Household          Rs. 4,549          04-07-2026
351          Petrol               Fuel               Rs. 6,100          09-07-2026
352          Eid Shopping         Miscellaneous      Rs. 9,450          12-07-2026
===================================================================================
Total Amount: Rs. 21,249
Total Years: 1 (2026)
Total Months: 1
```

### Search Expense

```text
Search By:
1. Search by ID
2. Search by Title
3. Search by Category
Enter your choice: 3
Enter the Expense Category: fuel

===================================================================================
Expense ID   Title                Category           Amount             Date
===================================================================================
351          Petrol               Fuel               Rs. 6,100          09-07-2026
360          Petrol               Fuel               Rs. 4,850          28-07-2026
===================================================================================
```

### Update Expense

```text
Enter the Expense ID: 350
Current Details:
===================================================================================
Expense ID   Title                Category           Amount             Date
===================================================================================
350          Cleaning Supplies    Household          Rs. 4,549          04-07-2026
===================================================================================
Enter new title (leave blank to keep current):
Enter new category (leave blank to keep current):
Enter new amount (leave blank to keep current): 4200
Enter new date DD-MM-YYYY (leave blank to keep current):
Expense Updated Successfully!
```

### Category-wise Summary

```text
==================================================
Category                       Total Amount
==================================================
Health                          Rs. 1,150
Household                       Rs. 4,549
Fuel                            Rs. 10,950
Miscellaneous                   Rs. 17,349
Food                            Rs. 2,450
Transport                       Rs. 1,049
Bills                           Rs. 8,700
Personal care                   Rs. 1,150
==================================================
```

### Average Expense Analytics

```text
Average Expense Options:
1. Overall Monthly Average
2. Average Per Transaction
Enter choice (1-2): 1

--------------------------------------------------
Average Monthly Expense: Rs. 41,732
--------------------------------------------------
```

### Highest Expense Analytics

```text
Highest Expense Options:
1. Highest Single Transaction (Overall)
2. Highest Spending Month (Overall)
3. Highest Expense in a Specific Month
Enter choice (1-3): 3
Enter Year (e.g., 2026): 2026
Enter Month (1-12): 7

----------------------------- Highest Expense for 07/2026 ------------------------------
Expense ID   Title                Category           Amount             Date
========================================================================================
352          Eid Shopping         Miscellaneous      Rs. 9,450          12-07-2026
========================================================================================
```

### Monthly Report (`.txt` output)

```text
=====================================================
              MONTHLY EXPENSE REPORT
                    July 2026
=====================================================
Generated On: 13-08-2026
-----------------------------------------------------
BUDGET OVERVIEW
-----------------------------------------------------
Monthly Budget    : Rs. 50,000
Total Spent       : Rs. 47,298
Remaining/Exceeded: Rs. 2,702 remaining (94.6% used)
-----------------------------------------------------
-----------------------------------------------------
CATEGORY BREAKDOWN
-----------------------------------------------------
Category         Amount        % of Total
Health            1,150          2.4%
Household         4,549          9.6%
Fuel             10,950         23.1%
Miscellaneous    17,349         36.6%
Food              2,450          5.2%
Transport         1,049          2.2%
Bills             8,700         18.4%
Personal care     1,150          2.4%
-----------------------------------------------------
-----------------------------------------------------
TOP 3 EXPENSES THIS MONTH
-----------------------------------------------------
1. Eid Shopping           Rs. 9,450    12-07-2026
2. Gas Bill               Rs. 6,600    19-07-2026
3. Petrol                 Rs. 6,100    09-07-2026
-----------------------------------------------------
-----------------------------------------------------
ALL TRANSACTIONS
-----------------------------------------------------
Title                Amount             Date
Lab Test             Rs. 1,150          01-07-2026
Cleaning Supplies    Rs. 4,549          04-07-2026
Petrol               Rs. 6,100          09-07-2026
Eid Shopping          Rs. 9,450          12-07-2026
=====================================================
```

---

## Concepts Covered

* **Object-Oriented Programming (OOP):** Class design (`Expense`, `Expense_Manager`), with `to_dict()` / `from_dict()` serialization using safe `.get()` defaults.
* **CRUD Operations:** Full expense lifecycle — add, search, update, delete.
* **JSON Data Serialization:** Persistent storage for both expenses and budget, with corrupt-file recovery.
* **Date-Aware Business Logic:** A reusable `_filter_by_month()` helper drives budget checks, monthly analytics, and report generation — replacing what was originally repeated date-filtering logic across multiple methods.
* **Data Normalization:** Category input consistently normalized to avoid duplicate categories from casing differences.
* **Reporting:** Generating structured `.txt` reports (budget overview, percentage breakdowns, top expenses, transaction list) designed after real-world statement formats.
* **Modules & Packages:** Code organized into a `src/` package (`models.py`, `manager.py`, `UI.py`), separating data, business logic, and presentation, with `main.py` as the entry point outside the package.
* **Defensive Programming:** Input validation and exception handling (`try`/`except`) across all menus and date parsing.

---

## How the Monthly Budget Check Works

* The budget is a **monthly** figure, so the check when adding an expense only sums **that expense's month's** existing total — not all-time spending — before comparing to the budget.
* This distinction matters: an app that compared lifetime totals to a "monthly" budget would eventually warn on every single expense, regardless of how much was actually spent that month.

## How Analytics Handle "Overall" vs. "Specific Month"

* Highest/Lowest/Average Expense each offer both an overall view and a month-specific view, since both are genuinely useful for different questions ("what was my single biggest purchase ever?" vs. "what was my highest expense last March?").
* All month-specific filtering goes through one shared helper (`_filter_by_month()`), so the filtering logic exists in exactly one place.

---

## Future Improvements

* **Per-category budgets** — separate limits for Food, Bills, etc., instead of one overall monthly budget, so overspending in a single category can be caught early.
* **Recurring/fixed monthly expenses** — mark an expense (rent, subscriptions) as recurring so it can be auto-suggested or auto-logged each month instead of re-entered manually.
* **Early warning threshold** — alert at, say, 80% of the budget used, rather than only after it's fully exceeded.
* **CSV export** — export expenses and reports to `.csv` for use in Excel/Sheets, in addition to the current `.txt` reports.
* **SQLite integration** — replace JSON persistence with a proper relational database as the dataset grows.
* **Graphical User Interface (Tkinter)** — a visual dashboard instead of a console menu, including simple charts for category breakdowns.
* **Multi-currency support** — track expenses in more than one currency with conversion.
* **Report for a custom date range** — currently reports are month-based; a "from date to date" option would allow arbitrary ranges (e.g., a quarter or a trip's duration).

---

## Learning Outcomes

This project helped me practice and solidify key software engineering concepts:

* **Getting "monthly" logic actually right:** Catching and fixing a real bug where a budget check and analytics compared lifetime totals instead of monthly ones — a good lesson in matching a feature's name to what it actually calculates.
* **DRY refactoring:** Consolidating repeated date-filtering code across multiple methods into a single `_filter_by_month()` helper.
* **Designing for real-world usability:** Iterating from "just show the numbers" to a report structure (summary first, then breakdown, then detail) modeled on how real bank/credit-card statements are laid out.
* **Modular project structure:** Splitting a single-file project into a `models` / `manager` / `UI` / `main` package, and deciding which parts of input-heavy methods belong in the manager versus the UI layer.

---

## Author

**Muhammad Abdullah Farooq**

GitHub: [https://github.com/osaid400](https://github.com/osaid400)