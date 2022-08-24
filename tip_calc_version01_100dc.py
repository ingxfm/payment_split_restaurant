#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
tot_bill = input("What was the total bill? $")
percent_tip = input("How much tip would you like to pay? 10, 12, 15? ")
num_people = input("How many people to split the bill? ")

bill_tip = (1 + float(percent_tip) / 100) * float(tot_bill)
pay_p_person = bill_tip / float(num_people)

print(f"Each person should pay: ${pay_p_person:.2f}")
