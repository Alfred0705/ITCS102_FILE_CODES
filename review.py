#input

age = int(input("Enter your age")) 
rev = float(input("Enter your revenue"))
cc = input("Enter your credit card number")
yrs_bank = int(input("Enter your years with the bank"))
has_defaulted = input("Have you defaulted on a loan before? ")
collat = input("Do you have collateral? ")
collateral_value = float(input("Enter the value of your collateral "))

max_limit = 0
base_fee = 0

#baseline
if age >=21 and yrs_bank >= 2 and has_defaulted is False:
    print ("Baseline Requirement pass ")

    if cc >= 720: #teir 1
      max_loan = rev * 3
      print("max loan for high credit score is ",max_loan)
      print ("High Credit Score of 720")
      if rev >= 50000:
         base_fee = max_loan * 0.015
         print("base fee rate is ", base_fee)
      else:
         base_fee = max_loan * 0.025
         print("base fee rate is",base_fee)

      if c_value >= max_loan:
         print("collateral", collateral, "-- Accepted")
      else:
         print("collateral not accepted")

    elif cc <= 620 and cc < 720: #teir 2
       max_loan = rev * 1.5
       print("max loan is set to ",max_loan)
       if yrs_b >= 5:
          base_fee = max_loan * 0.02
          print("base fee rate is ",base_fee)
       else: 
          base_fee = max_loan * 0.035
          print("base fee rate is ",base_fee)

          #surcharge
          surcharge = max_loan * base_fee
          if c_value % 50000 != 0: 
             surcharge += 250

          if c_value >= max_loan:
             print("Collateral", collateral, " -- Accepted")
          else:
             print("collateral not accepted")

    elif cc < 620: #teir 3
       print("credit score is too low for a loan")
    else:
       print("not tier 1")
else:
   print("Reject, High Risk Application or Ineligible Owner")
          
          
          



      
      
       
       
      


