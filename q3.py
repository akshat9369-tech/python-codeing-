#Write a program to find the largest of three numbers.
num1,num2,num3 = map(int, input("enter the  three number").split())
if num1 >= num2 and num1>= num3:
    print("num1 is greatest ")
elif num2 >=num1 and num2>= num3:
    print("num2 is greatest ")
else:
    print("num3 is greatest ")
          
