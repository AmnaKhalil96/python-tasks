# Task 6: Grocery Shopping Bill

total_bill = 0

total_products = int(input("Enter the number of products: "))

for i in range(1, total_products + 1):
    product_name = input(f"Enter the name of product {i}: ")
    product_price = float(input(f"Enter the price of {product_name}: "))
    product_quantity = int(input(f"Enter the quantity of {product_name}: "))

    subtotal = product_price * product_quantity
    total_bill = total_bill + subtotal

if total_bill >= 5000:
    discount = total_bill * 10 / 100
else:
    discount = 0

final_bill = total_bill - discount

print(f"Total Bill: Rs. {total_bill}")
print(f"Discount: Rs. {discount}")
print(f"Final Bill: Rs. {final_bill}")

# ==================================================================================================
# Task 7: Employee Weekly Salary

employee_name = input("Enter employee name: ")
working_hours = float(input("Enter total working hours in a week: "))
hourly_rate = float(input("Enter hourly rate: "))

if working_hours <= 40:
    weekly_salary = working_hours * hourly_rate
else:
    overtime_hours = working_hours - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    weekly_salary = (40 * hourly_rate) + overtime_pay

print(f"Employee Name: {employee_name}")
print(f"Weekly Salary: Rs. {weekly_salary}")

# ===================================================================================================
# Task 8: Bus Seat Booking

available_seats = [1,2,3,4,5,6,7,8,9,10]

seat_number = int(input("Enter the seat number you want to book (1-10): "))

if seat_number in available_seats:
    available_seats.remove(seat_number)
    print(f"Seat {seat_number} has been successfully booked.")
    print(f"Remaining available seats: {available_seats}")
else:
    print("Invalid seat number.")

# ====================================================================================================
# Task 9: Message Analyzer

message = input("Enter your message: ")

total_character = len(message)

total_words = len(message.split())

vowels = "aeiouAEIOU"
vowels_count = 0

for vowel in message:
    if vowel in vowels:
        vowels_count += 1

total_spaces = message.count(" ")

upper_case = message.upper()

if "python" in message.lower():
    python_exist = "yes"
else:
    python_exist = "no"

print("========== Message Analysis ==========")

print("Message:", message)
print("Total character:", total_character)
print("Total words:", total_words)
print("Total vowel:", vowels_count)
print("Total spaces:", total_spaces)
print("Uppercase formatting:", upper_case)
print("Python Exist:", python_exist)

# =====================================================================================================
# Task 10: Contact Book

contact_book = {}

while True:
    print("========== Contact Book ==========")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")

        if name in contact_book:
            print(f"Contact {name} already exists.")
        else:
            contact_book[name] = phone_number
            print(f"Contact {name} added successfully.")

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contact_book:
            print(f"Contact found: {name} - {contact_book[name]}")
        else:
            print(f"Contact {name} not found.")

    elif choice == "3":
        if contact_book:
            print("All Contacts:")

            for name, phone_number in contact_book.items():
                print(f"{name}: {phone_number}")
        else:
            print("No contacts found.")

    elif choice == "4":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")