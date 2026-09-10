# Global Freight Calculator

name = input("Sender name: ")
weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
is_express = input("Is it express? (y/n): ").lower() == "y"
is_international = input("Is it international? (y/n): ").lower() == "y"
is_rush = input("Is the item rush? (y/n): ").lower() == "y"

# Calculate
base_cost = (weight * 2.50) + (distance * 0.15)

# Evaluate pricing tiers
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif (is_express or is_international) and weight > 20:
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

elif is_rush:
    total = base_cost + 20

else:
    total = base_cost


# Display result

print("==================================")

print(f"Total shipping charge: ${total:.2f}")

