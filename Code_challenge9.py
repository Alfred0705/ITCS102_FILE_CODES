#target 1 Loan Payment Schedule
loan_amount = int(input("Enter the loan amount:"))
year = int(input("Enter the loan period in years: "))

interest = 0.0025          #3% per year / 12 months
months = year * 12
principal = loan_amount / months
rem_bal = loan_amount

print()
print("Paymnent Schedule")
print("Month\t| Monthly Payment\t| Interest\t| Principal\t| Remaining Loan")
print("-" * 75)

for month in range(1, months + 1):
    interest_rate = rem_bal * interest
    monthly = principal + interest_rate
    rem_bal = rem_bal - principal
    if rem_bal < 0.005:
        rem_bal = 0

    print(f"{month}\t| {monthly: .2f}\t\t| {interest: .2f}\t\t| {principal: .2f}\t| {rem_bal: .2f}")

#Target 2 Hollow Pyramid 

rows = 6
for i in range(rows):
    if i == 0:
        print(" " * (rows - 1) + "*")
    elif i == rows - 1:
        print("*" * (2 * rows - 1))
    else:
        print(" " * (rows - 1 - i) + "*" + " " * (2 * i - 1) + "*")
        
#Target 3 "Z" Shape

size = 5
print("*" * size)
for i in range(size - 2):
    print(" " * (size - 2 - i) + "*")
print("*" * size)

