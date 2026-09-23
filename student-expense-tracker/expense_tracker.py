# Student Expense Tracker
expenses = []
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    note = input("Enter a short note: ")
    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!\n")
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n----- Your Expenses -----")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['note']}"
        )
    print()
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}\n")
def category_summary():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    print("\n----- Category Summary -----")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")
    print()
def main():
    while True:
        print("===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Student Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()