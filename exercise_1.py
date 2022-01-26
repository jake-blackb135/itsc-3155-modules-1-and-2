gradenum = int(input("Enter a grade from 0 - 100\n"))
if gradenum >= 0 and gradenum < 60:
    print("Your grade is F")
elif gradenum >= 60 and gradenum < 70:
    print('Your grade is D')
elif gradenum >= 70 and gradenum < 80:
    print("Your grade is C")
elif gradenum >= 80 and gradenum < 90:
    print("Your grade is B")
elif gradenum >= 90 and gradenum <= 100:
    print("Your grade is A")
else:
    print("Invalid Input")
    