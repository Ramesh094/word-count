print(10)
print("Value : ", 10)

x = 10
# print(x)  # Bad way
print("Value : ", x)
print("Square: ", x**2)

print("----Entity : Employee----------")
emp_id = 100
print("Employee id is : ", emp_id)
ename = 'Madhu'
print("Employee name is : ", ename)



print("----Entity : Mobile----------")

print(10)  # DONT
print("Value : ", 10)  # DONT
print("Mobile count : ", 10)  # DONT

# IDEAL APPROACH
mob_count = 20
print("Mobile count : ", mob_count)



print("Value : ", 10)  # DONT
print("Mobile count : ", 'MI', type('MI'))  # DONT

brand = 'MI'
print("Brand     : ", brand, type(brand))   # DO
price = 12600.56
print("Price     : ", price, type(price))


print("-----------------------------------------------------")
# 1. One time usage of Value
print(10)   # 1  DON'T
print("Eid is  : ", 10)  # 2   DON'T
print("Square : ", 10*10)

# 2 Multiple times reuse variable: Assign value to variable
x = 10
print("Value : ", x)   # III. DO
print("Square : ", x**2)
print("Cube   : ", x**3)
print("--------------------")

# Ideal approach
   # Static way
age = 15
print("Age is : ", age)

   # Dynamic way
age = input("Enter your age : ")   # 45  --> "45"
print("Age is : ", age, type(age))

age = int(input("Enter your age : "))   # 45  --> "45"  ---> 45
print("Age is : ", age, type(age))
print("----------------------------------------------------")

# REQ: Load employee id and print it
# emp_id e_id eid empid
e_id = int(input("Enter your employee ID: "))
print("Employee id is : ", e_id)

s_name = input("Enter student name : ")
print("Student name is : ", s_name)
print(type(e_id), type(s_name))

marks = input("Enter marks : ")
print("Marks are : ", marks, type(marks))
marks = int(marks)
print("Marks are : ", marks, type(marks))

r_bill = float(input("Enter food bill : "))  # 119.3  --> "119.3" --> 119.3
print("Restaurant bill is : ", r_bill, type(r_bill))

x = 100
print("Before value is : ", x, type(x))
x = str(x)
print("After value  is : ", x, type(x))

msg = 4332  # Non 0 --> True   0 --> False
print("Before Message is : ", msg, type(msg))
msg = bool(msg)
print("After Message is : ", msg, type(msg))


score = 0  # Non 0 --> True   0 --> False
print("Before Message is : ", score, type(score))
score = bool(score)
print("After Message is : ", score, type(score))

score = -5  # Non 0 --> True   0 --> False
print("Before Message is : ", score, type(score))
score = bool(score)
print("After Message is : ", score, type(score))


'''
Functions discussed : 
---------------------
print()  # To print given content 
id()     # To get address of value in integer format 
type()   # To get type of value(int/float/boolean/string/list/tuple....)
input()  # To load value dynamically at runtime
int()    # To convert number to Integer
float()  # To convert number to Float
bool()   # To convert number to Boolean
str()    # To convert anything to String
'''
x = 42
num2 = input("Enter num : ")

print("Addition: ", x + int(num2))


x = 10

# to Float
print("Before Float1 : ", x, type(x))
x = float(x)
print("After Float1 : ", x, type(x))

x = 10
# to string
print("Before Float2 : ", x, type(x))
x = str(x)
print("After Float2 : ", x, type(x))



x = 100
# to boolean   non0: True   0: False
print("Before Float3 : ", x, type(x))
x = bool(x)
print("After Float3 : ", x, type(x))

print("============ADDING NUMBERS========")

print("-------------Approach 1-------------")
print(10+20)  # Hard coding & Single time usage



print("-------------Approach 2-------------")
# Let us assume x = 10
x = 10
y = 20        # Multiple times usage
print(x+y)   # Operation1

print("-------------Approach 3.1   Practice purpose-------------")
x = 10  # Static way of initialization
y = 20
print("Addition is     : ", x+y)  # One time usage

x = 10  # Static way of initialization
y = 20
res = x + y
print("Addition is : ", res)


empid = 100
print("Employee id : ", empid)



print("-------------Approach 3.2  Ideal-------------")
x = input("Enter number1 : ")   # 10 -> '10'   # UI   Python  Database
y = input("Enter number2 : ")   # 20 -> '20'
output = x+y  # '1020'
print("Addition is : ", output)

# Final and Correct Approach
x = int(input("Enter number1 : "))   # 10 --> '10'  --> 10
y = int(input("Enter number2 : "))  # '20'
output = x+y
print("Addition is : ", output)


'''
REQ:  Create new gmail account

Entity: Gmail 
=================
1. CRUD    : CREATE   (CREATE RETRIEVE UPDATE DELETE)
2. State   : firstname, lastname, mobile number, dob, age, gender, location 
3. Behavior: Create new gmail account of user
 
 
Gmail:
--------
    - CREATE : Create gmail account 
                State: firstname...........
                Behavior: Create gmail account with details 
                           - If user already exists : Error 
                           - If no user exists : Will create account 
    - RETRIEVE: Login to gmail account 
                State : username, password, otp
                Behavior: Logged into account 
                            - If creds are correct - Home page 
                            - If creds are wrong - Error message
    - CREATE  : Send email to friend with attachment
    - DELETE : Delete email 
    - UPDATE : Change password
    - UPDATE : Change mobile number



Entity: Gmail
CRUD : CREATE RETRIEVE UPDATE DELETE

    Gmail Signup: CREATE 
    Login op    : RETRIEVE 
    Ch mobile # : UPDATE 
    Deactivating: DELETE

Technologies    : Python/Java/.Net
Domain knowledge: Finance/Banking/Healthcare/Telecom/Ecommerce/Manufacturing/Education

'''

'''   
REQUIREMENT:
==============
1. CRUD     : CREATE/RETRIEVE/UPDATE/DELETE
2. STATE    : Datatypes/Datastructures  int/float/bool/str/list/tuple/dict/set 
3. BEHAVIOR : Action part               Operators/DM/Loops
'''
'''
# REQ: Give result of adding 2 numbers
    State    : 2 numbers
    Behavior : Give result of addition
    
1. CRUD  : CREATE    
2. STATE : int / float
3. Operators(+, =)
'''
# State
x = 10
y = 20
# Behavior
result = x+y
print("Addition is  :", result)
