#Greeting Prompt for the calculator
print('Welcome to the tip calculator')
#This asks the user how much is the total bill
bill = float(input('How much is the total bill: #'))

#What percent tip would the user like to pay
percent_tip = int(input('What percent would you like to tip: ')) / 100

#How many people would be spliting the bill
no_of_people = int(input('How many people would split the bill: '))

#this calculates the total bill + tip
bill_with_tip = float(bill) + (bill * percent_tip)

#How much is each person supposed to pay
each_bill = bill_with_tip / no_of_people

#rounds up each person bill to two decimal places
bill_rounded = round(each_bill, 2)

#print the amount each person should pay
print(f"Each person should pay #{bill_rounded}")

#Goodbye message
print('Thank you for using the tip calculator')
