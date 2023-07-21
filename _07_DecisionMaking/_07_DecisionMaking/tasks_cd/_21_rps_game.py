'''21
Write a program that allows two players to play the classic game of rock, paper, scissors and determines the winner.
I. Req: crate a two player based rock, paper scissor game.
II. Analysis:
Technical Analysis:
1. no of players two
2. write the  different conditions/rules of game
3. announce the winner
Functional Analysis:
1   player1 = rock
    player2 = paper
    rock < paper #rock surrounded by the paper # player2 wins!
2   player1 = scissor
    payer2 = paper
    paper < scissor #scissor cuts the paper   # player1 wins!
3.  scissor < rock   # rocks breaks the scissor # player2 wins!
State : player1 player2
Behavior: Operators, Decision Making, Loops
            > < ==     if elif else
III. Design:
'''
print("Enter the first letter from below options only \nrock \npaper \nscissor")
player1 = input("Enter player1 input : ")
player2 = input("Enter player2 input : ")
player1 = player1.strip()
player2 = player2.strip()
r = "r"
p = "p"
s = "s"
if player1 == r or player1 == p or player1 == s:
    if player2 == r or player2 == p or player2 == s:
        if (player1 == r and player2 == p) or (player1 == p and player2 == s) or (player1 == s and player2 == r):
            print("player2 wins!")
        elif (player1 == p and player2 == r) or (player1 == s and player2 == p) or (player1 == r and player2 == s):
            print("player1 wins!")
        elif (player1 and player2 == r) or (player1 and player2 == p) or (player1 and player2 == s):
            print("It's  draw")
    else:
        print("PLayer2  should enter the first letter from below options only")
else:
    print("PLayer1 enter the first letter from below options only")