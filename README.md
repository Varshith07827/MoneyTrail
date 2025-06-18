# MoneyTrail - Personal Expense Tracker

A simple command-line expense tracker built in Python to help you monitor your spending habits and manage your personal finances.

## Features

### Core Features
- ✅ **Add Expenses**: Log your daily expenses with amount, category, and date
- ✅ **View Summary**: See total expenses, category-wise breakdown, and spending over time
- ✅ **Data Persistence**: All data is automatically saved to JSON files
- ✅ **Interactive Menu**: Easy-to-use command-line interface

### Bonus Features
- ✅ **Edit/Delete Expenses**: Modify or remove previously added entries
- ✅ **Graphical Reports**: Visual charts using matplotlib (pie charts and line graphs)
- ✅ **Budget Alerts**: Set spending limits and get warnings when exceeded

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Varshith07827/MoneyTrail.git
   cd MoneyTrail
   ```

2. **Install dependencies**
   ```bash
   pip install matplotlib
   ```

3. **Run the application**
   ```bash
   python Tracker.py
   ```

## Usage

### Main Menu
The application provides a simple menu with 7 options:

1. **Add Expense** - Log a new expense
2. **View Summary** - See spending overview
3. **Edit Expense** - Modify existing entries
4. **Delete Expense** - Remove entries
5. **Show Graphs** - Visual spending analysis
6. **Set Budget** - Configure spending limits
7. **Exit** - Close the application

### Adding an Expense
```
how much did you spend? ₹25.50
what did you spend it on? food
when? (YYYY-MM-DD) or just press enter for today: 2024-03-20
```

### Setting Budget Limits
```
what category do you want to set a budget for? food
what's your budget for food? ₹200
```

## Data Storage

The application uses two JSON files for data persistence:

- `expenses.json` - Stores all your expense entries
- `budget.json` - Stores your category-wise budget limits

**Note**: These files are automatically created when you first use the application.

## Data Model

Each expense is stored as a JSON object:
```json
{
  "amount": 25.50,
  "category": "food",
  "date": "2024-03-20"
}
```

## Features in Detail

### Expense Management
- Add expenses with amount, category, and optional date
- Edit existing expenses (amount, category, or date)
- Delete unwanted entries
- Automatic date stamping for today's expenses

### Summary Views
- **Total Spending**: Overall expense summary
- **Category Breakdown**: See how much you spend in each category
- **Time-based View**: Chronological list of all expenses

### Budget System
- Set spending limits for different categories
- Automatic alerts when you exceed budget
- Persistent budget storage between sessions

### Visual Reports
- **Pie Chart**: Shows spending distribution by category
- **Line Graph**: Displays spending trends over time
- Requires matplotlib library

## Requirements

- Python 3.x
- matplotlib (for graphical reports)

## File Structure

```
Expense/
├── Tracker.py          # Main application file
├── expenses.json      # Expense data (auto-generated)
├── budget.json        # Budget limits (auto-generated)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Future Enhancements

- GUI interface using Tkinter
- Web interface using Flask
- Export functionality (PDF, Excel)
- User accounts and authentication
- Advanced analytics and insights
- Expense reminders and notifications

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is open source and available under the MIT License.

## Author

Varshith07827

---

**Happy tracking! 💰** 