'''14
Develop a program that validates user input to ensure it meets specific criteria (e.g., length, format)
I. Req: Validate the user input
II. Analysis:
Technical Analysis:
1. Take the input
2. validate the input
3. print result
Functional Analysis:
State : str 
Behavior: Operators, Decision Making, Loops
            >= ==       if else 
III. Design:
'''
entered_in = input("Enter something : ")
length = len(entered_in)
if length >= 8 and type(entered_in) == str:
    print("It is a valid input")
else:
    print("It is not valid")
