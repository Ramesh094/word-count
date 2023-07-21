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