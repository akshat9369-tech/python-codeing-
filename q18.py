#Write a program to count number of vowels in a string.
x= input("enter a word")
vowel ="aeiouAEIOU"
count = 0
for i in x:
    if i in vowel:
        count += 1
print("vowel int he word are ", count)