from abc import ABC, abstractmethod
from datetime import datetime

# ---- Abstract Base Class ----
class LibraryItem(ABC):
    library_name = "Central Library"  # Class attribute

    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self._is_available = True # Encapsulation - protected

    @property
    def is_available(self):
        return self._is_available

    @abstractmethod
    def loan_period_days(self):
        pass

    def to_dict(self):
        return {"type": self.__class__.__name__, "item_id": self.item_id, 
                "title": self.title, "is_available": self._is_available}

# Single Inheritance
class Book(LibraryItem):
    def __init__(self, item_id, title, author=""):
        super().__init__(item_id, title)
        self.author = author
    
    def loan_period_days(self): # Overriding + Polymorphism
        return 14

    def to_dict(self):
        d = super().to_dict(); d["author"] = self.author; return d

class Magazine(LibraryItem):
    def loan_period_days(self):
        return 7

# ReferenceBook -> zero day, not lendable
class ReferenceBook(LibraryItem):
    def loan_period_days(self):
        return 0

# ---- Member Hierarchy ----
class Member:
    max_active_loans_default = 3 # Class attribute

    def __init__(self, member_id, name, borrowing_limit=None):
        self.member_id = member_id
        self.name = name
        self.borrowing_limit = borrowing_limit or Member.max_active_loans_default
        self._active_loans = [] # Encapsulated

    @property
    def active_loans_count(self):
        return len(self._active_loans)

    @classmethod
    def set_policy(cls, new_limit):
        cls.max_active_loans_default = new_limit

    def can_borrow(self):
        return self.active_loans_count < self.borrowing_limit

    def to_dict(self):
        return {"type": self.__class__.__name__, "member_id": self.member_id, 
                "name": self.name, "limit": self.borrowing_limit, "active": self._active_loans}

# Hierarchical Inheritance
class StudentMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, borrowing_limit=3)

class FacultyMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, borrowing_limit=5)

# Multilevel Inheritance: ResearchStudent -> StudentMember -> Member
class ResearchStudent(StudentMember):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.borrowing_limit = 4

# Multiple Inheritance Demo
class NotificationMixin:
    def send_notice(self, message):
        print(f"[NOTICE to {self.name}]: {message}")

# MRO: NotifiedMember -> Member first, then NotificationMixin
# MRO Order: NotifiedMember, StudentMember, Member, NotificationMixin, object
class NotifiedMember(StudentMember, NotificationMixin):
    pass