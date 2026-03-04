#Write a program to calculate simple interest.
principle , rate, time = map(int, input("enter the princple , rate , time for simplem intrest").split())
si = (principle *rate *time)/100
print("simple intrsest is :", si)
