#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
   

def greet(name):
    print(f"Hello,{name}!")
greet("Angela")

def greet_with_default(name="programmer"):
    print(f"Hello,{name}")
greet_with_default("Tom")

def add(num1, num2):
    print(num1+num2)
add(10,20)

def halve(number):
    print(number/2)
halve(30)
