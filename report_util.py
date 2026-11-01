import datetime as dt
import os
from tabulate import tabulate
import expense_utils as eu


def build_monthly_report(expenses, year, month):
    monthly_expenses = eu.filter_expenses_by_month(expenses, year, month)
    month_name = dt.date(year, month, 1).strftime("%B %Y")

    rows = []
    for expense in monthly_expenses:
        rows.append([
            expense["reference_id"],
            expense["date"].strftime("%Y-%m-%d"),
            expense["description"],
            expense["category"],
            f"{expense['amount']:.2f}"
        ])

    report = ["----- MONTHLY EXPENSE REPORT -----", "Report month: " + month_name]

    if rows:
        table = tabulate(
            rows,
            headers=["Reference ID", "Date", "Description", "Category", "Amount"],
            tablefmt="grid"
        )
        report.append(table)
    else:
        report.append("No expenses found for this month.")

    report.append(f"Total spending: {eu.calculate_total(monthly_expenses):.2f}")

    totals_by_category = eu.category_totals(monthly_expenses)
    if totals_by_category:
        report.append("\nCategory totals:")
        for category, amount in totals_by_category.items():
            report.append(f"{category} total: {amount:.2f}")

    return "\n".join(report)


def save_report(report_text, year, month):
    folder_path = os.path.join(os.path.dirname(__file__), "reports")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = f"expense_report_{year}_{month:02d}.txt"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print("A report for this month already exists. It will be updated.")

    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

    return file_path
