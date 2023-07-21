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
    res = res + (int(i) * 2 ** exp)
    exp += 1
print(res)