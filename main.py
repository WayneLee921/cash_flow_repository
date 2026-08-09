#This file will just to handle the interface with the user, asking for inputs and giving the outputs.

from datetime import datetime
from forecaster import simulate_month

def main():
    print("=== Welcome to the Cash-Flow Forecaster ===")

    starting_balance = 1500.00
    start_date = datetime.now()
    days_to_simulate = 30

    transactions = [
        {"name": "Rent", "amount": -1000.00, "day_of_month": 1},
        {"name": "Salary", "amount": 2500.00, "day_of_month": 5},
        {"name": "Groceries", "amount": -400.00, "day_of_month": 15},
        {"name": "Phone Bill", "amount": -100.00, "day_of_month": 20}
    ]

    print("\nCalculating your forecast.....")
    result = simulate_month(starting_balance, start_date, days_to_simulate, transactions)

    print("\n=== Forecast Results ===")
    print(f"Final Blance after {days_to_simulate} days: RM{result['final_balance']:.2f}")
    print(f"Lowest Balance: RM{result['lowest_balance']:.2f}")

    lowest_date_str = result['lowest_day'].strftime('%Y-%m-%d')
    print(f"Watch out! Your balance dips lowest on: {lowest_date_str}")

if __name__ == "__main__":
    main()