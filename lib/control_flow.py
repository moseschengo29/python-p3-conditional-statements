#!/usr/bin/env python3
def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 65 > temperature > 40:
        return "It's a little chilly out there!"
    elif temperature > 80:
        return "It's too dang hot out there!"  
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if num % 3 ==0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 ==0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return None
    else:
        return "Invalid operation!"

admin_login('admin', '12345')
admin_login('sudo', '12345')

hows_the_weather(75)
hows_the_weather(33)
hows_the_weather(99)

num1 = fizzbuzz(3)
print(num1)