from expenses import expenses

def main():
    print("Welcome to the expenses tracker app, v 1.0!")

    budget = float(input("Enter the budget amount: "))

    expense_list = []

    choice = ""

    while choice != "6":
        choice = print_menu(budget)
        match choice:
            case "1": budget = add_expense(expense_list, budget)
            case "2": budget = delete_expense(expense_list, budget)
            case "3": budget = update_expense(expense_list, budget)
            case "4": list_expenses(expense_list)
            case "5": print_to_file(expense_list)
            case "6": print("Goodbye. Come Again Soon.")
            case _: print("Invalid choice. Please try again.")


def print_menu(budget):
    print(f"Your Budget: ${budget:.2f}")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. List of Expenses")
    print("5. Print to File")
    print("6. Exit")
    c = input("Your Choice: ")
    return str(c)


def add_expense(arr, budget):
    name = input("Enter the name of the expense you want to add: ")
    category = input("Enter the category of this expense: ")
    amount = float(input("Enter the amount for this expense: "))

    expense = expenses(name, category, amount)
    arr.append(expense)

    return budget - amount


def delete_expense(arr, budget):
    name = input("Enter the name of the expense you want to delete: ")
    category = input("Enter the category of this expense: ")
    amount = float(input("Enter the amount of this expense: "))

    for i, item in enumerate(arr):
        if item.name == name and item.category == category and item.amount == amount:
            arr.pop(i)
            return budget + amount

    print("Expense not found.")
    return budget
    

def update_expense(arr, budget):
    name = input("Enter the name of the expense you want to update: ")
    category = input("Enter the category of this expense: ")
    amount = float(input("Enter the amount of this expense: "))
    diff = 0

    for i, item in enumerate(arr):
        if item.name == name and item.category == category and item.amount == amount:
            print("Expense Found.")
            while True:
                print("\nWhat would you like to change in this Expense?")
                print("1. Name")
                print("2. Category")
                print("3. Amount")
                print("4. Exit")
                choice = input("Your Choice: ")
                if choice == "1":
                    item.name = input("Enter the new name of the expense: ")
                elif choice == "2":
                    item.category = input("Enter the new category of the expense: ")
                elif choice == "3":
                    new_amount = float(input("Enter the new amount of the expense: "))
                    diff = item.amount - new_amount
                    item.amount = new_amount
                elif choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
            arr[i] = item
            return budget + diff

    print("Expense Not Found.")
    return budget + diff
    


def list_expenses(arr):
    if not arr:
        print("No Expenses Recorded.")

    # count for list
    count = 1
    for item in arr:
        print(f"{count} - Name: {item.name}, Category: {item.category}, Amount: ${item.amount:.2f}")
        count += 1


def print_to_file(arr):
    file = open("expenses.csv", "a")

    for item in arr:
        file.write(f"{item.name},{item.category},{item.amount}\n")
    
    file.close()

    print("Done.")


def summaraize_expenses(arr):
    category_map = {}
    for item in arr:
        key = item.category
        if key in category_map:
            category_map[key] += item.amount
        else:
            category_map[key] = item.amount
    
    print("Final Expenses By Category:")
    for key, amount in category_map.items():
        print(f" {key}: ${amount:.2f}")

if __name__ == "__main__":
    main()