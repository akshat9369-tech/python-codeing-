#Write a program to swap two numbers (using third variable).
num1= int(input("enter the first num:"))
num2= int(input(" enter the second num:"))
print( "orignal order", num1 , num2 )
num3 = num1 
num1 = num2
num2 = num3
print("swap order is ", num1, num2)
