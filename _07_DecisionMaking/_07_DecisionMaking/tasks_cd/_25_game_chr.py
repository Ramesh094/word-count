'''25
Create a program that simulates decision-making for a game character based on different scenarios (e.g., fight or flee,
choose a weapon).
I. Req:
II. Analysis:
Functional Analysis:
Technical Analysis:
1.
2.
3.
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
print("Make game character active by entering the first letter of the given actions")
actions = {'p': 'give a punch to enemy',
           'j': 'Jump from standing position',
           'w': 'take the weapon',
           'f': 'fly high',
           'r': 'run like a deer',
           'h': 'hide from the enemy',
           'jp': 'jump and punch the enemy',
           'jr': 'jump and run away from enemy',
           'd': 'down misses from enemy'}
action = input("What to do: ")
action = action.strip()
if action in actions.keys():
    for d in actions:
        if action == d:
            print(actions[d])
else:
    print("Give valid input")