#Write a program to check whether a number is prime or not.
num = int(input("enter a number"))

if num <=1:
    print("number is not prime")
else:
    is_prime= True
    for i in range (2 , num):

        if num %i == 0:
            is_prime = False
            break
    if is_prime:
        print("number is prime")
    else:
        print("number is not a prime")