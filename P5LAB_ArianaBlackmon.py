# Ariana Blackmon
# July 19, 2026
# P5LAB - Self-Checkout Change Dispenser
# Simulates a self-checkout machine that calculates random purchase totals

import random

def disperse_change(change_amount):
    """
    Takes a float change_amount as a parameter and displays the amount
    of dollars, quarters, dimes, nickels, and pennies required to make change.
    """
    print(f"Change is: ${change_amount:.2f}\n")
    
    # Convert total change amount into total cents to avoid floating point issues
    cents = round(change_amount * 100)
    
    if cents == 0:
        print("No Change")
        return

    # Calculate dollars
    dollars = cents // 100
    cents %= 100

    # Calculate quarters
    quarters = cents // 25
    cents %= 25

    # Calculate dimes
    dimes = cents // 10
    cents %= 10

    # Calculate nickels
    nickels = cents // 5
    cents %= 5

    # Remaining cents are pennies
    pennies = cents

    # Display dollars
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    # Display quarters
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    # Display dimes
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    # Display nickels
    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")

    # Display pennies
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")


def main():
    """
    Main logic of the self-checkout simulation.
    Generates total owed, gets payment input, and calls disperse_change().
    """
    # Generate random amount owed rounded to 2 decimal places
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    # Prompt user for cash payment
    cash_paid = float(input("How much cash will you put in the self-checkout? $"))

    # Calculate change
    change_owed = cash_paid - amount_owed

    # Display change breakdown
    disperse_change(change_owed)


# Call the main function to run the program
if __name__ == "__main__":
    main()