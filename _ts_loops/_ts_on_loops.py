""" 1
Write a program that counts the occurrences of each character in a given string.
I. Req: Have to count each character of a string how many times it presents in the string.
II. Analysis:
Functional Analysis:
1. Have to take input as a string.
2. count each character of a string how many times it repeating.
3. print result character with its count.
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            in                          for
III. Design:
"""
input_str = input("Enter a string: ")
new = {}
# for i in input_str:
#     cc = input_str.count(i)
#     new[i] = cc
# print(new)
for i in input_str:
    c = 0
    for j in input_str:
        if i == j:
            c = +1
    new[i] = c
print(new)
'''2
Write a program to find the maximum and minimum numbers in a given list.
I. Req: find minimum and maximum numbers in a given list.   
II. Analysis:
Functional Analysis:
1. Take input as list.
2. find minimum and maximum numbers in the list. 
3. print the result.
Technical Analysis:
State : list
Behavior: Operators, Decision Making, Loops
                                        for
'''
"""
no_of_input = int(input("Enter number of list items: "))
given_list = []
for i in range(no_of_input):
    list_item = int(input("Enter list item: "))
    given_list.append(list_item)
min_num = min(given_list)
max_num = max(given_list)
print("Minimum is : ", min_num, "and maximum is : ", max_num)
# given_list.sort()
# print("Minimum is : ", given_list[0], "and maximum is : ", given_list[-1])
"""
given_num_list = input("Enter the numbers with space").split()
maxi = given_num_list[0]
mini = given_num_list[0]
for i in given_num_list:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print(maxi, mini)

'''3
Write a program that calculates the average of a given list of numbers.
I. Req: find the average of the given list of numbers.   
II. Analysis:
Functional Analysis:
1. take input as list
2. find the average.
3. print the result.
Technical Analysis:
State : list
Behavior: Operators, Decision Making, Loops
            + /                        for
'''
given_num_list = input("Enter the numbers with space").split()
print(given_num_list)
summ = 0
no_of_nums = len(given_num_list)
for i in given_num_list:
    summ = summ + int(i)
average = summ / no_of_nums
print("Average of the given list is", average)

'''4
Write a program to check if a given string is a palindrome.
I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
input4 = str(input("Enter a string : "))
rev_str = ""
for s in input4:
    rev_str = s + rev_str
if input4 == rev_str:
    print("%s is a palindrome" % input4)
else:
    print("%s is not a palindrome" % input4)
'''5
Write a program that removes duplicates from a given list.
I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
# remove_duplicates = input("Enter the numbers with space").split()
# remove_duplicates = set(remove_duplicates)
# print(remove_duplicates)
remove_duplicates = input("Enter the numbers with space").split()
new = []
for i in remove_duplicates:
    if i not in new:
        # new.append(i)
        new = new + [i]
print(new)
'''6
Write a program that reverses the order of elements in a given list.
I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
list_item = input("Give each item with space : ").split()
reversed_list = []
# for n in list_item[::-1]:
#     reversed_list.append(n)
# print(reversed_list)
for n in list_item:
    reversed_list.insert(0, n)
print(reversed_list)
# list_item.reverse()
# print(list_item)

'''7
Write a program to check if a given number is an Armstrong number.
Armstrong number is sum of its own digits raised to the power of number of digits of the number. 
I. Req: check the given number is armstrong number.
II. Analysis:
Functional Analysis:
1. Take input as an integer.
2. Do the sum of its digits raised to the power of number of digits of the number. 
3. compare the sum and the number.
4. Print armstrong if it is true else it is not an arm strong number. 
Technical Analysis:
State : int
Behavior: Operators, Decision Making, Loops
            **,==,+     if else         for
'''
armstrong_num = input("Enter a number to  check Armstrong or Not : ")
length = len(armstrong_num)
summation = 0
for i in armstrong_num:
    summation = summation + int(i)**length
if summation == int(armstrong_num):
    print(armstrong_num, " is an armstrong number")
else:
    print(armstrong_num, " is not an armstrong number")

# if you take input as an integer this is the method to check armstrong number
# armstrong_num = int(input("Enter a number to  check Armstrong or Not : "))
# length = len(str(armstrong_num))
# summation = 0
# for i in range(length):
#     armstrong_num = str(armstrong_num)
#     summation = summation + int(armstrong_num[i])**length
# if summation == int(armstrong_num):
#     print(armstrong_num, " is an armstrong number")
# else:
#     print(armstrong_num, " is not an armstrong number")

'''8
Write a program that removes specified characters from a given string.
I. Req: Remove the characters specified.   
II. Analysis:
Functional Analysis:
1. Take input 1 and 2 as string.
2. check that input 2 is presented in input 1 or not.
3. if presents remove that input 2 from input 1.
4. print result.
Technical Analysis:
State : str str
Behavior: Operators, Decision Making, Loops
            ==,            if else     for
