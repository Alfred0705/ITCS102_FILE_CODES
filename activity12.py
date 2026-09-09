name = input("Please input your name ---> ")
age = int(input("Please input your age ---> "))

if age >= 0 and age <= 5 : 
	print("The age is consider as INFANT")

elif age >= 6 and age <= 12 : 
	print("The age is consider as KID")

elif age >= 13 and age <= 15 : 
	print("The age is consider as PER TEEN")

elif age >= 16 and age <= 19 : 
	print("The age is consider as TEENAGER")

elif age >= 20 and age <= 29 : 
	print("The age is consider as EARLY ADULTHOOD")

elif age >= 30 and age <= 58 : 
	print("The age is consider as ADULTS")

elif age >= 59 and age <=100 : 
	print("The age is consider as SENIORS")

else:
	print("age invalid") 	