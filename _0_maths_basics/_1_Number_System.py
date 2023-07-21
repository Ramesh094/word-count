''''''
'''Winzip, Notepad++ 

https://www.mathsisfun.com/unit-conversion-tool.php
'''

S = '''
Number System
=====================
                    NUMBERS
Natural     Whole       Integer     Rational        Irrational
             - Even nos
             - Odd nos
             - Prime nos
             - Composite nos

Natural Numbers : 1,2,3,4,5.....
Whole Numbers   : 0,1,2,3,4.....  0 + natural numbers
                      Even  : 2,4,6,8,10....
                      Odd   : 1,3,5,7,9.....
                      Prime : 2,3,5,7,11....
                      Comp  : 4,6,8,9,12....
Integers*       : {......-3,-2,-1,0,1,2,3,......}   ==> int *
Decimal*        : 12.3, 54.32, -34.432              ==> float *
Rational        : 2/3, 3/5 --> 0.6, -2/7
Irrational      : π, √3, √5 
Real nos        : Rational + Irrational
Imaginary nos*  : 3i+4j                              ==> complex *
                        # 3 realno # 4 imaginaryno

CONCEPT:
----------------                 MATHS                 PYTHON
int decimal            ==>  Number System    ===> Data Types: Numbers: 
                                                                        int 
                                                                        float 
                                                                        complex
                                                             : Boolean:
                                                             : String    
Set, Sequence, Matrix  ==>  Adv topics       ===> Data Structures
                                                                   String, 
                                                                   List, 
                                                                   Tuple, 
                                                                   Dictionary, 
                                                                   Set


Entity: 
    1. STATE     : Datatypes/DataStructures
    2. Behavior  : Operators, DM, Loops    : Functions/OOPs
                ------------------
                | int eid = 100  |     eid = 10   ( x = 10 )
                ------------------
Entity: Employee 
===================
    1. STATE:
    ---------   
                 int eid = 100    
                ================
variable: Attributes: eid, name, sal, location, mobile, mailid, is_perm
value   : Values    : 100, Madhu, 10000, Bangalore, 324324234, email@gmail.com, True
type    : datatypes:  int, str, float, str, str, str, bool

    2. BEHAVIOR:
    --------------
    CRUD : CREATE / RETRIEVE / UPDATE / DELETE 
        - Create an Employee     : Onboarding  
        - Retrieve Employee info : By Employee / Organization
        - Update                 : Address / Mobile 
        - Delete Employee        : While resignation / termination
  

Entity: Student 
===================
    1. STATE:
    ---------   
                 int rno = 100    
                ================
variable: Attributes: rno, name, marks, gender, class, section, result, school, location, par_contnum, dob
value   : Values    : 100, Madhu, 54, Male, 5th, B, True, "DPS", "Bangalore", 324324, 14-Jun-32
type    : datatypes:  int, str, float, str, str, str, str, bool

    2. BEHAVIOR:
    --------------
    CRUD : CREATE / RETRIEVE / UPDATE / DELETE 
        - Create Student         : While joining school  (School)
        - Retrieve Student info  : By Student / School
        - Update                 : Parentscontactnum, Addr, MailID / Marks, Grade, Class, Section 
        - Delete Student         : While leaving / Termination
  



DATA TYPES/ STRUCTURES :
========================
==>Data types --> Individual values 
    --> Number system   int*    :   100, 120, -5, -23
                        float*  :   14.3,  25.4   -14.5
                        complex :   3i+4j
                        
    --> Boolean         True/False   1/0       
    
==>Data structures --> Collection(Group) of individual values 
                      
                   ==>    Maths  : Matrix , Sequence,         Set      
                   ==> Python    : String, List, Tuple     Dictionary, Set       


Conversion in mathematics :
---------------------------
Conversion : Measurement: to change from one unit to another 
                          such as from inches to millimeters, or liters to gallons

Temperature:
°C	  °F	Description
37	98.6	Body temperature

Length:   
            1 km = 1000 m
            1 m  = 100 cm
            1 cm = 10 mm    ==> 1 KM + 100 M ==>  1KM + 0.1KM = 1.1 KM   Internal conversion(Same category)
                                                 1000M + 100M = 1100 M
            1 KM + 2 KM ==> 3KM  : 3000M                                   
                                              ==> 100KM + 10M - 100.01KM
            2x+3x = (2+3)x  = (5)x = 5x
Mass:
            1 tonne = 1000 kg
            1 kg    = 1000 gm
            1 gm    = 1000 mg
            1 mg    = 0.0154 grain


            
Volume/Capacity:
            1 liter = 2.113 fluid pt
 
5 KG + 3 KG = 8 KG 
2 Dozen + 5 Dozen = 7 Dozen
3L water + 5L Oil = 8L
    - Calculate quantity ? YES - 8L
    - Mixture               NO - ERROR

3L water + 5L Milk = 8L
    - Calculate quantity ? YES - 8L
    - Mixture              YES - 8L Milk



2 Dozen eggs + 5 KG Rice + 3 L Water + 1 KM  ==> XXX Invalid statement 

1GB = 1024 MB
1 MB = 1024 KB 
1KB = 1024 bytes
1 byte = 8 bits 
___________________________________________
0 1 0 1 0 1 0 1 
___________________________________________

Variable Declaration:
---------------------
int   - 2 bytes     1 byte = 8 bits
float - 4 bytes
                                         CAN        Water
                                         -----      ---------
int x = 10     # YES                      2L   <--   2L
float x = 10.5 # YES                      5L   <--   5L
float x = 10   # YES   10.0               5L   <==   2L          - Implicit casting
int x = 10.4   #  NO   int x = (int)10.4  2L   <==   5L          - Explicit casting


x = 10    # int
x = 10.5  # float




'''
'''
Number System <==> Data types


Integer Whole Fractional Real  Imaginary   ==> Data Types     ===> int float boolean String
Sets, Sequences, Matrices                  ==> Data Structures ==> List Tuple Dictionary Set

List<Integer> li = new ArrayList<Integer>();
li.add(10)
li.add(20)
li.add(30)
li.add(40)

li = [10, 20, 30, 40]

 

'''
