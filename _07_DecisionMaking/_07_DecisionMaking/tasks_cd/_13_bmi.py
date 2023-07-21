'''13
Create a program that calculates a person's Body Mass Index (BMI) based on their height and weight.
I. Req: calculate body mass index(bmi) acc to user input
II. Analysis:
Technical Analysis:
1. Have to take two inputs
2. make validation of inputs
3. calculate bmi by using formula 
4. print the result
Functional Analysis:
State : float, float
Behavior: Operators, Decision Making, Loops
            /, **,     if else
III. Design:
bmi = weight in kgs / (height in meters)**2
bmi = 65 / 5.7**2
'''
print("BMI calculator")
height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in kgs : "))
bmi = weight / (height**2)
if bmi < 18.5:
    print("Your BMI is %s and You are under weight" % bmi)
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI is %s and You are in healthy range" % bmi)
elif bmi >= 25 and bmi <= 29.9:
    print("Your BMI is %s and You are over weight" % bmi)
elif bmi >= 30 and bmi <= 39.9:
    print("Your BMI is %s and You have obesity" % bmi)
else:
    print("Your BMI is %s and You have severe obesity" % bmi)