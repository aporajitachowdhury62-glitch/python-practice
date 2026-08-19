  ## Inputs we need from the user
#total rent
#total food ordered for snacking
#Electricity units spend
#Charge per unit
#people living in room/flat

## output
# total amount you've to pay is
rent= int(input("Enter total rent: "))
food= int(input("Enter the amount of food ordered: "))
electricity_spend= int(input("Enter total electricity spent: "))
charge_per_unit= int(input("Enter the charge per unit: "))
people= int(input("Enter the number of people living in the room/flat: "))

total_electricity_bill = electricity_spend * charge_per_unit

output  = (rent + food + total_electricity_bill) // people

print("EACH PERSON HAS TO PAY:", output)