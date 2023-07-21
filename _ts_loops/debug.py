num = int(input("Enter the number to find Prime Factors : "))
factors = []
for i in range(2, num):
    if num % i == 0:
        factors += [i]
print(factors)
prime_fact = ""
for j in factors:
    c = 0
    for h in range(2, j):
        print(h)
        if j % h == 0:
            c += 1
    if c == 0:
        prime_fact += str(j) + " "
        print(prime_fact)