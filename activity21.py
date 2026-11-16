#Jeepney Simulator
route = ["Terminal", "Perez Park", "Pacific Mall"]
passenger =[]
passenger.append("Dan")
passenger.insert(0,"Lola Nena")
x = passenger.pop()
y = passenger.pop(0)
Seats = 6
Fare = 13 
total = 0

while True:
    print()
    print("Sakay",(passenger))
    print(len(passenger), "of", Seats,"seat")
    print("1 Sakay 2 Proirity seat 3 para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 exit")
    choice = input("choice: ")

    if choice == "1": 
        if len(passenger) == Seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passenger.append(name)
            total = total + Fare
            print(name, "board at the back.")

    elif choice == "2": 
        if len(passenger) == Seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passenger.insert(0, name)
            total = total + Fare
            print(name, "took the priority seat.")

    elif choice == "3":
        name = input("who is getting off? ") 
        if name in passenger:
            passenger.remove(name)
            print(name, "get off, ingat!")
        else:
            print(name, "is not on this jeep")

    elif choice == "4": 
        if len(passenger) == 0:
            print("The jeep is empty.")
        else:
            left = passenger.pop()
            print(left, "got off at the door.")

    elif choice == "5": 
        if len(passenger) == 0:
            print("The jeep is empty.")
        else:
            front = passenger.pop(0)
            print(front, "got off at the front")

    elif choice == "6":
        for i in range(len(passenger)):
            print("seats", i + 1, passenger[i])

    elif choice == "7":
        route. reverse()
        print("route:", route)

    elif choice == "8":
        print("total fare today:", total)
        break

    else:
        print("Invalid choice.")