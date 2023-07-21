'''2
Description: Have students create a program that prompts the user to enter their age. 
Based on the input, the program should display different messages according to the following conditions:

I. Req: Printing the message according user input.
II. Analysis:
Functional Analysis:
1. User gives the input.
2. check the user input is valid or not
3. What basis we have to print message.
4. if input is valid print message else gives error message. 
Technical Analysis:
State : user_input = int
Behavior: Operators, Decision Making, Loops
            <,>,=       if elif else
III. Design:
1. num = 9
    10<= num >=0 
    True /User is a boy
    
2. num = 25 #State
    30 <= num >=18 #Behavior
    30 <= 25 >= 18 
    True /user is an adult
'''
print("----------- age -------------")
# State
user_input = int(input("Enter Your Age : "))
# Behavior
if user_input > 0:
    print('User input is valid')
    if 0 < user_input <= 18:
        print("User is teenage")
    elif 18 < user_input <= 30:
        print("user is an adult")
    elif 30 < user_input <= 100:
        print("user is an elder")
    else:
        print("User is too elder")
else:
    print("user input is invalid")