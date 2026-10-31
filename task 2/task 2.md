# Problem Statement
Design a Progressive Electricity Billing System that calculates household electricity bills based on the number of units consumed using multiple consumption slabs. The system should include fixed charges, additional surcharges and applicable rebates. It should calculate the total bill amount for each month, compare electricity bills across several months and identify unusual increases in consumption or billing amounts.
Assumptions
1. Electricity consumption is measured in units (kWh).
2. The billing period is one month.
3. The following slab rates are assumed:
Consumption	Rate per unit
First 100 units	₹2
101–200 units	₹3
201–300 units	₹5
Above 300 units	₹7
4. Fixed charge is ₹50 per month.
5. Surcharge is 5% of the energy charge.
6. A rebate of ₹20 is given if consumption is below 100 units.
7. Rebate is deducted from the final bill.
8. A bill increase of more than 30% compared with the previous month is considered unusual.
9. The bill amount cannot be negative.
# Algorithm
1. Start.
2. Read the number of months.
3. Initialize an empty list to store monthly bills.
4. For each month:
   - Read the electricity units consumed.
   - Calculate energy charges using progressive slabs.
   - Add fixed charges.
   - Calculate a 5% surcharge on energy charges.
   - Check whether consumption is below 100 units.
   - If yes, apply a ₹20 rebate.
   - Calculate the final bill amount.
   - Store the monthly units and bill amount.
5. Compare each month's bill with the previous month's bill.
6. Calculate the percentage increase in the bill.
7. If the increase is greater than 30%, display "Unusual Increase".
8. Otherwise, display "Normal Increase".
9. Display all monthly bills and comparison results.
10. Stop.

# Mermaid flowchat 
```mermaid
flowchart TD
    A([START]) --> B[/Enter Number of Months/]
    B --> C[/Enter Electricity Units/]
    C --> D{Units <= 100?}

    D -- Yes --> E[Energy = Units * 2]
    D -- No --> F{Units <= 200?}

    F -- Yes --> G[Energy = 200 + (Units - 100) * 3]
    F -- No --> H{Units <= 300?}

    H -- Yes --> I[Energy = 500 + (Units - 200) * 5]
    H -- No --> J[Energy = 1000 + (Units - 300) * 7]

    E --> K[Calculate Fixed Charge = 50]
    G --> K
    I --> K
    J --> K

    K --> L[Calculate Surcharge = Energy * 5%]
    L --> M{Units < 100?}

    M -- Yes --> N[Rebate = 20]
    M -- No --> O[Rebate = 0]

    N --> P[Calculate Total Bill]
    O --> P

    P --> Q[Store Monthly Bill]
    Q --> R{More Months?}

    R -- Yes --> C
    R -- No --> S[Compare Monthly Bills]

    S --> T[Calculate Percentage Increase]
    T --> U{Increase > 30%?}

    U -- Yes --> V[Display Unusual Increase]
    U -- No --> W[Display Normal Increase]

    V --> X[/Display Monthly Bills/]
    W --> X
    X --> Y([STOP])
```
  # sample input
 Enter number of months: 3

Month 1
Enter electricity units: 80

Month 2
Enter electricity units: 150

Month 3
Enter electricity units: 280
