'''15
Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
I. Req: convert temperature from celsius to fahrenheit 
II. Analysis:
Technical Analysis:
1. take input
2. check the input is fahrenheit or celsius 
3. convert using formula acc to input
4. print result
Functional Analysis:
fahrenheit = (temp *9/5) + 32
°C = (temp - 32) × 5/9
State :
Behavior: Operators, Decision Making, Loops
III. Design:
'''
print("while temperature enters in celsius should end with capital 'C' \n while temperature enters in fahrenheit should end with capital 'F'")
temp = input("Enter temperature in Fahrenheit(F) or in celsius(C)")
x = temp.endswith("C")
y = temp.endswith("F")
if x:
    temp1 = temp.rstrip("C")
    temp_in_c = (int(temp1) * 9 / 5) + 32
    print("Temperature in %s in celsius" % temp_in_c)
elif y:
    temp2 = temp.rstrip('F')
    temp_in_f = (int(temp2) - 32) * 5 / 9
    print("Temperature in %s in celsius" % temp_in_f)
else:
    print("Input is invalid! please number ends with F or C")