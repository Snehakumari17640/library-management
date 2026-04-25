import datetime

library = {}  

# ADD BOOK
def add_book():
    name = input("Enter book name: ").strip()
    if name in library:
        print(" Book already exists.")
    else:
        library[name] = {
            "available": True,
            "issued_to": "",
            "issue_date": None,
            "days": 0
        }
        print("Book added successfully!")

# SHOW BOOKS
def show_books():
    if not library:
        print("No books in library.")
    else:
        print("\n Library Books:")
        for book, info in library.items():
            status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
            print(f"- {book} → {status}")

# ISSUE BOOK
def issue_book():
    name = input("Enter book name to issue: ").strip()
    
    if name not in library:
        print("Book not found.")
        return
    
    if not library[name]["available"]:
        print("Book already issued.")
        return
    
    student = input("Enter student name: ")
    days = int(input("Enter number of days: "))
    
    library[name]["available"] = False
    library[name]["issued_to"] = student
    library[name]["issue_date"] = datetime.date.today()
    library[name]["days"] = days
    
    print("Book issued successfully!")
    print(" Note: Late return will include fine charges.")

# CALCULATE FINE
def calculate_fine(days_late):
    fine = 0
    for i in range(1, days_late + 1):
        week = (i // 7) + 1
        rate = 10
        for j in range(1, week + 1):
            rate *= j
        fine += rate
    return fine

# RETURN BOOK
def return_book():
    name = input("Enter book name to return: ").strip()
    
    if name not in library:
        print("Book not found.")
        return
    
    if library[name]["available"]:
        print("Book was not issued.")
        return
    
    issue_date = library[name]["issue_date"]
    allowed_days = library[name]["days"]
    
    today = datetime.date.today()
    used_days = (today - issue_date).days
    
    if used_days <= allowed_days:
        print(" Book returned on time. No fine!")
    else:
        late_days = used_days - allowed_days
        fine = calculate_fine(late_days)
        print(f" Late by {late_days} days.")
        print(f" Fine to pay: Rs {fine}")
    
    # Reset book
    library[name] = {
        "available": True,
        "issued_to": "",
        "issue_date": None,
        "days": 0
    }

# MENU
def menu():
    while True:
        print("\n LIBRARY MENU ")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print(" Invalid choice.")

menu()
