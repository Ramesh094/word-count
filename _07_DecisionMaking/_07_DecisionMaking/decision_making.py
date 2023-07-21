"""First one
I. REQ: print whether given number is Even or Odd:
II. Analysis:
Functional Analysis:
        1. Customer will give number
        2. Check whether it is even or odd
        3. Print it
    Technical Analysis:
        State : int
        Beheavior : Operators, Decision Making,  Loops
                    %, ==       if else             -

III. Design:
    As given x = 43     # State
    x % 2 = 45 % 2      # Behavior
          = 1
    As reminder is 1, given value is Odd Number

    AS given x = 22     # State
    x % 2 = 22 % 2      # Behavior
          = 0
    As reminder is 1, given value is Even Number. """
# State
given_num = int(input("Enter Number : "))
# Behavior
if given_num % 2 == 0:
    print(given_num, " is Even number")
else:
    print(given_num, "is Odd number")


"""
Second one
I. REQ: print the given number is positive or negative
II. Analysis
    Functional Analysis:
        1. Customer will give number    #State
        2. Check it is positive or negative with reference to 0 # Behavior
        3. print result
            1. positive   if num > 0
            2. negative   if num < 0
            3. zero       if num == 0
    Technical Analysis:
        1. State    : int
        2. Behavior : operators, DM,            loops
                        >,<,==   if elif else    -
III. Design:
    Maths solution:
    1.  if given num = 50   #State
        x > 0 = 50 > 0      #Behavior
              = True
        As result True, given number is Positive
    2. elif given num = -10   #State
        x < 0 = -10 < 0     #Behavior
              = True
        As result True, given number is Negative
    3. else 
        given number is not positive and not negative, it is zero.
"""
# State
input_num = int(input("Enter the number:"))
# Behavior
if input_num > 0:
    print(input_num, " is Positive Number")
elif input_num < 0:
    print(input_num, 'is Negative Number')
else:
    print(input_num, 'is Zero')
    """"
 Write a program that reads two words and checks if the given two words are same or not
 I. REQ: Print the result after checking two words are same or not
 II. Analysis:
        Functional Analysis:
            1. two words will give by user
            2. check the two words are same or not
            3. print result
        Technical Analysis:
            State : str1
                    str2 
            Behavior : Operators,  DM,           loops
                        ==         if else        -
 III. Design:
    1.  str1 = "ramesh"
        str2 = "ram"
        str1     ==    str2 
        "ramesh" ==     "ram"
        False, Two words are not same
    2.  str1 = "hari"
        str2 = "hari"
        str1    ==  str2
        "hari"  ==  "hari"
        True, Two wards are same.       
 """
# State
word1 = input("Enter your first word :")
word2 = input("Enter Your second word :")
# Behavior
if word1 == word2:
    print(word1+" and "+word2+" are same.")
else:
    print(word1+" and "+word2+"are not same")
"""
Write a program to check whether it is sunday or not by input number
I. REQ. Print the result whether it is sunday or not.
II. Analysis:
    Functional Analysis:
        1. Input will give by user
        2. Check whether it is sunday or not
        3. Print result
    Technical Analysis:
        State   : int
        Behavior : Operators, DM, Loops
                    ==      if else -
III. Design:
        monday      - 1
        tuesday     - 2
        wednesday   - 3
        thursday    - 4
        friday      - 5
        saturday    - 6
        sunday      - 7
        
        Given input num = 7     #State
        if num == 7             #Behavior
            7 == 7
            True, Ya it is sunday
        
        Given input num = 2     #State
        if num == 7             #Behavior
            2 == 7
            False, No it is not sunday                                            
"""
# State
day_num = int(input("Enter sunday number :"))
# Behavior
if day_num == 7:
    print("Ya, It is sunday")
else:
    print("It is not sunday")

