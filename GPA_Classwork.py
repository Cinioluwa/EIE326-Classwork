def convertGrade(grade):
    grade = grade.upper() 
    if grade == 'A':
        return 5.0
    elif grade == 'B':
        return 4.0
    elif grade == 'C':
        return 3.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return -1.0 # Invalid grade
    
def wrapUpmessage(Sum):
    if Sum/tcreditUnit >= 4.0:
        print("Congratulations! You've achieved a high GPA!")
    elif Sum/tcreditUnit >= 3.0:
        print("Good job! You've done well this semester.")
    elif Sum/tcreditUnit >= 2.0:
        print("You've passed this semester. Keep it up!")
    elif Sum/tcreditUnit >= 1.0:
        print("You've barely passed this semester. You can do better!")
    elif Sum/tcreditUnit >= 0.0:
        print("You've failed this semester. Don't give up!")
    
print("Hi! Welcome to the GPA Calc!")
print("You've offered 6 courses this past semester. Nice job!")
course_names = []
for i in range(6):
    course_name = input(f"Enter the name of course {i+1}: ")
    course_names.append(course_name)

print("You've entered all your courses!")
print("Now, let's convert your grades to GPA.")
print("Please enter your grades in the following format: A, B, C, D, F")
sum = 0
tcreditUnit = 0
gpa_list = []
for i in range(6):
    while True:
        grade = input(f"Enter your grade for course {i+1}: ")
        gp = convertGrade(grade)
        creditUnit = int(input(f"Enter the credit unit for course {i+1}: "))
        if gp == -1.0:
            print("Um. That's not a valid grade. Please enter a valid grade (A, B, C, D, F).")
        else:
            break
    gpa = gp * creditUnit
    print(f"Your GP for course {i+1} is: {gpa}")
    sum += gpa
    tcreditUnit += creditUnit
    gpa_list.append(gpa)
    if i == 5:
        print("You've entered all your grades!")
        print("Calculating your GPA...")
        break
    else:
        continue
print(f"Your total GPA is: {sum/tcreditUnit}")
print("Here's a list of your GPAs for each course:")
for i in range(6):
    print(f"{course_names[i]}: {gpa_list[i]}")
wrapUpmessage(sum)
print("Thank you for using the GPA Calc!")
print("Goodbye!")



