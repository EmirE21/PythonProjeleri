print("Welcome to the Daily Expense Tracker!")
# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
# Initialize an empty list to store expenses
expenses = []
while True:
    # Get user choice
    choice = input()
    # Add a new expense
    if choice == "1":
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")
    # View all expenses
    elif choice == "2":
        if expenses != []:
            print("Your expenses:")
            for i in range(1, len(expenses)+1):
                print(f"{i}. {expenses[i-1]}")
        else:
            print("No expenses recorded yet.")
    # Calculate total and average expense
    elif choice == "3":
        if expenses != []:
            total_expense = 0
            for i in range(len(expenses)):
                total_expense += expenses[i]
            average_expense = total_expense/len(expenses)
            print(f"Total expense: {float(total_expense)}")
            print(f"Average expense: {float(average_expense)}")
        else:
            print("No expenses recorded yet.")
    # Clear all expenses
    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")
    elif not 1 <= int(choice) <= 5:
        print("Invalid choice. Please try again.")
    # Exit the program
    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break