'''
# input_1 = input("Enter a string : ")
# input_2 = input("Enter a character to remove from input_1: ")
# for i in input_1:
#     if input_2 == i:
#         input_1 = input_1.replace(i, "")
# print(input_1)

input_1 = input("Enter a string : ")
input_2 = input("Enter a character to remove from input_1: ")
result = ''
# for i in input_1:
#     if input_2 == i:
#         result = result
#     else:
#         result = result + i
# print(result)
for i in input_1:
    if i not in input_2:
        result += i
print(result)
'''9
Write a program to check if a given number is a perfect number.
perfect number is sum of  its proper divisors is equals to given number.
I. Req:   check the given number is perfect number or not
II. Analysis:
Functional Analysis:
1. Take input as integer.
2. find the proper divisors of the given number.
3. do the sum of divisors.
4. print the result if sum is equals to input.
Technical Analysis:
State : int
Behavior: Operators, Decision Making, Loops
            %,==,+      if else        for
'''
num = int(input("Enter a number to check it is Perfect number or Not:"))
summ = 0
if num > 0:
    for i in range(1, num):
        if num % i == 0:
            summ = summ + i
    if summ == num:
        print(num, " is perfect number")
    else:
        print(num, " is not a perfect number")
else:
    print("To check perfect number the number should be positive number")
'''10
Write a program that prints all the prime factors of a given number.
prime factor is a natural number other than 1 only  which is divisible by itself.
I. Req: print the prime factors of given number
II. Analysis:
Functional Analysis:
1. Take input number as an integer.
2. Find the factors of the number.
3. If factors divisible by 1 and factor itself. 
    # to find prime factors you have to iterate through factors list first. and then set count = 0 after that again
    iterate from 2 to itertable item of factors i.e 'f' and with in this loop write a condition to find divisible 
    by the 'f' itself. i.e "f % p == 0" then c += 1
    # if c == 0 add f in to a new list and print it.   
4. print that factor numbers. 
Technical Analysis:
State : int
Behavior: Operators, Decision Making, Loops
         += % and ==    if else        for
'''
# STATE
num = int(input("Enter a number to find prime factors of the number : "))
factors = []
# Behavior
for i in range(2, num):
    if num % i == 0:
        factors += [i]
print(factors)
prime_factors = ""
for f in factors:
    c = 0
    for p in range(2, f):
        if f % p == 0:
            c += 1
    if c == 0:
        prime_factors += str(f) + " "
print(prime_factors)

# prime numbers and composite numbers
num = int(input("Enter: "))
prime = []
composite = []
for i in range(2,num):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
    if c == 0:
        prime += [i]
    else:
        composite += [i]
print(prime)
print(composite)

'''11
Write a program to calculate the greatest common divisor (GCD) of two given numbers.
I. Req: find the gcd of two give numbers.   
II. Analysis:
Functional Analysis:
1. Take two inputs as integers from user.
2. Find the common factors of two numbers.
3. print the highest common factor.
Technical Analysis:
State : int int
Behavior: Operators, Decision Making, Loops
            % == >     if else         while
'''
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
# gcd = 0
# for i in range(2, num1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print(gcd)

i = 2
while i < num1:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1
print(gcd)
'''12
Write a program that counts the number of words in a given sentence.
I. Req:   count the number of words in given sentence.
II. Analysis:
Functional Analysis:
1. Take the input from user as a string.
2. set count = 0 
3. if item of input string is equals to empty space update count with 1.
4. print the count.   
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            < == +=         if        while
'''
sentence = input("Enter a sentence :")
cw = 1
i = 0
le = len(sentence)
while i < le:
    if sentence[i] == " ":
        cw += 1
    i += 1
print(cw)
# cw = 1
# for char in sentence:
#     if char == " ":
#         cw += 1
# print(cw)
'''13
Write a program that finds common elements between two given lists.
I. Req:   find the common elements from given two lists.
II. Analysis:
Functional Analysis:
1. Take two inputs from user as lists.
2. Iterate the elements of first list.
3. If element of first list is second list add the element to new list.
4. After final iteration of first list print new list.     
Technical Analysis:
State : list list
Behavior: Operators, Decision Making, Loops
            in +=        if            while
'''
list1 = eval(input("Enter list1: "))
list2 = eval(input("Enter list2: "))
new = []
i = 0
while i < len(list1):
    if list1[i] in list2:
        new += [list1[i]]
    i += 1
print(new)
# for e in list1:
#     if e in list2:
#         new += [e]
# print(new)
'''14
Write a program to calculate the square root of a given number using the Newton-Raphson method.
I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
'''15
Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
I. Req: Swap the case of characters in a given string.
II. Analysis:
Functional Analysis:
1. Take input as a string.
2. Iterate through input. 
3. If element is in lower case make it to upper case and vice versa.
4. print final output.
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            +           if elif         while            
'''
# State
input_str = input("Enter a string: ")
# Behavior
st = ""
i = 0
while i < len(input_str):
    if input_str[i].isupper():
        x = input_str[i].lower()
        st += x
    elif input_str[i].islower():
        y = input_str[i].upper()
        st += y
    i += 1
