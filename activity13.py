#loan engine challenge

print("Loan Approval System")

# Inputs
age = int(input("Enter your age: "))
is_employed = bool(input("Are you currently employed?  --->  "))
credit_score = eval(input("Enter your credit score ---> "))
annual_income = eval(input("Enter your annual income ---> "))
has_collateral = bool(input("Do you have collateral? --->  "))

print("=========RESULT===========")

#baseline 
if age >= 21:
    if is_employed:

        if credit_score >= 750:
            rate = 5.0

        if annual_income >= 100000: 
            rate = 4.5

        print("Approved!")
        print("Credit Tier:High Credit")
        print("Interest Rate:", rate, "%")

    elif credit_score >= 600:
        rate = 8.0

        if has_collateral == True:
            rate = 7.0
        else:
            if annual_income <40000:
                rate = 9.5
                print("Approved!")
                print("Credit Tier: Fair Credit")
                print("Interest rate:", rate, "%")
               
            else:
                 print("Base line requirement failed")
    else:
         print("Base line requirement failed")
else:
    print("Base line requirement failed")      
     
