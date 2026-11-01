import datetime as dt
import expense_utils as eu
from report_utils import build_monthly_report, save_report


def get_expense_date():
    date_text = input("Enter date (YYYY-MM-DD, blank for today): ").strip()
    if date_text == "":
        return dt.date.today()
    try:
        return dt.datetime.strptime(date_text, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None


def add_expense(expenses):
    print("\nEnter Expense Details")
    description = input("Enter description: ").strip()
    category = input("Enter category (Food/Travel/Study/Bills/Other): ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense_date = get_expense_date()
    if expense_date is None:
        return

    if not eu.validate_expense(description, category, amount, expense_date):
        print("Invalid expense. Description and category are required, and amount must be positive.")
        return

    reference_id = eu.generate_reference_id(expenses)
    expense = {
        "reference_id": reference_id,
        "date": expense_date,
        "description": description,
        "category": category.title(),
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully.")
    print("Reference ID:", reference_id)


def show_current_month_report(expenses):
    today = dt.date.today()
    report = build_monthly_report(expenses, today.year, today.month)
    print("\n" + report)

    choice = input("\nDo you want to save this report? (y/n): ").strip().lower()
    if choice == "y":
        file_path = save_report(report, today.year, today.month)
        print("Report saved to:", file_path)


def main():
    expenses = []
    print("=" * 35)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 35)

    while True:
        print("\n1. Add expense")
        print("2. View current month's report")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses have been recorded yet.")
            else:
                show_current_month_report(expenses)
        elif choice == "3":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
