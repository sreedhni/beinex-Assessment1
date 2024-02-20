#14) Write a Python program to check if a given year is a leap year.
yr=int(input("enter the year:"))
is_leap=False
if(yr%100==0) and (yr%400==0):
    is_leap=True
elif(yr%4==0) and(yr%100 !=0):
    is_leap=True
if is_leap:
    print(yr,"is leap year")
else:
    print(yr,"is not leap year")
