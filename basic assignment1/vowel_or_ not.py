#write a program to check if the given charecter is vowel or not.


vowel = ['a', 'e','i', 'o', 'u']
charecter = input("Enter the letter :")
if charecter.lower() in vowel:
    print("The given letter is vowel :")
else:
    print("It's not vowel")
