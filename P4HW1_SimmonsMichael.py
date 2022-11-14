#This program creates a score list..
#CTI-110
#P4HW1 - Score List
#Michael A. Simmons
#November 14, 2022
#
# Program asks user to enter for number of scores they would like to enter
# Program creates a loop to collect the number of scores the user wants to ente 
# Program evaluates if the score is valid, it should be between 0 and 100. If it is not, notify the user and ask for a VALID score to be entered a valid score.
# Program displays lowest score received and display a letter grade for the calculated average.



score_list = []
total = 0

scores = int(input("How many scores you would like to enter:" ))

for x in range(scores):
        score = float(input("Enter score #{}: ".format(x + 1)))
        if score < 0:
            print("INVALID score entered!!!!")
            print("Score should be between 0 and 100")
            float(input("Enter score #3 again:"))
        score_list.append(score)

for x in score_list:
                total += x

score_list.remove(min(score_list))               		  

average = round(sum(score_list)/len(score_list),2)


def letterGrade(score_average):
    letter = ""
    if score_average >= 90:
	    letter = "A"
    elif score_average >= 80:
	    letter = "B"
    elif score_average >= 70:
	    letter = "C"
    elif score_average >= 60:
	    letter = "D"
    elif score_average <= 59:
	    letter = "F"

    return letter

print()
print("-----------Results-----------")
print(f"{'Lowest Grade:':<19}",min(score_list))
score_list.remove(min(score_list))
print(f"{'Modified List:':<19}", score_list)
print(f"{'Scores Average:':<19}",format(average,".2f"))
print(f"{'Grade:':<19}", (letterGrade(average)))
print("-------------------------------------")
