'''16
Create a program that verifies a user's login credentials (e.g., username and password).
I. Req: check the username and password are correct or not 
II. Analysis:
Functional Analysis:
1. take username and password from user
2. check the username and password is correct or not
3. if correct give validation message
4. if wrong give an error message 
Technical Analysis:
State : str str
Behavior: Operators, Decision Making, Loops
            ==          if              none
                            if
                            else
                        else
'''
user_id = input("Enter UserId")
password = input("Enter Password")
actual_id = "Ramesh094"
pwd = "Learn@779"
if user_id == actual_id:
    if password == pwd:
        print("Login successful, Enjoy the session.....!")
    else:
        print("password is wrong!")
else:
    print("userId is wrong!")

