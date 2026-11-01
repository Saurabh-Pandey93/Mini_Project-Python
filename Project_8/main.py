from models import Book, Magazine, ReferenceBook, StudentMember, FacultyMember, ResearchStudent, NotifiedMember, Member
from library_services import LibraryManager
from Storage import save_data, load_data

def main():
    mgr = LibraryManager()
    load_data(mgr)

    # Preload for demo to cover all OOP types
    if not mgr.items:
        mgr.register_item(Book("B201", "Python Basics", "Aman"))
        mgr.register_item(Magazine("M301", "Tech Monthly"))
        mgr.register_item(ReferenceBook("R401", "Encyclopedia"))

    if not mgr.members:
        mgr.register_member(StudentMember("S101", "Riya"))
        mgr.register_member(FacultyMember("F101", "Dr. Sharma"))
        mgr.register_member(ResearchStudent("RS101", "Kabir"))
        mgr.register_member(NotifiedMember("N101", "Neha")) # Multiple inheritance demo

    while True:
        print("\n1.Register item 2.Register member 3.Borrow 4.Return 5.Reports 6.Exit")
        ch = input("Choice: ").strip()
        try:
            if ch == "1":
                iid = input("Item ID: "); title = input("Title: ")
                t = input("Type (Book/Magazine/ReferenceBook): ").lower()
                if t == "book": mgr.register_item(Book(iid, title))
                elif t == "magazine": mgr.register_item(Magazine(iid, title))
                else: mgr.register_item(ReferenceBook(iid, title))
            elif ch == "2":
                mid = input("Member ID: "); name = input("Name: ")
                t = input("Type (Student/Faculty/Research/Notified): ").lower()
                if t == "faculty": mgr.register_member(FacultyMember(mid, name))
                elif t == "research": mgr.register_member(ResearchStudent(mid, name))
                elif t == "notified": mgr.register_member(NotifiedMember(mid, name))
                else: mgr.register_member(StudentMember(mid, name))
            elif ch == "3":
                mid = input("Member ID: "); iid = input("Item ID: ")
                mgr.borrow_item(mid, iid)
            elif ch == "4":
                iid = input("Item ID: "); mgr.return_item(iid)
            elif ch == "5":
                mgr.reports()
            elif ch == "6":
                save_data(mgr); print("Bye"); break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()