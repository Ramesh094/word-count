'''18
Create a program that calculates the final price of a product after applying a discount.
I. Req: calculate final price after discount 
II. Analysis:
Technical Analysis:
1. Take two inputs as total price, discount from user.
2. find final price with out discount.
3. print the price. 
Functional Analysis:
State : int int
Behavior: Operators, Decision Making, Loops
III. Design:
'''
price = int(input("Enter the total price : "))
discount = int(input("Enter the discount : "))
if price >= 0 and price > discount:
    final_price = price - price*(discount / 100)
    print("Final price is", final_price)
print("Item price should be greater than 0 and discount")