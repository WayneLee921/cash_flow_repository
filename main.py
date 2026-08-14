from datetime import datetime
from forecaster import simulate_month

def main():
    print("\n" + "="*45)
    print("💸 WELCOME TO THE CASH-FLOW FORECASTER 💸")
    print("="*45)

    set_start_balance = False
    while not set_start_balance:
        try:
            user_input = input("\n💰 Please enter your current bank balance (RM): ")
            starting_balance = float(user_input)
            set_start_balance = True
            break
        except ValueError:
            print("❌ Please re-enter a valid number (e.g., 1500.50).")
            
    start_date = datetime.now()
    days_to_simulate = 30

    transactions = []
    print("\n" + "-"*45)
    print("📝 ADD YOUR BILLS & INCOME")
    print("💡 (Type 'done' when you are finished adding)")
    print("-"*45)
    
    set_transactions = False
    while not set_transactions:
        t_name = input("\n📌 Enter the name of the transaction (or 'done'): ")
        if t_name.lower() == 'done':
            set_transactions = True
            break
        try:
            t_amount_input = input(f"   💵 Enter amount for '{t_name}' (use - for bills, or 'cancel'): RM ")
            if t_amount_input.lower() == 'cancel':
                raise ValueError("cancel")
            t_amount = float(t_amount_input)
            
            t_day_input = input(f"   📅 Enter the day of the month it happens (1-31, or 'cancel'): ")
            if t_day_input.lower() == "cancel":
                raise ValueError("cancel")
            t_day = int(t_day_input)

            if t_day < 1 or t_day > 31:
                print("   ❌ Invalid input. Please re-enter the day within 1 and 31.")
                continue

            transactions.append({
                "name": t_name,
                "amount": t_amount,
                "day_of_month": t_day
            })
            print(f"   ✅ Successfully added '{t_name}' to your forecast!")

        except ValueError as error:
            if str(error) == "cancel":
                print(f"   🛑 Cancelled adding '{t_name}'. Let's start over.")
            else:
                print("   ❌ Invalid amount or day. Please try again with valid numbers.")

    print("\n⏳ Calculating your forecast...")
    result = simulate_month(starting_balance, start_date, days_to_simulate, transactions)

    print("\n" + "="*45)
    print("📊 FORECAST RESULTS")
    print("="*45)
    print(f"Final Balance (after {days_to_simulate} days): RM {result['final_balance']:.2f}")
    print(f"Lowest Balance: RM {result['lowest_balance']:.2f}")

    lowest_date_str = result['lowest_day'].strftime('%Y-%m-%d')
    print(f"\n📉 Watch out! Your balance dips lowest on: {lowest_date_str}")

    if len(result['overdraft_dates']) > 0:
        print("\n⚠️  WARNING: Your account is projected to overdraw on these dates:")
        for warning in result['overdraft_dates']:
            warn_date = warning['date'].strftime('%Y-%m-%d')
            print(f"   🔴 {warn_date}: RM {warning['balance']:.2f}")
    else: 
        print("\n✅ Great news: You are not projected to overdraw this month!")

if __name__ == "__main__":
    main()