
n = int(input("Enter number of households: "))

total_consumption = 0
highest = 0
highest_name = ""

for i in range(n):

    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = float(input("Enter water consumption (KL): "))

    # Calculate progressive bill
    if units <= 10:
        bill = units * 5

    elif units <= 20:
        bill = (10 * 5) + (units - 10) * 8

    else:
        bill = (10 * 5) + (10 * 8) + (units - 20) * 12

    # Add fixed charge
    bill = bill + 50

    # Apply penalty
    if units > 30:
        bill = bill + 100

    total_consumption += units

    if units > highest:
        highest = units
        highest_name = name

    print("Household:", name)
    print("Consumption:", units, "KL")
    print("Water Bill: Rs.", bill)

    if units > 30:
        print("Status: Excessive Usage")
    else:
        print("Status: Normal Usage")

print("\n----- FINAL REPORT -----")
print("Total Consumption:", total_consumption, "KL")
print("Highest User:", highest_name)
print("Highest Consumption:", highest, "KL")
print("Average Consumption:", total_consumption / n, "KL")

