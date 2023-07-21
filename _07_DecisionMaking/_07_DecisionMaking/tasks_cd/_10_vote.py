'''10
Description: Write a program that prompts the user to enter their age and determines if they are eligible to vote or not.
I. Req: Toc check the eligibility of an user
II. Analysis:
Functional Analysis: 
1. will take user input
2. compare the input with eligibility age
3. print the message 
Technical Analysis:
State :  str
Behavior: Operators, Decision Making, Loops
            >= <= ==    if else
III. Design:
'''
user_age = int(input())
ele_age = 18
if user_age >= ele_age:
    print("You are eligible to vote")
else:
print("You are not eligible to vote")