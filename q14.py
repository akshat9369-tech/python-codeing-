#Write a program to check whether a number is palindrome.
num = int(input("enter a number "))
rev = 0
pre = num
while num !=0:
     div = num %10
     rev = rev *10 +div
     num = num //10
if  pre == rev:
     print("number is palindrome")
else:
     print("number is not palindrome ")
         