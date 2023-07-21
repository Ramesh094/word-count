#it repeatedly asks the input and executes the code and you have to exit manually by entering -1

# while True:
#     marks = int(input("Enter Your Marks (or enter -1 to exit): "))
#     if marks == -1:
#         break
#     if marks >= 200 and marks <= 600:
#         if marks >= 500 and marks <= 600:
#             print("Pass and got first class")
#         elif marks >= 400 and marks < 500:
#                print("Pass and got second class")
#         elif marks >= 300 and marks < 400:
#             print("Pass and got third class")
#         elif marks<300:
#             print("Pass and got fourth class")
#     elif marks > 600:
#         print("it's not valid input, enter marks below 1 - 600 only")
#     else:
#         print("fail")

num = int(input("Enter a number : "))  # 897
reversed_num = 0
while num != 0:  # while loop executes until condition is false
    reversed_num = reversed_num * 10 + num % 10
    # 1. 0*10 + 897%10 => 0 + 7 = 7
    # 2. 7*10 + 89%10 => 70 + 9 = 79
    # 3. 79*10 + 8%10 => 790 + 8 = 798
    num = (num // 10)
# 897!=0 True /it executes the loop
#   1. 897//10 = 89.7 here 89 is stored in num and checks
# 89!=0 True
#   2. 89//10 = 8.9  here 8 is stored in num for next iteration
# 8!=0 True
#   3. 8//10 = 0.8 here 0 is stored in num
# 0 != 0 False it terminates the loop execution
print("After reverse : %d " % reversed_num)
