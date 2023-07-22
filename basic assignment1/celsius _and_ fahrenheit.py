#write a python program to convert temp to celsius and fahrenheit.


def celsius_to_fahrenheit():
    celsius_temp=int(input("Enter the temp of celsius to convert into fahrenheit : "))
    fahrenheit = ( celsius_temp * 9/5) + 32
    print(f"Temp in fahrenheit {fahrenheit}")

celsius_to_fahrenheit() 

def fahrenheit_to_celsius():
    farenheit_temp=int(input("Enter the temp of fahrenheit to convert into celsius : "))
    celsius = ( farenheit_temp - 32) * 5/9
    print(f"Temp in celsius {celsius}")
    
fahrenheit_to_celsius()