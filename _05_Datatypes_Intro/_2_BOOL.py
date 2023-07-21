

# Boolean : bool()
    # True
    # False
# 1 bit of memory location    1 or 0

is_present = True
is_active = False
is_exists = True
is_completed = False
is_leap = True
# is_male = True
is_pass = False
is_happy = True
is_win = True
is_good = False
is_holiday = False
is_worthy = True
is_rainy = False


# True  - 1    10011001
# False - 0

# Numbers
# 0     - False  -  0
# non 0 - True   - -10, -34, 1, -1, 644, 3322, 45.4, -5.4

x = -10
print("Value of x : ", x)
x = bool(x)
print("Bool of val : ", x)

x = 0
print("Value of x : ", x)
x = bool(x)
print("Bool of val : ", x)

is_val = 0
is_val2 = 12

# Binary 0 - False
# Binary 1 - True
# non zero - True   -14 25 3 -567
# zero     - False   0

x = 10
print("Value of x: ", x)
# print("Value of x: ", ord(x))
print("Value of x: ", bin(x))
bin_val = bin(x)
# print("Value of x: ", ord(x))
x = bool(x)
print("Value of x: ", x)

res = 10-10
print("Value of x: ", res, bool(res))

# None - False
# not None - True

#  0 vs None
# Entity  :       Attributes
# -----------       ------------
# Employee  : eid name mailid idcard address   sal
# Intern    : eid name mailid idcard address   sal(None)


str1 = ''
print("Bool string  ", bool(str1))
sal = None
print("Value   ", sal, bool(sal))

str1 = 'hello'
print("Bool string  ", bool(str1))

li = []
tu = ()
di = {}
set1 = set({})