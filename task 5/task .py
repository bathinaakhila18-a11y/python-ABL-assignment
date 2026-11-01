# ATM Transaction Sequence Simulation

print("===== ATM TRANSACTION SYSTEM =====")

# Initial balance
balance = 10000

total_deposits = 0
total_withdrawals = 0
rejected = 0

# Number of transactions
n = int(input("Enter number of transactions: "))

for i in range(n):

    print("\nTransaction", i + 1)

    print("D - Deposit")
    print("W - Withdrawal")

    choice = input("Enter transaction type: ").upper()
    amount = float(input("Enter amount: "))

    # Validate amount
    if amount < 100:
        print("Invalid Transaction Amount")
        rejected += 1

    # Deposit transaction
    elif choice == "D":

        balance += amount
        total_deposits += amount

        print("Deposit Successful")

    # Withdrawal transaction
    elif choice == "W":

        if amount > 5000:
            print("Withdrawal Limit Exceeded")
            rejected += 1

        elif amount > balance:
            print("Insufficient Balance")
            rejected += 1

        else:
            balance -= amount
            total_withdrawals += amount

            print("Withdrawal Successful")

    else:
        print("Invalid Transaction Type")
        rejected += 1

    print("Current Balance: Rs.", balance)


# Transaction Summary
print("\n===== TRANSACTION SUMMARY =====")

print("Total Deposits: Rs.", total_deposits)
print("Total Withdrawals: Rs.", total_withdrawals)
print("Rejected Transactions:", rejected)
print("Final Account Balance: Rs.", balance)

print("\nThank you for using ATM!")
