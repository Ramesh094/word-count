# no_of_questions = 5
# score = 0
# questions_list = {"1) which operator is used for multiplication?\na) # \nb) - \nc) / \nd) *": "d",
#                   "2) what symbol is used for single line comment?\na) // \nb) ''' \nc) # \nd) ||": "c",
#                   "3) what is the answer for 89%10 ?\na) 9 \nb) 8 \nc) 8.9 \nd) 89 ": "a",
#                   "4) which method is used to add single item to a list?\na) add \nb) a&d \nc) append \nd) extend ": 'b',
#                   '5) which method is used to make string capitalize?\na) upper() \nb) lower() \nc) capitalize() \nd) bigger()': 'a'
#                   }
# for x in questions_list:
#     print(x)
#     answer = input("Enter your Answer : ")
#     if answer == questions_list[x]:
#         score = score + 1
#         print(score)
# percentage = (score / no_of_questions) * 100
# print(percentage)
#-----------------------------------------------
# import random
#
# user_input = int(input("Guess the number: "))
# num = random.randint(1, 100)
# while  user_input <=100 and user_input >=0:
#     if user_input >= 0 and user_input <= 100:
#         print("Entered a valid number")
#         if user_input == num:
#             print("Congratulations, you won")
#             break
#         elif user_input > num:
#             print("Entered number is too high")
#             user_input = int(input("Enter the number again: "))
#         elif user_input < num:
#             print("Entered number is too low")
#             user_input = int(input("Enter the number again: "))
#     else:
#         print("Please Enter the number between 1 to 100")
#         user_input = int(input("Enter the number again: "))
#-------------------------------------------------
# user_input1 = int(input("Enter first number :"))
# user_input2 = int(input("Enter second number :"))
# user_input3 = int(input("Enter third number :"))
# total_sum  = user_input1 + user_input2 + user_input3
# if user_input1 == user_input2 == user_input3 :
#     total_sum = total_sum * 3
#     print(total_sum)
# else:
#     print(total_sum)
#-------------------------------
# n = int(input("Enter no inputs :"))
# given_list = []
# for x in range(0, n):
#     ele = int(input())
#     given_list.append(ele)
# count = 0
# for four in given_list:
#     if int(four) == 4:
#         count += 1
# print(count)
#---------------------------------
# user_input = input("Enter a letter to check : ")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# for vowel in vowels:
#     if user_input == vowel:
#         print("%s is vowel" % user_input)
#         break
#     else:
#         print("%s is not vowel" % user_input)
#         break
#------------------------------------------
# price = int(input("Enter the total price : "))
# discount= int(input("Enter the discount : "))
# if price >= 0 and price > discount:
#     final_price = price - price*(discount / 100)
#     print("Final price is", final_price)
# print("Item price should be greater than 0 and discount")
#------------------------------------------------
# print("Enter the first letter from below options only \nrock \npaper \nscissor")
# player1 = input("Enter player1 input : ")
# player2 = input("Enter player2 input : ")
# player1 = player1.strip()
# player2 = player2.strip()
# r = "r"
# p = "p"
# s = "s"
# if player1 == r or player1 == p or player1 == s:
#     if player2 == r or player2 == p or player2 == s:
#         if player1 == r and player2 == p:
#             print("player2 wins!")
#         elif player1 == p and player2 == s:
#             print("player2 wins!")
#         elif player1 == s and player2 == r:
#             print("player2 wins")
#         elif player1 == p and player2 == r:
#             print("player1 wins!")
#         elif player1 == s and player2 == p:
#             print("player1 wins!")
#         elif player1 == r and player2 == s:
#             print("player1 wins")
#         elif (player1 and player2 == r) or (player1 and player2 == p) or (player1 and player2 == s):
#             print("It's  draw")
#     else:
#         print("PLayer2  should enter the first letter from below options only")
# else:
#     print("PLayer1 enter the first letter from below options only")
#-------------------------------------------------
ent_pass = input("Enter your password to validate : ")
special_chr = "!@#$%^&*()_-+=|?/<>.,`~"                 # special character list
sp_c = 0                                                # special character count
num = 0                                                 # numbers in password
if ent_pass:
    if len(ent_pass) >= 8:
        if ent_pass[0].isupper():
            for i in ent_pass:
                if i.isdigit():
                    num += 1
                for j in special_chr:
                    if i == j:
                        sp_c += 1
                        break
            if sp_c >= 1 and num >= 1:
                print("Password is strength is good")
            else:
                print("Password should contain at least one special character and one number")
        else:
            print("first letter should be capital")
    else:
        print("password must be 8 characters length")
else:
    print("Invalid input")