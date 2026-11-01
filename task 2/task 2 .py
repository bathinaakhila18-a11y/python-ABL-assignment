# Progressive Electricity Billing System

months = int(input("Enter number of months: "))

bills = []

for i in range(months):
    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    # Calculate bill using progressive slabs
    if units <= 100:
        amount = units * 1.50
    elif units <= 200:
        amount = (100 * 1.50) + (units - 100) * 2.50
    elif units <= 300:
        amount = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        amount = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00

    # Fixed charges
    fixed_charge = 50

    # Surcharge
    surcharge = amount * 0.05

    # Rebate for low consumption
    if units <= 100:
        rebate = amount * 0.10
    else:
        rebate = 0

    # Final bill
    total = amount + fixed_charge + surcharge - rebate

    bills.append(total)

    print("Energy Charge:", amount)
    print("Fixed Charge:", fixed_charge)
    print("Surcharge:", surcharge)
    print("Rebate:", rebate)
    print("Total Electricity Bill: Rs.", round(total, 2))


# Monthly bill comparison
print("\n----- MONTHLY BILL COMPARISON -----")

for i in range(months):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

# Identify unusual increases
for i in range(1, months):
    increase = bills[i] - bills[i - 1]

    if bills[i - 1] > 0 and increase > bills[i - 1] * 0.20:
        print("Unusual increase detected in Month", i + 1)
    else:
        print("No unusual increase in Month", i + 1)

print("\nElectricity Billing Completed!")
