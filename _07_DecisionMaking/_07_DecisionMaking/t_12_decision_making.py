"""1
I. REQ: print whether given number is Even or Odd:
II. Analysis:
Functional Analysis:
        1. Customer will give number
        2. Check whether it is even or odd
        3. Print it
    Technical Analysis:
        State : int
        Behavior : Operators, Decision Making,  Loops
                    %, ==       if else           -

III. Design:
    As given x = 43     # State
    x % 2 = 45 % 2      # Behavior
          = 1
    As reminder is 1, given value is Odd Number

    AS given x = 22     # State
    x % 2 = 22 % 2      # Behavior
          = 0
    As reminder is 1, given value is Even Number. """
print("---------- Odd or Even ----------")
# State
user_input = int(input("Enter a number : "))
# Behavior
if user_input % 2 == 0:
    print("%d is Even " % user_input)
else:
    print("%d is Odd " % user_input)
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
'''3
Description: In this task, students should develop a program that calculates the discount amount for a shopping cart 
based on the following conditions:

If the total price is greater than or equal to $100, apply a 10% discount.
If the total price is between $50 and $99.99, apply a 5% discount.
If the total price is less than $50, no discount is applied.

I. Req: calculate discount amount of a cart based on conditions specified.
II. Analysis:
Functional Analysis:
1. Price of cart will be given by user.
2. Have to calculate the discount of cart
3. print the result.
Technical Analysis:
State : total_price = float
Behavior: Operators, Decision Making, Loops
            >,<,=    if elif else
III. Design:
1. price >=100
total_price = 101
total_price >= 100 
101 >= 100 
    101 * 0.1
    10.1 is the discount
    
2. 99.99 <= price >=50
price = 60
60 * 0.05 =  3 is the discount of 60

3. price < 50
for 25 discount is zero
'''
print("----------- know the discount of a cart price -------------")
total_price = float(input("Enter a price to know discount : "))
if total_price > 0:
    print("input is valid")
    if total_price >= 100:
        disc = total_price * 0.1
        print("$", disc, " is the discount for ", "$", total_price)
    elif 99.99 <= total_price >= 50:
        disc = total_price * 0.05
        print("$", disc, " is the discount for ", "$", total_price)
    else:
        print("$0 is the discount for ", "$", total_price)
else:
    print("Input is invalid")
'''4. 
Description: Ask students to create a program that simulates a simple quiz. The program should present a series of
multiple-choice questions to the user and keep track of their score. At the end of the quiz, display the user's score as 
a percentage.
I. Req: Make a quiz and show the score in percentage.
II. Analysis:
Functional Analysis:
1. No of questions are 5.
2. Take answers for the 5 questions from user.
3. If answer is right give 1 mark.
4. print total score in percentage.
Technical Analysis:
State : user_input1-5 = str
Behavior: Operators, Decision Making, Loops
            +, /, *    if          for
III. Design:
'''
print("---------- Shall we test your knowledge ------------")
no_of_questions = 5
score = 0
questions_list = {"1) which operator is used for multiplication?\na) # \nb) - \nc) / \nd) *": "d",
                  "2) what symbol is used for single line comment?\na) // \nb) ''' \nc) # \nd) ||": "c",
                  "3) what is the answer for 89%10 ?\na) 9 \nb) 8 \nc) 8.9 \nd) 89 ": "a",
                  "4) which method is used to add single item to a list?\na) add \nb) a&d \nc) append \nd) extend ": 'b',
                  '5) which method is used to make string capitalize?\na) upper() \nb) lower() \nc) capitalize() \nd) bigger()': 'a'
                  }
for x in questions_list:
    print(x)
    answer = input("Enter your Answer : ")
    if answer == questions_list[x]:
        score = score + 1
        print(score)
percentage = (score / no_of_questions) * 100
print(percentage)
'''5
Description: Have students create a program that generates a random number between 1 and 100. The user should guess the 
number, and the program should provide feedback on whether the guess is too high or too low. The program should continue
until the user guesses the correct number.
I. Req: Create a number guess game
II. Analysis:
Functional Analysis:
Technical Analysis:
1. Have to take input from user.
2. should give some suggestions acc to user input until he guesses the number
3. print  a congratulations message once he found.
State : user_input = int
        import random to get random number
Behavior: Operators, Decision Making, Loops
            >,<,==      if elif else    while
III. Design:
input = 55
random = 22
if input == random:
    write success message
elif input > random
    write too high
elif input < random
    write too low        
    
'''
print("----------Number Guess Game-----------")
import random

