# Task 1: Cinema Ticket Price

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if  user_age >= 5 and user_age <= 12:
    ticket_price = "Rs. 300"
elif user_age >= 13 and user_age <= 59:
    ticket_price = "Rs. 700"
elif user_age >= 60 and user_age <= 100:
    ticket_price = "Rs. 400"
else:
    ticket_price = "Free"

print(f"Hello {user_name}, your ticket price is: {ticket_price}")

# ==================================================================================================
# Task 2: Temperature Converter

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is: {fahrenheit}")

if celsius < 10:
    weather = "Very Cold"
elif celsius >= 10 and celsius <= 19:
    weather = "Cold"
elif celsius >= 20 and celsius <= 29:
    weather = "Normal"
else:
    weather = "Hot"

print(f"Weather condition: {weather}")

# ===================================================================================================
# Task 3: Mobile Recharge Calculator

mobile_number = input("Enter your mobile number: ")
recharge_amount = float(input("Enter recharge amount: "))

tax = recharge_amount * 3 / 100
final_balance = recharge_amount - tax
print(f"Your recharge amount after tax deduction is: Rs. {final_balance}")

# ====================================================================================================
# Task 4: Weekly Steps Tracker

total_steps = 0

for i in range(1, 8):
    steps = int(input(f"Enter steps for day {i}: "))
    total_steps = total_steps + steps

average_steps = total_steps / 7

print(f"Total Steps: {total_steps}")
print(f"Daily Average: {average_steps}")

if average_steps >= 5000:
    print("Status: Active Week")
else:
    print("Status: Needs More Activity")

# =====================================================================================================
# Task 5: Secure PIN Checker

secret_pin = "1234"

for i in range(1, 4):

    user_pin = input("Enter your PIN: ")

    if user_pin == secret_pin:
        print("Access Granted")
        break

    else:
        remaining_attempts = 3 - i
        print(f"Incorrect PIN. Remaining attempts: {remaining_attempts}")

else:
    print("Account Blocked")
