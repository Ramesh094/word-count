"""19
Create a program that validates if a given email address is correctly formatted.
I. Req: validating email address
II. Analysis:
Technical Analysis:
1. User will give email.
2. email should contain @ symbol and domain name after @.
3. Should have some name before @.
4. If above conditions satisfied print valid else invalid.
Functional Analysis:
State : str
Behavior: Operators, Decision Making, Loops
           >=             if else
III. Design:
input = xyz@nmnm.com
"""
email = input("Enter an email Id!")
end = email.endswith(".com")
if "@" in email and end:
    x = email.split("@")
    xl = len(x[0])
    xr = len(x[1])
    if xl >= 6 and xr >= 8:
        print("%s is valid email" % email)
    else:
        print("%s is not valid" % email)
else:
    print("Please enter a valid email")