user_input = int(input("Guess the number: "))
num = random.randint(1, 100)
while  user_input <=100 and user_input >=0:
    if user_input >= 0 and user_input <= 100:
        print("Entered a valid number")
        if user_input == num:
            print("Congratulations, you won")
            break
        elif user_input > num:
            print("Entered number is too high")
            user_input = int(input("Enter the number again: "))
        elif user_input < num:
            print("Entered number is too low")
            user_input = int(input("Enter the number again: "))
    else:
        print("Please Enter the number between 1 to 100")
        user_input = int(input("Enter the number again: "))

'''6
Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
I. Req: calculate sum and print sum acc to conditions
II. Analysis:
Technical Analysis:
1. Three inputs we have to take from user.
2. calculate the sum and print when three are not same. 
3. if three are same print thrice of the sum.
Functional Analysis:
State : three user_input = int
Behavior: Operators, Decision Making, Loops
            +,==,       if else
III. Design:
'''
# State
user_input1 = int(input("Enter first number :"))
user_input2 = int(input("Enter second number :"))
user_input3 = int(input("Enter third number :"))
total_sum = user_input1 + user_input2 + user_input3
if user_input1 == user_input2 == user_input3:
    total_sum = total_sum * 3
    print(total_sum)
else:
    print(total_sum)
'''7
I. Req: 
II. Analysis:
Functional Analysis:
Technical Analysis:
1.
2.
3.    
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
'''8
Python program to count the number 4 in a given list.
I. Req: Print the number of fours in a given list 
II. Analysis:
Technical Analysis:
1. will give list
2. check no of fours in the list
3. print the count
Functional Analysis:
State : list
Behavior: Operators, Decision Making, Loops
            +=, ==    if        for
III. Design:
list = [1, 4, 2, 3, 6, 4]
no of fours in list  are 2 
'''
n = int(input("Enter no inputs :"))
given_list = []
for x in range(0, n):
    ele = int(input())
    given_list.append(ele)
count = 0
for four in given_list:
    if int(four) == 4:
        count += 1
print(count)
'''9
Python program to test whether a passed letter is a vowel or not.
I. Req: To check the entered letter is vowel or not
II. Analysis: 
Technical Analysis:
1. Take an input from user
2. check the input is vowel or not
3. print result
Functional Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            in         if else         no
III. Design:
'''
user_input = input("Enter a letter to check : ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if user_input in vowels:
    print("%s is vowel" % user_input)
else:
    print("%s is not vowel" % user_input)
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
'''11
Create a program that checks if a given year is a leap year or not.
I. Req: check input is a leap year or not
II. Analysis:
Technical Analysis:
1. Take input 
2. check it is divisible by 4 
3. centuries are input those should be divisible 400 not by 100
Functional Analysis:
State : int
Behavior: Operators,    Decision Making, Loops
         and, ==, %,     if elif else       none
III. Design:
'''
user_year = int(input("Enter a year : "))
if (user_year % 400 == 0) and (user_year % 100 != 0):
    print("%d is leap year" % user_year)
elif user_year % 4 == 0:
    print("%d is leap year" % user_year)
else:
    print("%d is not a leap year" % user_year)
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

'''15
Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
I. Req: convert temperature from celsius to fahrenheit 
II. Analysis:
Technical Analysis:
1. take input
2. check the input is fahrenheit or celsius 
3. convert using formula acc to input
4. print result
Functional Analysis:
fahrenheit = (temp *9/5) + 32
°C = (temp - 32) × 5/9
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
print("while temperature enters in celsius should end with capital 'C' \n while temperature enters in fahrenheit should end with capital 'F'")
temp = input("Enter temperature in Fahrenheit(F) or in celsius(C)")
x = temp.endswith("C")
y = temp.endswith("F")
if x:
    temp1 = temp.rstrip("C")
    temp_in_c = (int(temp1) * 9 / 5) + 32
    print("Temperature in %s in celsius" % temp_in_c)
elif y:
    temp2 = temp.rstrip('F')
    temp_in_f = (int(temp2) - 32) * 5 / 9
    print("Temperature in %s in celsius" % temp_in_f)
else:
    print("Input is invalid! please number ends with F or C")
'''16
Create a program that verifies a user's login credentials (e.g., username and password).
I. Req: check the username and password are correct or not 
II. Analysis:
Functional Analysis:
1. take username and password from user
2. check the username and password is correct or not
3. if correct give validation message
4. if wrong give an error message 
Technical Analysis:
State : str str
Behavior: Operators, Decision Making, Loops
            ==          if              none
                            if
                            else
                        else
'''
user_id = input("Enter UserId")
password = input("Enter Password")
actual_id = "Ramesh094"
pwd = "Learn@779"
if user_id == actual_id:
    if password == pwd:
        print("Login successful, Enjoy the session.....!")
    else:
        print("password is wrong!")
