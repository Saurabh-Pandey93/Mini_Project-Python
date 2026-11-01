from datetime import datetime, timedelta
from models import ReferenceBook

class LibraryManager:
    def __init__(self):
        self.items = {}   # id -> LibraryItem
        self.members = {} # id -> Member
        self.loans = {}   # item_id -> {member_id, issue_date, due_date}

    def register_item(self, item):
        if item.item_id in self.items:
            raise ValueError(f"Duplicate Item ID {item.item_id}")
        self.items[item.item_id] = item
        print(f"Item registered: {item.item_id}")

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError(f"Duplicate Member ID {member.member_id}")
        self.members[member.member_id] = member
        print(f"Member registered: {member.member_id}")

    def borrow_item(self, member_id, item_id):
        if member_id not in self.members: raise ValueError("Member not found")
        if item_id not in self.items: raise ValueError("Item not found")
        
        item = self.items[item_id]
        member = self.members[member_id]

        if not item.is_available: raise ValueError("Item not available")
        if isinstance(item, ReferenceBook): raise ValueError("ReferenceBook cannot be borrowed")
        if not member.can_borrow(): raise ValueError("Member limit exceeded")

        # Polymorphic call - no type checking
        days = item.loan_period_days()
        issue = datetime.now()
        due = issue + timedelta(days=days)

        self.loans[item_id] = {"member_id": member_id, "issue_date": issue.isoformat(), "due_date": due.isoformat()}
        item._is_available = False
        member._active_loans.append(item_id)

        if hasattr(member, 'send_notice'):
            member.send_notice(f"{item_id} issued, Due: {due.date()}")

        print(f"Borrow successful: {item_id} issued to {member_id} Due: {due.date()}")
        return due

    def return_item(self, item_id):
        if item_id not in self.loans: raise ValueError("Item not on loan")
        loan = self.loans.pop(item_id)
        member = self.members[loan["member_id"]]
        item = self.items[item_id]
        
        item._is_available = True
        if item_id in member._active_loans:
            member._active_loans.remove(item_id)

        overdue, fine = self.calculate_fine(loan["due_date"])
        print(f"Return successful. Overdue: {overdue} days, Fine: Rs.{fine}")
        return overdue, fine

    @staticmethod
    def calculate_fine(due_date_str):
        due = datetime.fromisoformat(due_date_str)
        now = datetime.now()
        overdue = (now - due).days
        overdue = max(0, overdue)
        return overdue, overdue * 10 # Rs 10 per day

    def reports(self):
        print("\n--- All Items ---")
        for i in self.items.values(): print(f"{i.item_id} | {i.title} | Available: {i.is_available} | LoanDays: {i.loan_period_days()}")
        print("\n--- Active Loans ---")
        for item_id, l in self.loans.items(): print(f"{item_id} | {l['member_id']} | Due: {l['due_date'][:10]}")
        print("\n--- Overdue Loans ---")
        for item_id, l in self.loans.items():
            od, _ = self.calculate_fine(l["due_date"])
            if od > 0: print(f"{item_id} overdue by {od} days")