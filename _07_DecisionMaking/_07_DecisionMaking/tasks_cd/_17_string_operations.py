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