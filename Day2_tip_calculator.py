print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill?\n$")
tip_percentage = input("What percentage tip would you like to give?\n")
persons_to_split = input("How many people to split the bill?\n")

result = round((float(total_bill) + float(tip_percentage) * float(total_bill) / 100) / float(persons_to_split), 2)
final_amount = "{:.2f}".format(result)

print(f"Each person should pay: ${final_amount}")
