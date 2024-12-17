# tip calculator

print("Welcome to the tip calculator")

# this line of code will take total bill as an input
total_bill=float(input(("What was the total bill? ")))

# this line of code will take tip's percentage as an input
tip=float(input("How much tip would you like to give? 10% ,12%  or 18%:  "))

# this line of code will take number person as an input 
number_of_people_to_be_spilted=int(input("How many people to  split the bill? "))


# this line of code calculate the net amount 
amount_to_paid=((total_bill*(tip/100))/number_of_people_to_be_spilted)



print(f"Each person should pay: {round(amount_to_paid,2)}")

