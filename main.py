print("Welcom to Tip-calculator app : ")

bill_amount = int(input("What was the total bill?"))
Tip = int(input("How much tip would you like to give? 10 , 12 , or 15"))
people = int(input("How many people to split the tip: "))

tip = Tip / 100
total_amout = bill_amount + (bill_amount * tip )
per_person = round(total_amout / people,2)

print(f"total bill {total_amout} \neach person pay : {per_person}$")