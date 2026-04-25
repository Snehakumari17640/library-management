import datetime

library = {}

# add book
def add_book():
    name = input("Enter book name: ")
    
    if name in library:
        print("Book already in library")
    else:
        library[name] = {
            "available": True,
            "student": "",
            "date": None,
            "days": 0
        }
        print("Book added")

# show books
def show_books():
    if len(library) == 0:
        print("No books")
    else:
        print("\nBooks list:")
        for b in library:
            if library[b]["available"]:
                print(b, "- Available")
            else:
                print(b, "- Issued to", library[b]["student"])

# issue book
def issue_book():
    name = input("Enter book name: ")

    if name not in library:
        print("Book not found")
        return

    if library[name]["available"] == False:
        print("Already issued")
        return

    student = input("Student name: ")
    
    try:
        days = int(input("For how many days: "))
    except:
        print("Wrong input")
        return

    library[name]["available"] = False
    library[name]["student"] = student
    library[name]["date"] = datetime.date.today()
    library[name]["days"] = days

    print("Book issued")
    print("Fine rule: 10 rs/day, next week 20, then 30...")

# fine
def calculate_fine(late):
    total = 0
    for i in range(1, late + 1):
        week = (i - 1) // 7 + 1
        total = total + (10 * week)
    return total

# return book
def return_book():
    name = input("Enter book name: ")

    if name not in library:
        print("Not found")
        return

    if library[name]["available"] == True:
        print("This book was not issued")
        return

    issue_date = library[name]["date"]
    allowed = library[name]["days"]

    today = datetime.date.today()
    used = (today - issue_date).days

    if used <= allowed:
        print("Returned on time")
    else:
        late = used - allowed
        fine = calculate_fine(late)
        print("Late by", late, "days")
        print("Fine =", fine)

    # reset values
    library[name]["available"] = True
    library[name]["student"] = ""
    library[name]["date"] = None
    library[name]["days"] = 0

# menu
while True:
    print("\n1 Add")
    print("2 Show")
    print("3 Issue")
    print("4 Return")
    print("5 Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        show_books()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        return_book()
    elif ch == "5":
        print("Bye")
        break
    else:
        print("Wrong choice")
