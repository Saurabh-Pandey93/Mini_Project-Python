import json
from models import Book, Magazine, ReferenceBook, StudentMember, FacultyMember, ResearchStudent, NotifiedMember

ITEM_MAP = {"Book": Book, "Magazine": Magazine, "ReferenceBook": ReferenceBook}
MEMBER_MAP = {"StudentMember": StudentMember, "FacultyMember": FacultyMember, "ResearchStudent": ResearchStudent, "NotifiedMember": NotifiedMember}

def save_data(manager, path="data.json"):
    try:
        data = {
            "items": [v.to_dict() for v in manager.items.values()],
            "members": [v.to_dict() for v in manager.members.values()],
            "loans": manager.loans
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {path}")
    except OSError as e:
        print(f"Save failed: {e}")

def load_data(manager, path="data.json"):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No previous data found, starting fresh")
        return
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}")
        return
    
    try:
        for d in data.get("items", []):
            cls = ITEM_MAP.get(d["type"])
            if not cls: continue
            obj = cls(d["item_id"], d["title"]) if d["type"] != "Book" else cls(d["item_id"], d["title"], d.get("author",""))
            obj._is_available = d.get("is_available", True)
            manager.items[obj.item_id] = obj
        
        for d in data.get("members", []):
            cls = MEMBER_MAP.get(d["type"])
            if not cls: continue
            obj = cls(d["member_id"], d["name"])
            obj._active_loans = d.get("active", [])
            manager.members[obj.member_id] = obj
        
        manager.loans = data.get("loans", {})
        print(f"Data loaded from {path}")
    except (KeyError, TypeError, ValueError) as e:
        print(f"Data corrupted: {e}")