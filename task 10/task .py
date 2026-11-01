
# Food Supply Chain Stock Reconciliation

locations = [
    ("Vijayawada", "Rice", 100, 50, 80, 5, 65),
    ("Gudivada", "Wheat", 80, 40, 70, 5, 45),
    ("Hyderabad", "Dal", 60, 30, 50, 10, 25),
    ("Guntur", "Rice", 50, 20, 45, 5, 15)
]

minimum_stock = 20

total_received = 0
total_distributed = 0
total_damaged = 0
total_remaining = 0

print("----- FOOD STOCK RECONCILIATION -----")

for location in locations:

    name, item, opening, received, distributed, damaged, actual = location

    # Calculate expected stock
    expected = opening + received - distributed - damaged

    # Calculate discrepancy
    discrepancy = expected - actual

    # Calculate replenishment
    if actual < minimum_stock:
        replenishment = minimum_stock - actual
    else:
        replenishment = 0

    # Update totals
    total_received += received
    total_distributed += distributed
    total_damaged += damaged
    total_remaining += actual

    print("\nLocation:", name)
    print("Food Item:", item)
    print("Expected Stock:", expected, "kg")
    print("Actual Stock:", actual, "kg")

    if discrepancy == 0:
        print("Status: Stock Reconciled")
    else:
        print("Discrepancy:", discrepancy, "kg")
        print("Status: Stock Mismatch")

    print("Replenishment Required:", replenishment, "kg")

# Final report
print("\n----- FINAL REPORT -----")
print("Total Received:", total_received, "kg")
print("Total Distributed:", total_distributed, "kg")
print("Total Damaged:", total_damaged, "kg")
print("Total Remaining:", total_remaining, "kg")

