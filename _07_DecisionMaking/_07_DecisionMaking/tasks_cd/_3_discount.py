'''3
Description: In this task, students should develop a program that calculates the discount amount for a shopping cart 
based on the following conditions:

If the total price is greater than or equal to $100, apply a 10% discount.
If the total price is between $50 and $99.99, apply a 5% discount.
If the total price is less than $50, no discount is applied.

I. Req: calculate discount amount of a cart based on conditions specified.
II. Analysis:
Functional Analysis:
1. Price of cart will be given by user.
2. Have to calculate the discount of cart
3. print the result.
Technical Analysis:
State : total_price = float
Behavior: Operators, Decision Making, Loops
            >,<,=    if elif else
III. Design:
1. price >=100
total_price = 101
total_price >= 100 
101 >= 100 
    101 * 0.1
    10.1 is the discount
    
2. 99.99 <= price >=50
price = 60
60 * 0.05 =  3 is the discount of 60

3. price < 50
for 25 discount is zero
'''
print("----------- know the discount of a cart price -------------")
total_price = float(input("Enter a price to know discount : "))
if total_price > 0:
    print("input is valid")
    if total_price >= 100:
        disc = total_price * 0.1
        print("$", disc, " is the discount for ", "$", total_price)
    elif 99.99 <= total_price >= 50:
        disc = total_price * 0.05
        print("$", disc, " is the discount for ", "$", total_price)
    else:
        print("$0 is the discount for ", "$", total_price)
else:
    print("Input is invalid")