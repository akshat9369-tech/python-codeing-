#Write a program to find factorial of a number.
num =int(input("enter a number"))
fac =1
for i in range ( 1, num+1):
    fac = fac *i
#print(f" the factorial of {num} is{fac} ")
print(" the factorial of num is ", fac)