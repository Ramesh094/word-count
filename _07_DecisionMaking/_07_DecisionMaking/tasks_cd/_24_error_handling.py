"""24
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
"""
a = 5
b = 6
print("div = a / str(b)")
print("TypeError: unsupported operand type(s) for /: 'int' and 'str'")
# print(a/0)
print("ZeroDivisionError: Division by zero")
# print(c)
print("NameError: name 'c' is not defined")
d = "ram"
# print(d[3])
print("IndexError: string  Index is out of range")
#print(int("xyz"))
print("ValueError: Invalid literal for int() with base 10: 'xyz'")
# print("str
print("SyntaxError: unterminated string literal (detected at line num")
# pritn()
print("NameError: Name pritn is not defined")
# print("str"
print("SyntaxError: unexpected EOF while parsing")