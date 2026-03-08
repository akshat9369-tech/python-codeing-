#Write a program to count uppercase and lowercase letters.
word= input("enter a word ")
upper =0
lower =0

for ch in word:
    if ch.isupper():
        upper +=1
    if ch.islower():
        lower +=1
print("The number of lower element are ", lower)
print("The number of upper element are ", upper)
