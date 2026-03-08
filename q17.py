#Write a program to print multiplication table of a number.
num = int(input("enter a number"))
for i in range(1 , 10):
    print(f"{i}*{num}= {i*num}")
    