# greats of 3number and smallest of 3 number.

num1 = int(input("Enter the 1st no : "))  #10 , 10   
num2 = int(input("Enter the 2st no : ")) #20  , 30
num3 = int(input("Enter the 3st no : ")) #30,  20
  
if (num1 >=num2)  and (num1 >=num3) :
    print(num1)
elif (num2 >=num3)  and (num2 >=num1):
    print(num2)
elif (num3 >=num2)  and (num3 >=num1):
    print(num3) 
else:
    print("all numbers  are same : ")

#lst =  [num1, num2, num3]

#large = max(lst)
#small = min(lst)

#print(f"Greats number is : ", {large})
#print(f"Smallest number is : ", {small})
