#This program calculates employee payroll (Payroll Calculator)
#October 31, 2022
#CTI-110 P3HW2 - Salary
#Michael A. Simmons
#
# Program gets data input from user
# Program calculates employee regular pay, overtime hours, and overtime pay
# Program prints and displays employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay.
#

name = input("Enter employee's name: ")
hours = (float(input('Enter number of hours worked: ', )))
payrate =(float(input("Enter employee's payrate: ", )))
regular_hours = 40

print('----------------------------------')
if hours <= 40:
        print('Employee name: ', name)
        overtimehours = (0)
        regularpay = round(hours * payrate)
        overtimerate = (0)
        overtimepay = (0)
        grosspay = float(round(regularpay,2))   
        print()
        print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay:'}")
        print('-------------------------------------------------------------------------------------------------')
        print(f"{hours:<15.1f}{payrate:<15.1f}{overtimehours:<15.1f}{overtimepay:<15.2f}${regularpay:<15.2f}${grosspay:<15.2f}")

elif hours > 40:
        print('Employee name: ', name)

        overtimehours = round(hours - 40.00,2)
        regularpay = round(regular_hours * payrate)
        overtimerate = round(payrate * 1.5,2)
        overtimepay = float(round(hours - regular_hours) * overtimerate)
        grosspay = float(round(regularpay + overtimepay,2))
        print()
        print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay:'}")
        print('-------------------------------------------------------------------------------------------------')
        print(f"{hours:<15.1f}{payrate:<15.1f}{overtimehours:<15.1f}{overtimepay:<15.2f}${regularpay:<15.2f}${grosspay:<15.2f}")


