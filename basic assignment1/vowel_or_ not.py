'''
@Author: Amreen shaikh
@Date: 2023-7-22
@Last Modified by: Amreen shaikh
@Last Modified : 2023-7-22
@Title :write a program to check if the given charecter is vowel or not. 

'''

vowel = ['a', 'e','i', 'o', 'u']
charecter = input("Enter the letter :")
if charecter.lower() in vowel:
    print("The given letter is vowel :")
else:
    print("It's not vowel")
