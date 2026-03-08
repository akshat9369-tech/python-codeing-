#Write a program to count number of digits in a number.
num = int(input("enter a number"))
count = 0
while num != 0:
     count = count +1
     rev = num //10 
print(f"number of digit in number is{count}")
    
