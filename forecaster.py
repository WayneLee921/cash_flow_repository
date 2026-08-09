#This file will hold the pure logic, which are the math that calculates the dates and balances. Keeping this separate from
#the other file allows us to easily find and verify that the core math works.

from datetime import timedelta

def simulate_month (starting_balance, start_date, days_to_simulate, transactions):
    current_balance = starting_balance

    lowest_balance = starting_balance
    lowest_day = start_date

    for i in range(days_to_simulate):
        current_day = start_date + timedelta(days = i)
        daily_change = 0

        for t in transactions:
            if t["day_of_month"] == current_day.day:
                daily_change += t["amount"]

        current_balance += daily_change

        if current_balance < lowest_balance:
            lowest_balance = current_balance
            lowest_day = current_day

    return {
        "final_balance": current_balance,
        "lowest_balance": lowest_balance,
        "lowest_day": lowest_day
    }