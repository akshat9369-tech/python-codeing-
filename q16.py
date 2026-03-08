#Write a program to find sum of digits of a number.
num = int(input("enter the number"))
sum =0
while num!=0:
    rev = num %10
    sum = sum +rev
    num = num //10
print(f"sum of the digit is {sum}")


