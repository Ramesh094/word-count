# Addition

''''''

# Requirement* / Task* / Ticket* / Incident / Service Request
''' Requirement : Adding Numbers 
    =================================
        1. Count   : Only 2 numbers or more
        2. Type    : Only Positive or both Pos,Neg
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
                            6. number, 0 (pos/neg)
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
    # STATE
x = 10
y = 20
    # BEHAVIOR
result = x+y
    # DISPLAY RESULT TO END USER
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
y = 30.5
result = x * y
print("Multiplication :", result)

print("--------4. Float, Int--------")
x = 20.5
y = 10
res = x+y
print("Addition is : ", res)