else:
    print("userId is wrong!")

'''17
Develop a program that performs different operations on a given string based on user input (e.g., length, reverse, uppercase).
I. Req: print a string after specified operations 
II. Analysis:
Technical Analysis:
1. Take the two inputs, one is string and second one operation to perform.
2. Do operation on string acc to user specified.
3. print the result.
Functional Analysis:
State : str str
Behavior: Operators, Decision Making, Loops
            ==          if elif else  none
                            
III. Design:
'''
print("Enter the second input from this list \na)reverse \nb)length \nc)uppercase \nd)lowercase ")
input_str = input("Enter a string : ")
operation = input("which operation to perform")
if operation == "a":
    ans = input_str[::-1]
    print(ans)
elif operation == "b":
    ans = len(input_str)
    print(ans)
elif operation == "c":
    ans = input_str.upper()
    print(ans)
elif operation == "d":
    ans = input_str.lower()
    print(ans)
else:
    print('you chosen invalid option')
'''18
Create a program that calculates the final price of a product after applying a discount.
I. Req: calculate final price after discount 
II. Analysis:
Technical Analysis:
1. Take two inputs as total price, discount from user.
2. find final price with out discount.
3. print the price. 
Functional Analysis:
State : int int
Behavior: Operators, Decision Making, Loops
III. Design:
'''
price = int(input("Enter the total price : "))
discount = int(input("Enter the discount : "))
if price >= 0 and price > discount:
    final_price = price - price*(discount / 100)
    print("Final price is", final_price)
print("Cart price should be greater than 0 and discount")
'''19
Create a program that validates if a given email address is correctly formatted.
I. Req: validating email address
II. Analysis:
Technical Analysis:
1. User will give email.
2. email should contain @ symbol and domain name after @.
3. Should have some name before @.
4. If above conditions satisfied print valid else invalid.
Functional Analysis:
State : str
Behavior: Operators, Decision Making, Loops
           >=             if else 
III. Design:
input = xyz@nmnm.com

'''
email = input("Enter an email Id!")
end = email.endswith(".com")
if "@" in email and end:
    x = email.split("@")
    xl = len(x[0])
    xr = len(x[1])
    if xl >= 6 and xr >= 8:
        print("%s is valid email" % email)
    else:
        print("%s is not valid" % email)
else:
    print("Please enter a valid email")
'''20
Develop a program that converts a given number from one number system to another (e.g., binary to decimal).
I. Req: converting binary to decimal
II. Analysis:
Functional Analysis:
Technical Analysis:
1. take input in binary.
2. make input validation.
3. converting binary number to decimal based on number conversion system.
4. print the decimal number.   
State :
Behavior: Operators, Decision Making, Loops
            += * **      none           for             
III. Design:
given =1101
        1       1       0       1
        2^3     2^2     2^1     2^0   
        8       4       2       1    = 13
                    
'''
bin_num = input("Enter a Binary Number")
len_num = len(bin_num)
exp = 0
res = 0
rev_num = bin_num[::-1]
for i in rev_num:
    res = res + (int(i)*2**exp)
    exp += 1
print(res)
'''21
Write a program that allows two players to play the classic game of rock, paper, scissors and determines the winner.
I. Req: crate a two player based rock, paper scissor game.
II. Analysis:
Technical Analysis:
1. no of players two
2. write the  different conditions/rules of game
3. announce the winner
Functional Analysis:
1   player1 = rock
    player2 = paper 
    rock < paper #rock surrounded by the paper #player2 wins!
2   player1 = scissor
    payer2 = paper 
    paper < scissor #scissor cuts the paper   #player1 wins!
3.  scissor < rock   # rocks breaks the scissor #player2 wins!
State : player1 player2
Behavior: Operators, Decision Making, Loops
            > < ==     if elif else 
III. Design:
'''
print("Enter the first letter from below options only \nrock \npaper \nscissor")
player1 = input("Enter player1 input : ")
player2 = input("Enter player2 input : ")
player1 = player1.strip()
player2 = player2.strip()
r = "r"
p = "p"
s = "s"
if player1 == r or player1 == p or player1 == s:
    if player2 == r or player2 == p or player2 == s:
        if (player1 == r and player2 == p) or (player1 == p and player2 == s) or (player1 == s and player2 == r):
            print("player2 wins!")
        elif (player1 == p and player2 == r) or (player1 == s and player2 == p) or (player1 == r and player2 == s):
            print("player1 wins!")
        elif (player1 and player2 == r) or (player1 and player2 == p) or (player1 and player2 == s):
            print("It's  draw")
    else:
        print("PLayer2  should enter the first letter from below options only")
