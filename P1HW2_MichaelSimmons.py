#This program calculates and displays travel expenses
#September 26, 2022
#CTI-110 P1HW2 - Travel Expense
#Michael A. Simmons

Initial_Budget = 1200.0

Fuel = 250.0
Accomodation = 300.0
Food = 200.0

Travel_Expenses = Fuel + Accomodation + Food

Remaining_Balance = Initial_Budget - Travel_Expenses

print('This program calculates and displays travel expenses')
print()
print('Enter Budget:', Initial_Budget)
print()
print('Enter your travel destination:', 'Asheville')
print()
print('How much do you think you will spend on gas?', Fuel)
print()
print('Approximately, how much will you need for accomodation/hotel?', Accomodation)
print()
print('Last, how much do you need for food?', Food)
print()
print('Remaining Balance:', Remaining_Balance)
