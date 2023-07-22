# Write a program when you give number from terminal it should gives you that
#number in letters (1 to 10)(one to ten )


number_letter = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
num = int(input("Enter the number : ")) # 4, 5

if num in number_letter.keys():
   print(number_letter[num])
else:
   print('No output')
