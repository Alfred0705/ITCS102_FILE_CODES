#import demo
import getpass #folder in the python

username = "user1" 
password = "number_1"

u = input("Input USERNAME---> ") 
p = getpass.getpass("Input PASSWORD---> ")

if u == username and p == password:
	print("username and password correct")

else: 
	print("access denied")

