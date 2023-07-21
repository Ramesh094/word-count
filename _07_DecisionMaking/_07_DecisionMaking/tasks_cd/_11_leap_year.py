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