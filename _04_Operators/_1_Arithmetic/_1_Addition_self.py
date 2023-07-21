# Addition

""" Requirement : Adding Numbers
  =============================
    1. How many numbers have to ADD : Only 2 numbers or more.
    2. What type of numbers         : Only Positive or only Negative or both.
    3. Datatype                     : Only int, only float, both int/float.
    4. Zero                         : 0 is allowed or not

Based on scenarios:

    I. Based on count
        1. 2 numbers  2 + 3 = 5
        2. 2 or more numbers  9 + 5 + 6 = 20
    II. Based on type
        1. Both positive    
        2. Both negative   
        3. First positive, second negative  
        4. First negative, second positive  
        5. First 0, second positive 
        6. First 0, second negative 
        7. First negative, second 0
        8. First positive, second 0
        9. Both 0
        10. two positive, one negative
        11. two neagtive, one positive
    III. Based on datatype
        1. Both int 
        2. Both float 
        3. one int, one float  
        4. one float, one int 
        5. two float, one int or one float two int
        6. two or more float, two or more int
        
I. Based on count:
    1. 2 numbers:"""
# 1. State
x = 25
y = 45
# 2. Behavior
result = x + y
# result = 25 + 45
# 3. Display result to End User.
print("Addition: ", result)
# 2. two or more numbers:
# 1.State
x = 20
y = 10
z = 15
# 2 Behavior
result = x + y + z
# 3. Display result to End User
print("Addition:", result)

#II.Based on type:
#1. Both positive numbers
# 1. State
n1 = 9
n2 = 15
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print("Addition", res)  # 24
#2. Both negative number
# 1. State
n1 = -77
n2 = -23
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print("Addition", res)  # -100
#3. First Positive and Second negative
# 1. State
n1 = 22
n2 = -33
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # -11
#4. First Negative and Second positive
# 1. State
n1 = -50
n2 = 25
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # -25
#5. First 0, second positive
# 1. State
n1 = 0
n2 = 10
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 10
#6. First 0, second negative
# 1. State
n1 = 0
n2 = -10
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # -10
#7. First positive, second 0
# 1. State
n1 = 29
n2 = 0
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 29
#8. First negative, second 0
# 1. State
n1 = -14
n2 = 0
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # -14
#9. Both 0
# 1. State
n1 = 0
n2 = 0
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 0
#10. two positive, one negative
# 1. State
n1 = 4
n2 = 26
n3 = -4
# 2. Behavior
res = n1 + n2 + n3
# Display result to End User
print('Addition', res)  # 26
#11. two negative, one negative
# 1. State
n1 = -9
n2 = -6
n3 = 25
# 2. Behavior
res = n1 + n2 + n3
# 3. Display result to End user
print('Addition', res)  # 10
#III.Basedon datatype: 1. Both int
# 1. State
n1 = 22
n2 = 23
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 45
# 2. Both float
# 1. State
n1 = 10.5
n2 = 15.5
# 2. Behavior
res = x + y
# 3. Display result on End User
print('Addition', res)  # 26.0
#3. One int, one float
# 1. State
n1 = 39
n2 = 31.5
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 70.5
#4. One float, one int
# 1. State
n1 = 26.5
n2 = 7
# 2. Behavior
res = n1 + n2
# 3. Display result to End User
print('Addition', res)  # 33.5
#5. two float, one int
# 1. State
n1 = 11.5
n2 = 0.7
n3 = 43
# 2. Behavior
res = n1 + n2 + n3
# 3. Display result to End User
print('Addition', res)  # 55.2
#6. two int, one float
# 1. State
n1 = 69
n2 = 21
n3 = 9.9
# 2. Behavior
res = n1 + n2 + n3
# 3. Display result to End User
print('Addition', res)  # 99.9

# Attendence of an institute Requirements to make attendance:
#== == == == == == == == == == == == == == == == == =
#1. classification of people: male / female / any other gender
#2. how i print result: only attendies / only absenties
#3. male presents / female presents / other gender presenties
#4. male abscenties / female abscenties / other gender absenties
#5. how many male / female / other students.

# 1. Attendence of an institute:

# 1. State
total_strength = 100
total_male = 60
total_female = 40
male_att = 30
female_att = 32
other_gender = 0
# 2. Behavior
total_attended = male_att + female_att
total_abscenties = total_strength - total_attended
male_abs = total_male - male_att
female_abs = total_female - female_att
# 3. Display result
print("Total Attended", total_attended)  # 62
print('Total Absented', total_abscenties)  # 38
print('Male Absented', male_abs)  # 30
print('Female Absented', female_abs)  # 8
print("------------------end1-------------------")
# # Requirements to write odd numbers upto 20:
# == == == == == == == == == == == == == == == == == == == == == =
# 1. how do you want to print the result.
# 2. Is there any limit to odd numbers.
# 3. Do you provide any inputs / i have to start my own inputs.

# 2. to write even / odd numbers as a list upto 20:
# 1. State
odd_num = 1
odd_20 = []
# 2. Behavior
while odd_num < 20:
    odd_20.append(odd_num)
    odd_num += 2
# 3. Display result:
print("odd numbers upto 20", odd_20)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# how many orders for an item in hotel
# calculating money
# time calculations
# scores in games
