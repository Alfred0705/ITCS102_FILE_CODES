#target 1 loan calculotor 
loan_amount = int(input("enter the loan amount:"))
year = int(input("enter the loan period years:"))
interest = 0.00256 

monthly = 1000 
principal = 41.67
rem_bal = 912.23423423423423

#string formatting
print(f"{monthly}\t\t | {principal} \t\t | {round(rem_bal,2)}")
