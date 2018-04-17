# Scores and Grades 

from random import randint

def scores_and_grades(number):
    for i in range(0,number+1):
        random_grade = randint(60,100)
        if random_grade >= 90:
            print "Score:", random_grade, "Your grade is: A"
        elif random_grade >= 80:
            print "Score:", random_grade, "Your grade is: B"
        elif random_grade >= 70:
            print "Score:", random_grade, "Your grade is: C"
        else:
            print "Score:", random_grade, "Your grade is: D"

scores_and_grades(15)