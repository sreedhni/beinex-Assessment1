# 22) Write a Python program to check if a given number is a perfect number.
try:
    num = int(input("Enter the number: "))
    sum_of_divisor = 0

    if num <= 0:
        print("It is a non-positive number, so it is not a perfect number.")
    else:
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisor += i

        if sum_of_divisor == num:
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")

except ValueError:
    print("Invalid input! Please enter a valid integer value.")
