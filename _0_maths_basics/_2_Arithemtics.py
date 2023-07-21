'''

'''
'''
Basic Operations:  

I. Arithmetics : Addition, Subtraction, Multiplication, and Division
                 Modulus, Floor Division, Exponential, Power

REQ: Adding numbers  :
======================
Operation: CRUD 
Entity   : Addition
    State    : int float 
    Behavior : Operators, DM, Loops 
                + =  




2+5  6+2  4+6 : 10  12+43 123+432   1234+43 -5+4 4322+432.4+4/5
2+5+6
     Scenarios:
         - Is it only integers or float is allowed ?
         - Only positive or only negative or both positive/negative ?
         - Is there any limit of input data ?
         - Similar or Diff data 
         
         : 2 + 3 
         : 2 + 0.5 
         : 23 + 45 
         : 1.4 + 2.5
         : 4556 + 66553
         : -103 + 56
         : -104.22 + 567.32
         : 2/3 - 5/6 + 78/9

            - Scenarios
                    4 + 3 =  7
                    10 + 20 = 30
                    12 + 34 = 46
                    12 + 45 + 76 = 345
                    -10 + 20 = 10
Addition ? YES
    4 + 3   : 7
    39 + 54 : 93
    43 + 65 + 34     4354  Percentage  discount final bill 
    39
    54
   1 --- 
     93






Addition        :   Usecase: 2 + 3 = 5   
                                Scenarios :  2 + 3 + 6 = 11 
                                             -2 + 5    = 3

Requirement: Adding numbers(Perform addition).
             Consider only positive numbers and 0
                UseCases(Scenarios):    I. Positive,Negative
                                         - Addition of both positive
                                         - Addition of neg, positive
                                         - Adidtion of both negative
                                         - Addition of pos, 0
                                         - Addition of neg, 0
                                     II.Rational,Irrational,Imaginary,Real    
                                    III. Based on no of input values
                                          - 2 input  values
                                          - 3 input values 
                                          ..... n 
Subtraction     :   2 - 3 = -1
                   -2 - 5 = -7
             
Multiplication  :   2 X 3 = 6
                   -5 X 3 = -15
                   
Division        :   21 / 4 = quotient 5,remainder 1
                   -20 / 3 = quotient -6, remainder -2

BODMAS Principle: 
-------------------
Brackets      :  ()  
Of            :  power of 
              :  percent of 
              :  fraction of  
Division      :  %
Multiplication:  X
Addition      :  +
Subtraction   :  - 


II. Comparison :
-----------------

Symbol     Words            Example Use
-------------------------------------------------
==          equals           1 + 1 == 2  ==> True
≠          not equal to     1 + 1 ≠ 1  ==> True
>          greater than     5 > 7      ==> False
<          less than        7 < 9      ==> True
≥          greater than or 
           equal to         money ≥ 1
≤          less than or 
           equal to         bill ≤ 3
           
Combining:
----------
Example: Becky starts with $10, buys something and says "I got change, too". How much did she spend?
Answer: Something greater than $2 and less than $10 (but NOT $2 or $10):
        "What Becky Spends" > $2
        "What Becky Spends" < $10
        This can be written down in just one line:
        ===>  $2 < "What Becky Spends" < $10

That says that $0 is less than "What Becky Spends" (in other words "What Becky Spends" is greater than $0) and 
what Becky Spends is also less than $10.

Notice that ">" was flipped over to "<" when we put it before what Becky spends. 
Always make sure the small end points to the small value.

Changing Sides:
---------------
This:	 	                Becky Spends > $0	 	(Becky spends greater than $0)
is the same as this:	 	$0 < Becky Spends	 	($0 is less than what Becky spends)

An Example Using Algebra:
------------------------
Example: What is x+3, when we know that x is greater than 11?
         If x > 11 , then x+3 > 14
'''