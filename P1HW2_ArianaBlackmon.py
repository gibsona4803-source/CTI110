# Ariana Blackmon
# 6/16/2026
# Assignment Name: P1HW2 - Travel Budget Calculator
# Description: This program calculates and displays travel expenses and subtracts them from a user-defined budget.

print("This program calculates and displays travel expenses \n")
# 1. Ask user to enter their budget
budget = int(input("Enter Budget: "))

# 2. Ask user to enter travel destination
destination = input("Enter your travel destination: ")

print()

# 3. Ask user for amount they will spend on gas
gas = int(input("How much do you think you will spend on gas? "))

# 4. Ask user for amount they will spend on accommodation
hotel = int(input("Approximately, how much will you need for accommodation/hotel? "))

# 5. Ask user for amount they will spend on food
food = int(input("Last, how much do you need for food? "))

print() # Prints a blank line for clean spacing

# 6. Add expenses and calculate remaining balance
print("------------Travel Expenses------------")
print("Location:", destination)
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")
print("---------------------------------------")

# 7. Perform calculations
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# 8. Display results
print()
print(f"Remaining Balance: {remaining_balance}")
