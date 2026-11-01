# Problem Statement
To develop a Python program for an ATM Transaction Sequence Simulation System. The system processes multiple deposit and withdrawal transactions, maintains the account balance, enforces withdrawal limits, and rejects invalid transactions. It also generates a transaction summary showing total deposits, total withdrawals, rejected transactions, and the final account balance.
# Assumptions
3. The initial account balance is ₹10,000.
4. The user can perform multiple transactions.
5. The user can select Deposit or Withdrawal.
6. The minimum transaction amount is ₹100.
7. The maximum withdrawal limit per transaction is ₹5,000.
8. Withdrawal is allowed only when sufficient balance is available.
9. Negative or zero transaction amounts are invalid.
10. Invalid transactions are rejected without changing the balance.
11. Deposits and successful withdrawals are recorded separately.
12. The final balance and transaction summary are displayed at the end.
#  Algorithm
14. Start the program.
15. Initialize the account balance to ₹10,000.
16. Initialize total deposits, total withdrawals, and rejected transactions to zero.
17. Enter the number of transactions.
18. Read the transaction type (Deposit or Withdrawal).
19. Enter the transaction amount.
20. Validate the transaction amount.
21. If the amount is less than ₹100, reject the transaction.
22. If the transaction is a deposit, add the amount to the balance.
23. If the transaction is a withdrawal:
    - Check whether the amount is within ₹5,000.
    - Check whether sufficient balance is available.
    - If valid, subtract the amount from the balance.
    - Otherwise, reject the transaction.
11. Update the transaction totals.
12. Repeat until all transactions are completed.
13. Display total deposits, total withdrawals, rejected transactions, and final balance.
 # mermaid flow chart
 ```mermaid
flowchart TD
    A([Start]) --> B[Initialize Balance = 10000]
    B --> C[Initialize Deposit, Withdrawal and Rejected Counts]
    C --> D[/Enter Number of Transactions/]
    D --> E[/Enter Transaction Type and Amount/]
    E --> F{Amount >= 100?}
    F -- No --> G[Reject Transaction]
    F -- Yes --> H{Transaction Type?}
    H -- Deposit --> I[Add Amount to Balance]
    I --> J[Update Total Deposits]
    H -- Withdrawal --> K{Amount <= 5000?}
    K -- No --> G
    K -- Yes --> L{Sufficient Balance?}
    L -- No --> G
    L -- Yes --> M[Subtract Amount from Balance]
    M --> N[Update Total Withdrawals]
    G --> O[Update Rejected Count]
    J --> P{More Transactions?}
    N --> P
    O --> P
    P -- Yes --> E
    P -- No --> Q[Display Transaction Summary]
    Q --> R[Display Final Balance]
    R --> S([Stop])
```
# Conclusion
The ATM Transaction Sequence Simulation system successfully processes deposit and withdrawal transactions. It maintains the account balance, enforces withdrawal limits, checks available balance, and rejects invalid transactions. Finally, it generates a transaction summary showing total deposits, withdrawals, rejected transactions, and the final account balance. This program helps understand transaction processing and conditional statements in Python.
