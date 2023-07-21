'''22
Create a program that converts an amount of money from one currency to another based on current exchange rates.
I. Req: conversion of money from one currency to another currency
II. Analysis:
Technical Analysis:
1. User will enter the money in rupees.
2. convert money from rupee to usd.
3. print result.
Functional Analysis:
State : int
Behavior: Operators, Decision Making, Loops

III. Design:
1 inr = 0.012
if given input = 50 inr
usd = 50 * 0.0122 = 0.6 usd

1usd = 82.16
if given input = 50 usd
inr = 50 * 82.16 = 4108
'''
rupees = input("Enter Money end with INR/USD : ")
one_rupee = 0.012
one_usd = 82.25
if "INR" in rupees:
    rupees = rupees.strip("INR")
    usd = float(rupees) * one_rupee
    print(rupees, " rupees are ", usd, " Us dollars")
elif "USD" in rupees:
    rupees = rupees.strip("USD")
    inr = float(rupees) * one_usd
    print(rupees, " usd are ", inr, "Indian rupees")
else:
    print("Enter a valid amount")