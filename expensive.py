import csv
import os

FILE_NAME = 'expenses.csv'

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def add_expense(date, category, amount, description):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def view_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: ${row[2]}, Description: {row[3]}")
    else:
        print("No expenses recorded yet.")

def main():
    initialize_file()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = input("Enter the amount: ")
            description = input("Enter a description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully.")
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