# for i in input_str:
#     if i.islower():
#         x = i.upper()
#         st += x
#     elif i.isupper():
#         y = i.lower()
#         st += y
print(st)
'''16
Write a program that checks the strength of a password based on the following criteria:
I. Req: Check the password strength
II. Analysis:
Functional Analysis:
1. Take input from user. 
2. check the input satisfies the conditions mentioned in requirement.
3. If true password strength is good else password strength is weak.
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            
'''
input_pass = input("Enter Password : ")
d = 0
u = 0
lo = 0
for i in input_pass:
    if i.isupper():
        u += 1
    elif i.isdigit():
        d += 1
    elif i.islower():
        lo += 1
if len(input_pass) > 8 and lo >= 1 and u >= 1 and d >= 1:
    print("Strong Password")
else:
    print("Weak Password")
'''17
Write a program that capitalizes the first letter of each word in a given sentence.
I. Req: Make the first letter capital of each word   
II. Analysis:
Functional Analysis:
1. Take input from user.
2. make the first letter capital of each word.
3. print the output.
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            
'''
user_in = input("Enter a sentence: ")
st = ""
word = user_in.split()
print(word)
for i in word:
    for j in range(len(i)):
        if j == 0:
            x = i[j].upper()
            st = st + " " + x
        elif j > 0:
            y = i[j].lower()
            st = st + y
st = st.strip()
print(st)
'''18
Write a program that counts the frequency of each word in a given text.
I. Req: count the frequency word of each word.
II. Analysis:
Functional Analysis:
1. Take user input.
2. Separate each word and make a list. 
3. Iterating the list and count each element present in list.
4. create an empty dictionary, add each element and its count into that dictionary.
5. print the dictionary.
Technical Analysis:
State : str
Behavior: Operators, Decision Making, Loops
            == +=        if            for
'''
user_in = input("Enter text : ")
word = user_in.split()
fr_c = {}
print(word)
for j in word:
    j = j.strip(".")
    if j in fr_c:
        fr_c[j] += 1
    else:
        fr_c[j] = 1
print(fr_c)
    # c = 0
    # j = j.strip(".")
    # for h in range(len(word)):
    #     h = word[h].strip(".")
    #     if j == h:
    #         c += 1
    #         fr_c[j] = c
    # if c == 1:
    #     fr_c[j] = c
    # elif c > 1:
    #     fr_c[j] = c
#     c = 0
# print(fr_c)
'''19
Write a program that checks if two given strings are anagrams of each other.
I. Req: To check anagram or not.
II. Analysis:
Functional Analysis:
1. take two inputs from user.
2. check the characters and length of first input and second input are same.
3. But first input should not be is equals to the second input.
4. If above conditions satisfied print it is an angram.
Technical Analysis:
State : str str
Behavior: Operators, Decision Making, Loops
            ==, in       if else        for
'''
input_1 = input("Enter first word: ")
input_2 = input("Enter second word: ")
if len(input_1) == len(input_2):
    c = 0
    for i in input_1:
        if i in input_2:
            c += 1
    if c == len(input_2):
        print("Inputs are anagrams")
else:
    print("Inputs are not anagrams")
'''20
Write a program that calculates the transpose of a given matrix.
I. Req: calculate the transpose of a matrix.
II. Analysis:
Functional Analysis:
1. Take list as input.
2. create a duplicate matrix opposite to input matrix rows and cols. 
3. calculate the transpose of input matrix.
Technical Analysis:
State : list
Behavior: Operators, Decision Making, Loops
            *                           
'''
matrix = eval(input("Enter a matrix to Transpose: "))
tr_matrix = []
rows = len(matrix)
cols = len(matrix)

for i in range(rows):
    tr_matrix.append([0] * cols)

for i in range(rows):
    for j in range(cols):
        tr_matrix[j][i] = matrix[i][j]
print(tr_matrix)
# for i in range(le):
#     if i == 0:
#         for j in matrix:

    #         row.append(j[i])
    # elif i == 1:
    #     for j in matrix:
    #         row.append(j[i])
    # elif i == 2:
    #     for j in matrix:
    #         row.append(j[i])
'''21

I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
'''2

I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
'''2

I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
'''2

I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
'''2

I. Req:   
II. Analysis:
Functional Analysis:
1. 
2.
3.    
Technical Analysis:
State :
Behavior: Operators, Decision Making, Loops
'''
input_1 = input("enter a string: ")
rev = ""
for i in input_1:
    rev = i + rev
print(rev)

given_num_list = input("Enter the numbers with space").split()
maxi = given_num_list[0]
mini = given_num_list[0]
for i in given_num_list:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print(maxi, mini)
