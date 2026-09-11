# Task 11: Personal Expense Tracker

# Task 11: Personal Expense Tracker

expenses = []

total_expenses = int(input("Enter total number of expenses: "))

for i in range(1, total_expenses + 1):
    expense_name = input(f"Enter expense name {i}: ")
    category = input("Enter category (Food, Transport, Shopping, Bills, Other): ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": expense_name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


total_spending = 0

for expense in expenses:
    total_spending = total_spending + expense["amount"]


category_spending = {
    "Food": 0,
    "Transport": 0,
    "Shopping": 0,
    "Bills": 0,
    "Other": 0
}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    category_spending[category] = category_spending[category] + amount

highest_expense = expenses[0]

for expense in expenses:
    if expense["amount"] > highest_expense["amount"]:
        highest_expense = expense


budget = float(input("Enter your budget: "))


def display_report():
    print("\n========== Expense Report ==========")
    print(f"Total Spending: Rs. {total_spending}")

    print("\nCategory Spending:")
    for category, amount in category_spending.items():
        print(f"{category}: Rs. {amount}")

    print(f"\nHighest Expense: {highest_expense['name']} - Rs. {highest_expense['amount']}")

    if total_spending > budget:
        print("Warning: Budget Exceeded!")
    else:
        print("Budget Status: Within Budget")


display_report()

# ====================================================================================================
# Task 12: Store Inventory Manager

inventory = {}

def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter available quantity: "))

    inventory[product_name] = {
        "price": price,
        "quantity": quantity
    }

    print(f"{product_name} added successfully.")

def sell_product():
    product_name = input("Enter product name to sell: ")

    if product_name in inventory:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= inventory[product_name]["quantity"]:
            inventory[product_name]["quantity"] -= quantity
            print(f"{quantity} {product_name} sold successfully.")
        else:
            print("Warning: Insufficient stock.")
    else:
        print("Product not found.")


def restock_product():
    product_name = input("Enter product name to restock: ")

    if product_name in inventory:
        quantity = int(input("Enter quantity to add: "))
        inventory[product_name]["quantity"] += quantity
        print(f"{product_name} restocked successfully.")
    else:
        print("Product not found.")

def search_product():
    product_name = input("Enter product name to search: ")

    if product_name in inventory:
        print(f"Product: {product_name}")
        print(f"Price: Rs. {inventory[product_name]['price']}")
        print(f"Quantity: {inventory[product_name]['quantity']}")
    else:
        print("Product not found.")

def display_inventory():
    if inventory:
        print("\n========== Inventory ==========")

        for product_name, details in inventory.items():
            print(f"Product: {product_name}")
            print(f"Price: Rs. {details['price']}")
            print(f"Quantity: {details['quantity']}")

            if details["quantity"] < 5:
                print("Low Stock!")

            print("--------------------")

        total_value = 0

        for product_name, details in inventory.items():
            product_value = details["price"] * details["quantity"]
            total_value = total_value + product_value

        print(f"Total Inventory Value: Rs. {total_value}")

    else:
        print("Inventory is empty.")

while True:
    print("\n========== Store Inventory Manager ==========")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. Search Product")
    print("5. Display Inventory")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()

    elif choice == "2":
        sell_product()

    elif choice == "3":
        restock_product()

    elif choice == "4":
        search_product()

    elif choice == "5":
        display_inventory()

    elif choice == "6":
        print("Exiting Inventory Manager.")
        break

    else:
        print("Invalid choice. Please try again.")

# =================================================================================================================
books = []


def add_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book added successfully.")


def display_books():
    if books:
        print("\n========== Library Books ==========")

        for book in books:
            print(f"Book ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            print("--------------------")

    else:
        print("No books available in the library.")


def search_book():
    title = input("Enter book title to search: ")

    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            print("\nBook Found:")
            print(f"Book ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            found = True
            break

    if not found:
        print("Book not found.")


def borrow_book():
    book_id = input("Enter Book ID to borrow: ")

    for book in books:
        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")

            return

    print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


while True:
    print("\n========== Library Book Management System ==========")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")

# =================================================================================================================
# Task 14: Restaurant Ordering System

menu = {
    "Burger": 500,
    "Pizza": 1200,
    "Pasta": 800,
    "Drink": 200
}

orders = []

print("========= Restaurant Menu =========")

for key, value in menu.items():
    print(f"{key} : Rs. {value}")


while True:

    item_name = input("Enter your item name: ").title()

    if item_name in menu:
        quantity = int(input("Enter quantity of your item: "))

        price = menu[item_name]
        sub_total = price * quantity

        orders.append({
            "item": item_name,
            "quantity": quantity,
            "sub_total": sub_total
        })

        print(f"{item_name} added to your order.")

    else:
        print("This item is not available.")

    choice = input("You want to add more items: yes/no: ").lower()

    if choice == "no":
        break


total = 0

for order in orders:
    total = total + order["sub_total"]


tax = total * 0.13


if total >= 3000:
    discount = total * 0.10
else:
    discount = 0


grand_total = total + tax - discount


def receipt():
    print("\n============ Receipt ============")

    for order in orders:
        print(f'{order["item"]} x {order["quantity"]} = Rs. {order["sub_total"]}')

    print("-------------------------------")
    print(f"Total: Rs. {total}")
    print(f"Tax (13%): Rs. {tax}")
    print(f"Discount: Rs. {discount}")
    print(f"Grand Total: Rs. {grand_total}")


receipt()

# ==================================================================================================
# Task 15: Clinic Appointment Manager

patients = []


def add_patient():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["id"] == patient_id:
            print("Patient ID already exists.")
            return

    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))
    problem = input("Enter Patient Problem: ")
    time = input("Enter Appointment Time: ")
    emergency = input("Is this an emergency patient? yes/no: ").lower()

    patient = {
        "id": patient_id,
        "name": patient_name,
        "age": patient_age,
        "problem": problem,
        "time": time,
        "emergency": emergency,
        "status": "Active"
    }

    patients.append(patient)

    print("Appointment added successfully.")


def search_patient():
    patient_id = int(input("Enter Patient ID to search: "))

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient Found")
            print(f'Patient ID: {patient["id"]}')
            print(f'Patient Name: {patient["name"]}')
            print(f'Patient Age: {patient["age"]}')
            print(f'Patient Problem: {patient["problem"]}')
            print(f'Appointment Time: {patient["time"]}')
            print(f'Emergency: {patient["emergency"]}')
            print(f'Status: {patient["status"]}')
            return

    print("Patient not found.")


def display_appointments():
    print("\n========== Emergency Patients ==========")

    for patient in patients:
        if patient["emergency"] == "yes" and patient["status"] == "Active":
            print(f'Patient ID: {patient["id"]}')
            print(f'Patient Name: {patient["name"]}')
            print(f'Patient Age: {patient["age"]}')
            print(f'Problem: {patient["problem"]}')
            print(f'Appointment Time: {patient["time"]}')
            print("--------------------")


    print("\n========== Normal Patients ==========")

    for patient in patients:
        if patient["emergency"] == "no" and patient["status"] == "Active":
            print(f'Patient ID: {patient["id"]}')
            print(f'Patient Name: {patient["name"]}')
            print(f'Patient Age: {patient["age"]}')
            print(f'Problem: {patient["problem"]}')
            print(f'Appointment Time: {patient["time"]}')
            print("--------------------")


def cancel_appointment():
    patient_id = int(input("Enter Patient ID to cancel appointment: "))

    for patient in patients:
        if patient["id"] == patient_id:

            if patient["status"] == "Active":
                patient["status"] = "Cancelled"
                print("Appointment cancelled successfully.")
            else:
                print("Appointment is already cancelled.")

            return

    print("Patient not found.")


def display_summary():
    emergency_count = 0
    normal_count = 0

    for patient in patients:
        if patient["status"] == "Active":
            if patient["emergency"] == "yes":
                emergency_count += 1
            else:
                normal_count += 1

    print("\n========== Clinic Summary ==========")
    print(f"Total Emergency Patients: {emergency_count}")
    print(f"Total Normal Patients: {normal_count}")
    print(f"Total Active Patients: {emergency_count + normal_count}")


while True:
    print("\n========== Clinic Appointment Manager ==========")
    print("1. Add Appointment")
    print("2. Search Patient")
    print("3. Display Appointments")
    print("4. Cancel Appointment")
    print("5. Display Clinic Summary")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        search_patient()

    elif choice == "3":
        display_appointments()

    elif choice == "4":
        cancel_appointment()

    elif choice == "5":
        display_summary()

    elif choice == "6":
        print("Exiting Clinic Appointment Manager.")
        break

    else:
        print("Invalid choice. Please try again.")