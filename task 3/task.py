
print("========== HOSPITAL BILLING SYSTEM ==========")

# Patient Details
name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))

# Enter Charges
consultation = float(input("Enter Consultation Charges: "))
diagnostic = float(input("Enter Diagnostic Charges: "))
treatment = float(input("Enter Treatment Charges: "))

income = float(input("Enter Annual Income: "))

# Validate Inputs
if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0 or income < 0:
    print("Invalid Input! Please enter valid values.")

else:
    # Calculate Total Bill
    total = consultation + diagnostic + treatment

    # Apply Concession
    concession = 0

    if age >= 60:
        concession = 10

    if income < 200000 and concession < 15:
        concession = 15

    # Calculate Final Bill
    discount = total * concession / 100
    final_bill = total - discount

    # Patient Classification
    if final_bill <= 5000:
        category = "Full Payment"

    elif final_bill <= 15000:
        category = "Installment Payment"

    else:
        category = "Special Approval Required"

    # Display Bill
    print("\n========== HOSPITAL BILL ==========")
    print("Patient Name:", name)
    print("Patient Age:", age)

    print("Consultation Charges:", consultation)
    print("Diagnostic Charges:", diagnostic)
    print("Treatment Charges:", treatment)

    print("Total Bill:", total)
    print("Concession:", concession, "%")
    print("Concession Amount:", discount)
    print("Final Bill:", final_bill)

    print("Patient Classification:", category)

    print("===================================")

