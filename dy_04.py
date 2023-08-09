# Grading Student Based on Marks Obtained by Making Functions
# Suppose you just attended a University examination. 
# The marks you obtained in various subjects are stored in a list like this:

# marks = [55, 64, 75, 80, 65] actual values
marks = [9, 44, 75, 80, 75] # edited values

# You want to find the average marks you obtained in the exam.
# Based on the average marks you want to find your grade as:
# You will get Grade A if the average marks is equal to or above 80 (A >= 80)
# You will get Grade B if the average marks is equal to or above 60 and less than 80 (B >= 60 and B < 80)
# You will get Grade C if the average marks is equal to or above 50 and less than 60 (C >= 50 and < 60)
# And if the average marks is less than 50, you will get Grade F (F < 50)

length_of_marks = len(marks)
tot_marks = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
avg_marks = tot_marks / length_of_marks
print(avg_marks)

if avg_marks >= 80:
    print('The student get Grade A')
elif avg_marks >= 60 and avg_marks < 80:
    print('The student get Grade B')
elif avg_marks >= 50  and avg_marks < 60:
    print('The student get Grade C')
else:
    (print('The student get Grade F'))
