# 23) Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))

if n1 == 0:
    gcd = abs(n2) #This is because 0 is a multiple of every integer
elif n2 == 0:
    gcd = abs(n1)
else:
    gcd = 1
    if n1 > n2:
        for i in range(1, n2 + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
    else:
        for i in range(1, n1 + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i

print("GCD:", gcd)




