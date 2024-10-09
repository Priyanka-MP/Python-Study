"""
Given as integer as input:
if it is only a multiple of 3 print only Fizz
if it is only a multiple of 5 print only Buzz
if it is only a multiple of 3 & 5 print only Fizz-Buzz
"""
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

num = int(input("Enter an number: "))
fizz_buzz(num)                