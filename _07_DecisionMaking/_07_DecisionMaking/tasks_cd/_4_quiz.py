''' 4.
Description: Ask students to create a program that simulates a simple quiz. The program should present a series of
multiple-choice questions to the user and keep track of their score. At the end of the quiz, display the user's score as 
a percentage.
I. Req: Make a quiz and show the score in percentage.
II. Analysis:
Functional Analysis:
1. No of questions are 5.
2. Take answers for the 5 questions from user.
3. If answer is right give 1 mark.
4. print total score in percentage.
Technical Analysis:
State : user_input1-5 = str
Behavior: Operators, Decision Making, Loops
            +, /, *    if          for
III. Design:
'''
print("---------- Shall we test your knowledge ------------")
no_of_questions = 5
score = 0
questions_list = {"1) which operator is used for multiplication?\na) # \nb) - \nc) / \nd) *": "d",
                  "2) what symbol is used for single line comment?\na) // \nb) ''' \nc) # \nd) ||": "c",
                  "3) what is the answer for 89%10 ?\na) 9 \nb) 8 \nc) 8.9 \nd) 89 ": "a",
                  "4) which method is used to add single item to a list?\na) add \nb) a&d \nc) append \nd) extend ": 'b',
                  '5) which method is used to make string capitalize?\na) upper() \nb) lower() \nc) capitalize() \nd) bigger()': 'a'
                  }
for x in questions_list:
    print(x)
    answer = input("Enter your Answer : ")
    if answer == questions_list[x]:
        score = score + 1
        print(score)
percentage = (score / no_of_questions) * 100
print(percentage)