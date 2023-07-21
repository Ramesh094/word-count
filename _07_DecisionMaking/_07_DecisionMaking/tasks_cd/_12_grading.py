'''12
Develop a program that accepts a student's score as input and returns their corresponding grade according to a grading scale.
I. Req:  Allotting grade acc to score 
II. Analysis:
Technical Analysis:
1. user gives input
2. compare the score with grading sclae
3. print the grade
Functional Analysis:
State : int
Behavior: Operators, Decision Making, Loops
            >=, <=      if elif else  
III. Design:
'''
marks = int(input("Enter your marks : "))
if marks >=0 and marks <=100:
    print("input is valid")
    if marks >= 90:
        print("You got grade 'A'")
    elif marks >= 60:
        print("You got grade 'B'")
    elif marks >= 45:
        print("You got grade 'C'")
    elif marks >= 35:
        print("You got grade 'D'")
    else:
        print("you are failed!")
else:
    print("input is invalid")
