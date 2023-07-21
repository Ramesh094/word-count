# Addition

''''''

# Requirement* / Task* / Ticket* / Story / Incident / Service Request
''' Requirement : Adding Numbers 
    =================================
        1. Count   : Only 2 numbers or more
        2. Type    : Only Positive or only Negative or both Pos,Neg
        3. Datatype: Only Int. Int/Float
        4. Zero    : 0 is allowed or not 

        Scenarios:      I. Based on count
                            1. 2 numbers  (Robot)  4 + 5 = __9___
                            2. 3/4/5 numbers
                        II. Based on type
                            1. Both positive 
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number(pos/neg), 0 
                        III. Based on datatype
                            1. Both int
                            2. Both float 
                            3. int + float 
                            4. float + int


'''
print("================I. ADDITION OF NUMBERS================")
print("----------------SCENARIOS-----------------")

# Different use cases/scenarios
print("================I. Based on Count================")
print("------1. 2 Numbers------")
    # 1. STATE
x = 10
y = 20
    # 2. BEHAVIOR
result = x+y
    # 3. DISPLAY RESULT TO END USER
print("Addition: ", result)

# print("Addition: ", 10+20)
# print("Addition: ", 10**2+20**2)
# print("Addition: ", 10**3+20**3)



print("------2. 3 or more  Numbers------")
x = 10
y = 20
z = 30
result = x+y+z
print("Addition: ", result)

'''
                        II. Based on type
                            1. Both positive 
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number, 0 (pos/neg)
                            '''
print("================II. Based on Type================")
print("------1 Both positive------")
x = 10
y = 20
result = x+y
print("Both positive: ", result)

print("------2 Both negative------")
x = -5
y = -12
output = x+y
print("Both negative :", output)

print("------3. First positive, Second negative ------")
x = 4
y = -20
res = x+y
print("3. First positive, Second negative: ", res)

print("------4. First negative, Second positive ------")
x = -4
y = 20
res = x+y
print("4. First negative, Second positive", res)

print("------5. Zero,Pos Number------")
x = 0
y = 30
res = x+y
print("Addition is : ", res)

print("------5. Zero,Neg Number------")
x = 0
y = -30
res = x+y
print("Addition is : ", res)

print("------6. Pos Number, Zero------")
x = 30
y = 0
res = x+y
print("Addition is : ", x+y)

print("------6. Neg Number, Zero------")
x = -30
y = 0
res = x+y
print("Addition is : ", res)



'''
                        III. Based on datatype
                            1. Both int
                            2. Both float 
                            3. int + float 
                            4. float + int'''


print("================III. Based on DataType================")
print("--------1. Both Integers--------")
x = 20
y = 10
res = x+y
print("Addition is : ", res)

print("--------2. Both Float--------")
x = 20.5
y = 10.7
res = x+y
print("Addition is : ", res)

print("--------3. Int , Float--------")
x = 20
y = 10.7
res = x*y
print("Addition is : ", res)

print("--------4. Float, Int--------")
x = 20.5
y = 10
res = x+y
print("Addition is : ", res)


print("------------REALTIME SCENARIOS----------")

# REQ: Get total marks of Student
# REQ: Number of Passengers in Bus
# ....

# REQ: Shopping bill
# REQ: Electricity bill

bank_balance = 5000
dep1 = 100
dep2 = 500
f_bal = bank_balance + dep1 + dep2
print("Final bank balance ", f_bal)

shoe = 2000
bag = 3000
water_bottle = 100
watch = 500

# 5 Shoes, 3 Bags, 10 Water bottles, 2 Watches

shoe_price = shoe * 5
bag_price = bag * 3
water_b_price = water_bottle * 10
watch_price = watch * 2

f_bill = shoe_price + bag_price + water_b_price + watch_price
print("Total bill : ", f_bill)
c_tax = 2.5
s_tax = 2.5
discount = 10
bill_aft_tax = f_bill + f_bill * 2.5/100 + f_bill * 2.5/100
print("Total bill after tax : ", bill_aft_tax)
bill_aft_dsc = bill_aft_tax - bill_aft_tax*10/100
print("Total bill after disc : ", bill_aft_dsc)

print("Final bill  :", bill_aft_dsc)

print("---Thank you. Visit Again---")
# Restaurant works
