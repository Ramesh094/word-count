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
if user_input1 == user_input2 == user_input3 :
    total_sum = total_sum * 3
    print(total_sum)
else:
    print(total_sum)