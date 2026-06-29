# Bank Transaction Summary Program

# Step 1: Initialize variables
total_deposit = 0
total_withdrawal = 0
balance = 0

# Step 2: Keep accepting transactions
while True:
    amount = int(input("Enter transaction amount (0 to stop): "))

    # Step 3: Stop condition
    if amount == 0:
        break

    # Step 4: Deposit
    elif amount > 0:
        total_deposit += amount
        balance += amount

    # Step 5: Withdrawal
    else:
        total_withdrawal += abs(amount)
        balance += amount

# Step 6: Display summary
print("\n--- Bank Transaction Summary ---")
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", balance)