# Problem Statement
To develop a program for hospital billing and patient classification. The program accepts the patient's name, age, patient type, and number of days admitted. It calculates the total hospital bill based on the patient type and classifies the patient as a child, adult, or senior citizen based on age.
#  Algorithm
1. Start.
2. Read the patient's name, age, patient type, and number of days admitted.
3. Calculate the hospital bill based on the patient type.
   - General patient: ₹1,000 per day.
   - Emergency patient: ₹2,000 per day.
   - ICU patient: ₹5,000 per day.
Calculate the total bill using:
Total Bill = Daily Charge × Number of Days
5. Classify the patient based on age:
- If age is less than 18, classify as Child.
- If age is between 18 and 59, classify as Adult.
- If age is 60 or above, classify as Senior Citizen.
6. Display the patient's details, classification, and total hospital bill.
# flowchart
  ```mermaid
flowchart TD
    A([Start]) --> B[/Input name, age, patient type, days/]
    B --> C{Patient type?}

    C -->|General| D[Daily charge = 1000]
    C -->|Emergency| E[Daily charge = 2000]
    C -->|ICU| F[Daily charge = 5000]

    D --> G[Calculate total bill]
    E --> G
    F --> G

    G --> H{Age less than 18?}
    H -->|Yes| I[Classification = Child]
    H -->|No| J{Age less than 60?}

    J -->|Yes| K[Classification = Adult]
    J -->|No| L[Classification = Senior Citizen]

    I --> M[/Display classification and bill/]
    K --> M
    L --> M

    M --> N([Stop])
  ```

