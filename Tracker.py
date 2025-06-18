# my expense tracker
# made this to keep track of where my money goes lol
# hope it helps!

import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# ok so here's how we store stuff:
# each expense is like: {"amount": 20, "category": "food", "date": "2024-03-20"}
# we keep all of them in a list and save to a json file

def load_expenses():
    # try to load the file, if it doesn't exist just give an empty list
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as f:
            return json.load(f)
    return []

def save_expenses(data):
    # save our expenses to the file
    with open('expenses.json', 'w') as f:
        json.dump(data, f, indent=2)

def add_expense():
    # get the expense details from user
    try:
        amount = float(input("how much did you spend? ₹"))
        category = input("what did you spend it on? ").lower()
        date_str = input("when? (YYYY-MM-DD) or just press enter for today: ")
        
        # if no date given, use today
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")
        
        # make the expense and save it
        expense = {
            "amount": amount,
            "category": category,
            "date": date_str
        }
        
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("cool, saved your expense!")
        
        # check if we're over budget
        check_budget_alert(category, amount)
        
    except ValueError:
        print("oops! that's not a valid number. try again!")

def edit_expense():
    expenses = load_expenses()
    if not expenses:
        print("nothing to edit yet!")
        return
    
    # show all expenses with numbers
    print("\nhere are your expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']}: ₹{exp['amount']}")
    
    try:
        # get which one to edit
        idx = int(input("\nwhich one do you want to change? (0 to cancel): ")) - 1
        if idx < 0 or idx >= len(expenses):
            print("that's not a valid number!")
            return
        
        # show what we're editing
        exp = expenses[idx]
        print(f"\nediting: {exp['date']} - {exp['category']}: ₹{exp['amount']}")
        
        # get new values (or keep old ones if nothing entered)
        amount = input("new amount? (press enter to keep current): ")
        category = input("new category? (press enter to keep current): ")
        date_str = input("new date? YYYY-MM-DD (press enter to keep current): ")
        
        if amount:
            exp['amount'] = float(amount)
        if category:
            exp['category'] = category.lower()
        if date_str:
            exp['date'] = date_str
            
        save_expenses(expenses)
        print("all done! expense updated!")
        
    except ValueError:
        print("that's not a valid number! try again!")

def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("nothing to delete!")
        return
    
    # show all expenses
    print("\nhere are your expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']}: ₹{exp['amount']}")
    
    try:
        # get which one to delete
        idx = int(input("\nwhich one do you want to delete? (0 to cancel): ")) - 1
        if idx < 0 or idx >= len(expenses):
            print("that's not a valid number!")
            return
        
        # remove it and save
        deleted = expenses.pop(idx)
        save_expenses(expenses)
        print(f"deleted: {deleted['date']} - {deleted['category']}: ₹{deleted['amount']}")
        
    except ValueError:
        print("that's not a valid number! try again!")

def view_summary():
    expenses = load_expenses()
    if not expenses:
        print("no expenses yet!")
        return
    
    # calculate total
    total = sum(exp["amount"] for exp in expenses)
    print(f"\ntotal spent: ₹{total:.2f}")
    
    # group by category
    by_category = {}
    for exp in expenses:
        cat = exp["category"]
        by_category[cat] = by_category.get(cat, 0) + exp["amount"]
    
    print("\nspending by category:")
    for cat, amt in by_category.items():
        print(f"{cat}: ₹{amt:.2f}")
    
    # show all expenses by date
    print("\nall expenses:")
    for exp in expenses:
        print(f"{exp['date']}: ₹{exp['amount']:.2f} ({exp['category']})")

def plot_summary():
    expenses = load_expenses()
    if not expenses:
        print("no expenses to plot!")
        return
    
    # get data ready for plotting
    by_category = defaultdict(float)
    by_date = defaultdict(float)
    
    for exp in expenses:
        by_category[exp['category']] += exp['amount']
        by_date[exp['date']] += exp['amount']
    
    # make the plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # pie chart for categories
    categories = list(by_category.keys())
    amounts = list(by_category.values())
    ax1.pie(amounts, labels=categories, autopct='%1.1f%%')
    ax1.set_title('where your money goes')
    
    # line plot for spending over time
    dates = sorted(by_date.keys())
    amounts = [by_date[date] for date in dates]
    ax2.plot(dates, amounts, marker='o')
    ax2.set_title('spending over time')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def set_budget():
    # create budget file if it doesn't exist
    if not os.path.exists('budget.json'):
        with open('budget.json', 'w') as f:
            json.dump({}, f)
    
    # load current budgets
    with open('budget.json', 'r') as f:
        budgets = json.load(f)
    
    # show current budgets
    print("\ncurrent budget limits:")
    for cat, limit in budgets.items():
        print(f"{cat}: ₹{limit}")
    
    # get new budget
    category = input("\nwhat category do you want to set a budget for? (press enter to finish): ").lower()
    if not category:
        return
    
    try:
        limit = float(input(f"what's your budget for {category}? ₹"))
        budgets[category] = limit
        with open('budget.json', 'w') as f:
            json.dump(budgets, f, indent=2)
        print(f"cool! budget set for {category}: ₹{limit}")
    except ValueError:
        print("that's not a valid number! try again!")

def check_budget_alert(category, amount):
    if not os.path.exists('budget.json'):
        return
    
    with open('budget.json', 'r') as f:
        budgets = json.load(f)
    
    if category in budgets:
        limit = budgets[category]
        if amount > limit:
            print(f"⚠️ whoa! you spent ₹{amount} on {category}, but your budget is ₹{limit}!")

def main():
    while True:
        print("\n=== Welcome to my expense tracker ===")
        print("1. add expense")
        print("2. view summary")
        print("3. edit expense")
        print("4. delete expense")
        print("5. show graphs")
        print("6. set budget")
        print("7. exit")
        
        choice = input("\nwhat do you want to do? (1-7): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            plot_summary()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            print("bye! 👋")
            break
        else:
            print("hmm, that's not a valid choice. try again!")

if __name__ == "__main__":
    main()