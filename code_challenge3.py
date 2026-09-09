#Global Freight Calculator

name = input("sender name ---> ")
wieght = float(input("Enter weight(kg): "))
distance = float(input("Enter distance(km) "))
is_express = input("is it express?(True/False): ") == True
is_international = input("is it international?(True/False): ") == True


#calculate

base_cost = (weight * 2.50) + (distance * 0.15) 

#evaluate pricing tiers

if weight <= 2.0 and distance <= 100 and not is_express and not_international:
	total = 0.00

elif is_international and is_express:
	total = (base_cost * 1.40) + 50

elif (is_express or is_international) and weight >20:
	total = (base_cost * 1.20) + 25

elif weight >30 or distance >1000: 
	total = base_cost + 30

else: 
	total = base_cost