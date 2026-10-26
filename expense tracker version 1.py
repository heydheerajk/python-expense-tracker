
# Expense Tracker
from datetime import datetime

print("=" * 36)
print("         EXPENSE TRACKER")
print("=" * 36)

expenses = []
budget = float(input("ENTER YOUR BUDGET: "))

while True:
    print("\n" + "*" * 36)
    print("                MENU")
    print("*" * 36)
    print("1. ADD EXPENSE")
    print("2. VIEW EXPENSE")
    print("3. TOP UP MONEY IN BUDGET")
    print("4. EXIT")

    menu = input("ENTER YOUR MENU: ")

    if menu == "1":
        amount = float(input("ENTER YOUR AMOUNT: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            continue

        now = datetime.now()
        budget -= amount

        expenses.append({
            "DATE": now.strftime("%d/%m/%Y"),
            "TIME": now.strftime("%H:%M:%S"),
            "AMOUNT": amount,
            "BALANCE": budget
        })

        print(f"REMAINING BUDGET: ₹{budget:.2f}")
        print("Expense added successfully!")

    elif menu == "2":
        print("\n" + "=" * 65)
        print("                  EXPENSE STATEMENT")
        print("=" * 65)

        if not expenses:
            print("No expenses recorded yet.")
        else:
            for number, item in enumerate(expenses, start=1):
                print(f"\nExpense #{number}")
                print("Date    :", item["DATE"])
                print("Time    :", item["TIME"])
                print(f"Amount  : ₹{item['AMOUNT']:.2f}")
                print(f"Balance : ₹{item['BALANCE']:.2f}")

        print("=" * 65)
        print(f"CURRENT BUDGET: ₹{budget:.2f}")

    elif menu == "3":
        topup = float(input("ENTER YOUR TOP-UP AMOUNT: "))

        if topup <= 0:
            print("Top-up must be greater than zero!")
            continue

        budget += topup
        print(f"NEW BALANCE: ₹{budget:.2f}")
        print("Budget has been updated!")

    elif menu == "4":
        print("Thank you for using this Expense Tracker!")
        print("Author: Dheeraj Kumar Shah")
        break

    else:
        print("Invalid entry! Please try again.")
