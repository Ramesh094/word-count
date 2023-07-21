print("op prec: ", True and False or False)    # 10+20+30
'''
10th Class:
If the candidate clears all subjects then only result is PASS
else even if one subject, he fails,  result is FAIL

and operation:
----------------
T H E M S So:  
P P P P P F  : FAIL
P P P P P P  : PASS
F _ _ _ _ _  : FAIL
P P P F _ _  : FAIL
P and P and P and Fail and S5 and S6 : Fail


P P P P P F :  FAIL

or operation:  If you clear any one paper, degree will be given.
----------------
Paper1 or Paper2  :  
Pass   or ______  : Pass
Fail   or Pass    : Pass
Fail   or Fail    : Fail 

JOB and operation: 
---------------------
R1           R2            R3           R4
Coding    Technical     Managerial     HR

Apply for Job   OR:
-----------------------
1. Atleast 60% OR B.Tech/B.E : 

10th   : 53
Inter  : 42
B.Tech : 55  - YES

10th   : 65
Inter  : 72
Degree : 80  - YES

10th   : 55
Inter  : 65
Degree : 62  - NO

PanCard and AadharCard:

'''
# condition1 and condition2 or condition3
# AND operator:
# Guest: Water and Coffee
print("AND 1 :", True and False)   # False
print("AND 2 :", True and True)    # True
print("AND 3 :", False and True)   # False
print("AND 4 :", False and False)  # False

print("AND Operation :: ", 10 < 20 and 10 > 5)

x = 100
y = 200

x = True
print("Value of x: ", x)
x = False
print("Value of x: ", x)

# Logical gate ===> and or not
# OR operator:
# Guest:  Coffee or Tea
print("OR 1 :", True or False)   # True **
print("OR 2 :", True or True)    # True **
print("OR 3 :", False or True)   # True
print("OR 4 :", False or False)  # False
print("-----------------------")



# not
not True  # False
not False  # True

'''
Syntax : condition1   AND/OR    condition2   AND/OR  condition3

True and False or False : False
True and True or False  : True
False and False or True : True
True and False or False : 
True and False or False : 
True and False or False : 
True and False or False : 
True and False or False : 
True and False or False : 
True and False or False : 
True and False or False : 

x = 10
y = 20
z = 30 

x < y and  z > y : True
x < y and  x > z : False


condition
not condition

'''
print("Cond 1:", 10 > 20 and 5 < 2)  # False and False ==> False
print("Cond 2:", 10 < 20 and 5 > 2)  # True and True  ==> True
print("Cond 2:", 10 < 20 and 5 < 2)  # True and False  ==> False
# print("Cond 3:", not 5>2)

# 10+2-4/5*6

# c1 and c2 and c3
# c1 or c2 or c3
# c1 and c2 or c3 ond c4
# c1 and c2 not c3 or c4

