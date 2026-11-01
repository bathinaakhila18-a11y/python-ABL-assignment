
# Multi-Day Water Tank Simulation

print("===== WATER TANK SIMULATION =====")

capacity = 1000
water_level = 500
threshold_day = -1

days = int(input("Enter number of days: "))
threshold = float(input("Enter threshold level: "))

# Validate threshold and number of days
if days <= 0 or threshold < 0 or threshold > capacity:
    print("Invalid days or threshold")

else:
    for day in range(1, days + 1):

        print("\nDay", day)

        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        # Validate water quantities
        if inflow < 0 or outflow < 0:
            print("Invalid Input")
            break

        # Calculate water level
        new_level = water_level + inflow - outflow

        # Check overflow
        if new_level > capacity:
            print("Overflow Detected!")
            water_level = capacity

        # Check shortage
        elif new_level < 0:
            print("Water Shortage Detected!")
            water_level = 0

        else:
            water_level = new_level

        print("Current Water Level:", water_level, "litres")

        # Find first threshold interval
        if water_level >= threshold and threshold_day == -1:
            threshold_day = day

    else:
        print("\n===== FINAL SUMMARY =====")

        print("Final Water Level:", water_level, "litres")

        if threshold_day != -1:
            print("Threshold Reached on Day:", threshold_day)
        else:
            print("Threshold Not Reached")

        print("Simulation Completed")
