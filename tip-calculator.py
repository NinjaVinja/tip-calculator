# TIP - Calculator
print("🧾 Welcome to Tip Calculator 🧾")

# Taking inputs
bill = float(input("What was the total bill? Rs. "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating total bill with tip
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
per_person = round(total_bill / people, 2)

# Displaying result
print(f"\n💰 Total Bill (with tip): Rs. {total_bill}")
print(f"👥 Number of people: {people}")
print(f"🧍 Each person should pay: Rs. {per_person}")
