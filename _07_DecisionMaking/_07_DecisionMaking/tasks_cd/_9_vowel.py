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