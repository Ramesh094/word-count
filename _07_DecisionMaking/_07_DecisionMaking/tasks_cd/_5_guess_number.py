'''5
Description: Have students create a program that generates a random number between 1 and 100. The user should guess the 
number, and the program should provide feedback on whether the guess is too high or too low. The program should continue
until the user guesses the correct number.
I. Req: Create a number guess game
II. Analysis:
Functional Analysis:
Technical Analysis:
1. Have to take input from user.
2. should give some suggestions acc to user input until he guesses the number
3. print  a congratulations message once he found.
State : user_input = int
        import random to get random number
Behavior: Operators, Decision Making, Loops
            >,<,==      if elif else    while
III. Design:
input = 55
random = 22
if input == random:
    write success message
elif input > random
    write too high
elif input < random
    write too low        
    
'''
print("----------Number Guess Game-----------")
import random

user_input = int(input("Guess the number: "))
num = random.randint(1, 100)
while  user_input <=100 and user_input >=0:
    if user_input >= 0 and user_input <= 100:
        print("Entered a valid number")
        if user_input == num:
            print("Congratulations, you won")
            break
        elif user_input > num:
            print("Entered number is too high")
            user_input = int(input("Enter the number again: "))
        elif user_input < num:
            print("Entered number is too low")
            user_input = int(input("Enter the number again: "))
    else:
        print("Please Enter the number between 1 to 100")
        user_input = int(input("Enter the number again: "))
