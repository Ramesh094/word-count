# 1. Numbers:
    # int     : int()
    # float   : float()
    # complex : complex()

x = 10  # int
print("Value of x : ", x)

x = 10.5  # float
print("Value of x : ", x)

# Convert from float to int
x = 125.33  # float
print("Value of x: ", x)
x = int(x)
print("Value of x: ", x)


# Convert from int to float
x = 10
x = float(x)
print("Value of x : ", x)


'''
Functions: f(x)
-----------------
print() : R : To print the content   
type()  : R : To get type of variable or value
id()    : R : To get address of value in integer format 
input() : C : To receive data dynamically 
-----------
int()   : U : converts other format to integer
float() : U : converts other format to float 
complex():U :  Ignore it 
bool()  : U : converts other format to boolean

'''

x = 10
print("Value of x  ", x)
print("Type of x : ", type(x))
print("ID of x   : ", id(x))
x = float(x)
print("Float of x : ", x)
x = int(x)
print("Int of x : ", x)
