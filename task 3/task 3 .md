# Problem Statement
Develop a Python program to calculate hospital bills by processing consultation charges, diagnostic charges, and treatment charges. Apply conditional concessions based on patient eligibility, validate billing constraints, calculate the final payable amount, and classify patients according to the payment policy.
# Assumptions
1. The patient must enter a valid name and age.
2. Consultation, diagnostic, and treatment charges must be non-negative.
3. Senior citizens (age 60 or above) receive a 10% concession.
4. Patients with annual income below ₹2,00,000 receive a 15% concession.
5. Only one concession is applied. If both conditions are satisfied, the higher concession is applied.
6. Payment classification:
   - Up to ₹5,000 – Full Payment.
   - ₹5,001 to ₹15,000 – Installment Payment.
   - Above ₹15,000 – Special Approval Required.
#  Algorithm
1. Start.
2. Read patient name and age.
3. Read consultation charges.
4. Read diagnostic charges.
5. Read treatment charges.
6. Read annual income.
7. Validate all input values.
8. Calculate total bill.
9. Check concession eligibility.
10. Calculate concession amount.
11. Calculate final bill.
12. Classify patient according to payment policy.
13. Display bill details and patient classification.
14. Stop
# flow chart 
```mermaid 
 .flowchart TD
    A([Start]) --> B[/Enter patient name, age/]
    B --> C[/Enter consultation, diagnostic and treatment charges/]
    C --> D[/Enter annual income/]
    D --> E{Are inputs valid?}
    E -- No --> F[/Display Invalid Input/]
    F --> Z([Stop])
    E -- Yes --> G[Calculate Total Bill]
    G --> H{Age >= 60?}
    H -- Yes --> I[Apply 10% Concession]
    H -- No --> J{Income < 200000?}
    J -- Yes --> K[Apply 15% Concession]
    J -- No --> L[No Concession]
    I --> M[Calculate Final Bill]
    K --> M
    L --> M
    M --> N{Final Bill <= 5000?}
    N -- Yes --> O[Full Payment]
    N -- No --> P{Final Bill <= 15000?}
    P -- Yes --> Q[Installment Payment]
    P -- No --> R[Special Approval Required]
    O --> S[/Display Bill and Classification/]
    Q --> S
    R --> S
    S --> Z
```
# sample input 
Enter Patient Name: Akhila
Enter Patient Age: 65

Enter Consultation Charges: 1000
Enter Diagnostic Charges: 2000
Enter Treatment Charges: 5000

Enter Annual Income: 300000