else:
    print("PLayer1 enter the first letter from below options only")
'''22
Create a program that converts an amount of money from one currency to another based on current exchange rates.
I. Req: conversion of money from one currency to another currency
II. Analysis:
Technical Analysis:
1. User will enter the money in rupees.
2. convert money from rupee to usd.
3. print result.
Functional Analysis:
State : int
Behavior: Operators, Decision Making, Loops

III. Design:
1 inr = 0.012
if given input = 50 inr
usd = 50 * 0.0122 = 0.6 usd

1usd = 82.16
if given input = 50 usd
inr = 50 * 82.16 = 4108
'''
rupees = input("Enter Money end with INR/USD : ")
one_rupee = 0.012
one_usd = 82.25
if "INR" in rupees:
    rupees = rupees.strip("INR")
    usd = float(rupees) * one_rupee
    print(rupees, " rupees are ", usd, " Us dollars")
elif "USD" in rupees:
    rupees = rupees.strip("USD")
    inr = float(rupees) * one_usd
    print(rupees, " usd are ", inr, "Indian rupees")
else:
    print("Enter a valid amount")
'''23
Develop a program that evaluates the strength of a user's password based on certain criteria (e.g., length, complexity).
I. Req: Check the password strength.
II. Analysis:
Technical Analysis:
1. Take input from user. 
2. check the password length should be greater than 8.
3. Should contain one upper case and special character.
4. password field should not empty.
5. password should be alphanumeric.
6. print validation message.
Functional Analysis:
State : str 
Behavior: Operators, Decision Making, Loops

III. Design:
'''
ent_pass = input("Enter your password to validate : ")
special_chr = "!@#$%^&*()_-+=|?/<>.,`~"                 # special character list
sp_c = 0                                                # special character count
num = 0                                                 # numbers in password
if ent_pass:
    if len(ent_pass) >= 8:
        if ent_pass[0].isupper():
            for i in ent_pass:
                if i.isdigit():
                    num += 1
                for j in special_chr:
                    if i == j:
                        sp_c += 1
                        break
            if sp_c >= 1 and num >= 1:
                print("Password is strength is good")
            else:
                print("Password should contain at least one special character and one number")
        else:
            print("first letter should be capital")
    else:
        print("password must be 8 characters length")
else:
    print("Invalid input")
'''24
Write a program that handles different types of errors and displays appropriate error messages to the user.
I. Req: write a program to show error messages to user. 
II. Analysis:
Technical Analysis:
1. can take no of inputs.
2. find the error of the program.
3. print error message. 
Functional Analysis:
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
a = 5
b = 6
print("div = a / str(b)")
print("TypeError: unsupported operand type(s) for /: 'int' and 'str'")
# print(a/0)
print("ZeroDivisionError: Division by zero")
# print(c)
print("NameError: name 'c' is not defined")
d = "ram"
print(d[3])
print("IndexError: string  Index is out of range")
#print(int("xyz"))
print("ValueError: Invalid literal for int() with base 10: 'xyz'")
# print("str
print("SyntaxError: unterminated string literal (detected at line num")
# pritn()
print("NameError: Name pritn is not defined")
# print("str"
print("SyntaxError: unexpected EOF while parsing")
'''25
Create a program that simulates decision-making for a game character based on different scenarios (e.g., fight or flee,
choose a weapon).
I. Req: Giving inputs to game character beased on scenarios  
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
print("Make game character active by entering the first letter of the given actions")
actions = {'p': 'give a punch to enemy',
           'j': 'Jump from standing position',
           'w': 'take the weapon',
           'f': 'fly high',
           'r': 'run like a deer',
           'h': 'hide from the enemy',
           'jp': 'jump and punch the enemy',
           'jr': 'jump and run away from enemy',
           'd': 'down misses from enemy'}
action = input("What to do: ")
action = action.strip()
if action in actions.keys():
    for d in actions:
        if action == d:
            print(actions[d])
else:
    print("Give valid input")
# while True:
#     if action == "k":
#         print(k)
#         break
#     elif action == "j":
#         print(j)
#         break
#     elif action == "r":
#         print(r)
#         break