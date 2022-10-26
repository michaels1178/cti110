#This program takes a number grade , determines average and displays letter grade for average.
#CTI-110
#P3HW1_Debugging
#Simmons
#October 26, 2022

# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules.
# User provides input.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)                   
average = sum(grades)/len(grades)

print()
print('-----------Results-----------')
print(f"{'Lowest_Grade:':<19}",min(grades))
print(f"{'Highest Grade:':<19}",max(grades))
print(f"{'Sum of Grades:':<19}",sum(grades))
print(f"{'Average:':<19}",format(average,".2f"))
print('-------------------------------------')

# determine letter grade for average

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
else:
    print('Your grade is: F') # TO DO: finish this





