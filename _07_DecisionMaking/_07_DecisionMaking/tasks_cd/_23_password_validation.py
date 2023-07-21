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