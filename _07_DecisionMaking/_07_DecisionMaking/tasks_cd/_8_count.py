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