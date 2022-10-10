#This program calculates and displays travel expenses
#October 8, 2022
#CTI-110 P2HW1 - Travel Expense
#Michael A. Simmons
#
# Program gets all input from user
# Program calculates travel expenses
# Program prints and displays travel expenses results including budget remaining balance
#
Initial_Budget = int(input('Enter Inital Budget:\n'))
Travel_Destination = input('Enter your destination:\n')

Fuel = int(input('Enter Fuel Cost:\n'))
Accomodation = int(input('Enter Accommodation cost:\n'))
Food = int(input('Enter Food Cost:\n'))

Travel_Expenses = Fuel + Accomodation + Food

Location = Travel_Destination

Remaining_Balance = Initial_Budget - Travel_Expenses

print('This program calculates and displays travel expenses.')
print()
print('Enter Budget:', Initial_Budget)
print()
print('Enter your travel destination:', Travel_Destination)
print()
print('How much do you think you will spend on gas?', Fuel)
print()
print('Approximately, how much will you need for accomodation/hotel?', Accomodation)
print()
print('Last, how much do you need for food?', Food)
print()
print('-----------Travel Expenses-----------')
print(f"{'Location:':<19}{Location}")
print(f"{'Initial Budget:':<19}"+"${:.1f}".format(Initial_Budget))
print(f"{'Fuel:':<19}"+"${:.1f}".format(Fuel))
print(f"{'Accomodation:':<19}"+"${:.1f}".format(Accomodation))
print(f"{'Food:':<19}"+"${:.1f}".format(Food))
print('-------------------------------------')
print()
print("Remaining Balance: "+"${:.1f}".format(Remaining_Balance))
