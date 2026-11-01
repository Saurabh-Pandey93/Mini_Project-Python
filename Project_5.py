import random
import math
import datetime as dt


def validate_expense(description, category, amount, expense_date):
    if not isinstance(description, str) or not description.strip():
        return False
    if not isinstance(category, str) or not category.strip():
        return False
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return False
    if amount <= 0:
        return False
    if not isinstance(expense_date, dt.date):
        return False
    return True


def generate_reference_id(expenses):
    # This is a convenience ID, not a secure identifier.
    while True:
        reference_id = "EXP-" + str(random.randint(100000, 999999))
        existing_ids = [expense["reference_id"] for expense in expenses]
        if reference_id not in existing_ids:
            return reference_id


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return math.floor(total * 100 + 0.5) / 100


def category_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    for category in totals:
        totals[category] = math.floor(totals[category] * 100 + 0.5) / 100
    return totals


def filter_expenses_by_month(expenses, year, month):
    monthly_expenses = []
    for expense in expenses:
        expense_date = expense["date"]
        if expense_date.year == year and expense_date.month == month:
            monthly_expenses.append(expense)
    return monthly_expenses
