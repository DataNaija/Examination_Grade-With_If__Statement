marks = [9, 44, 75, 80, 75] # edited values

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
    print('The student get Grade F')
