# sum=0
# for i in range(1,11):
#     sum+=i
    
# print (sum)


# x=int(input())
# sum=0
# for i in range(1,x+1):
#     sum+=i
    
# print (sum)

# i =1
# while i<=9:
#     print(i)
#     i=i+1
    
# row = 5
# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")

# s = 0
# n = int(input("Enter number "))
# for i in range(1, n + 1, 1):
#     s += i
# print("\n")
# print("Sum is: ", s)

# n = 2
# # stop: 11 (because range never include stop number in result)
# # run loop 10 times
# for i in range(1, 11, 1):
#     # 2 *i (current number)
#     product = n * i
#     print(product)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item)

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item)

# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item,end=' ')

# for num in range(-10, 0, 1):
#     print(num)

# for i in range(5):
#     print("Done!",i)
# else:
#     print("Done!")

# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(3, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)

# first two numbers
# num1, num2 = 0, 1

# print("Fibonacci sequence:")
# # run loop 10 times
# for i in range(10):
#     # print next number of a series
#     print(num1, end="  ")
#     # add last two numbers to get next number
#     res = num1 + num2

#     # update values
#     num1 = num2
#     num2 = res

# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on)
# for i in my_list[1::2]:
#     print(i, end=" ")

# input_number = 16
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

from turtle import *

# t=Turtle()
# t.speed(10)

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# for i in range(1,5):
#     t.forward(100)
#     t.right(90)

# t=Turtle()
# t.speed(0)
# t.color("red","black")

# t.begin_fill()
# for i in range(1,24):
#     t.circle(100)
#     t.right(15)
# t.end_fill()

# done()

# import turtle

# # Setup turtle
# turtle.speed(0)  # Set the speed of the turtle (0 = fastest)
# turtle.bgcolor("black")  # Set the background color
# colors = ["red", "yellow", "blue", "green"]  # List of colors

# # Draw the spiral
# for x in range(360):
#     turtle.pencolor(colors[x % 4])  # Set the pen color
#     turtle.width(x / 100 + 1)  # Set the pen width
#     turtle.forward(x)  # Move the turtle forward
#     turtle.left(59)  # Turn the turtle left

# # Exit on click
# turtle.exitonclick()

# import turtle

# t = turtle.Turtle()
# font = ("Arial", 12, "normal")

# x, y = 0, 100  # Example starting position
# t.penup()
# t.goto(x, y)
# t.pendown()

# text = "Hello, World!"  # Example text
# t.write(text, align="left", font=font)

# t.hideturtle()
# turtle.done()

# import turtle

# # Set up the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create the turtle object
# wheel = turtle.Turtle()
# wheel.speed(10)
# wheel.color("black")

# # Draw the wheel
# radius = 100
# spokes = 8
# angle = 360 / spokes

# for _ in range(spokes):
#     wheel.forward(radius)
#     wheel.backward(radius)
#     wheel.right(angle)

# # Hide the turtle
# wheel.hideturtle()

# # Exit on click
# turtle.done()
# import turtle
# import datetime

# # Set up the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.setup(width=600, height=600)
# screen.title("Analog Clock")
# screen.tracer(0)

# # Create the drawing pen
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.pensize(3)

# def draw_clock(h, m, s):
#     # Draw the clock face
#     pen.up()
#     pen.goto(0, 210)
#     pen.setheading(180)
#     pen.color("white")
#     pen.pendown()
#     pen.circle(210)

#     # Draw the hour marks
#     pen.up()
#     pen.goto(0, 0)
#     pen.setheading(90)

#     for _ in range(12):
#         pen.fd(190)
#         pen.pendown()
#         pen.fd(20)
#         pen.penup()
#         pen.goto(0, 0)
#         pen.rt(30)

#     # Draw the hour hand
#     pen.up()
#     pen.goto(0, 0)
#     pen.color("white")
#     pen.setheading(90)
#     angle = (h / 12) * 360 + (m / 60) * 30
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(100)

#     # Draw the minute hand
#     pen.up()
#     pen.goto(0, 0)
#     pen.color("white")
#     pen.setheading(90)
#     angle = (m / 60) * 360 + (s / 60) * 6
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(180)

#     # Draw the second hand
#     pen.up()
#     pen.goto(0, 0)
#     pen.color("red")
#     pen.setheading(90)
#     angle = (s / 60) * 360
#     pen.rt(angle)
#     pen.pendown()
#     pen.fd(50)

#     # Display the current time
#     pen.up()
#     pen.goto(0, -250)
#     pen.color("white")
#     pen.write(datetime.datetime.now().strftime("%H:%M:%S"), align="center", font=("Courier", 24, "normal"))

#     screen.update()

# while True:
#     h = datetime.datetime.now().hour
#     m = datetime.datetime.now().minute
#     s = datetime.datetime.now().second
#     draw_clock(h, m, s)
#     pen.clear()


 
# turtle.done()


# x=(1,'hello',2.55,4)
# print(x[1])
# print (len(x))

# x=(1,11,2.55,4,-100)
# print (sum(x))
# print (max(x))
# print (min(x))

# x=(10,"pakistan",22,3344)
# print(x[0:2])

# x=[3,"pak",33,55,"zinda"]
# x.append("bhaag")
# x.insert(2,"se")
# print(x)

# x={
#     "name": "ali",
#     "age":22,
#     "class":"6c"
# }

# print(x["class"])
# print(x["name"])
# print(list(x.keys()))
# print(list(x.values()))
# print(list(x.popitem()))
# x.update({"surname":"khan","DOB":"29july90"})
# print(x)

# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
    
# add(1,2)
# add(1,2,3,4,5)
# add(15,18,12);

# def add(x,y):

#     print(x+y)
    
# add(x=4,y=5)

# def add (**kwargs):
#     sum=0
#     for key,value in kwargs.items():
#         print("key:" , key, "value:", value)
#         sum+=value
#     print(sum)
    
# add(first_num=15,sec_num=10)

# def add (**kwargs):
#     sum=0
#     for x in kwargs.values():
#         sum+=x
#     print(sum)
    
# add(first_num=15,sec_num=10)

# import sys
# print(sys.argv)

# try:
#     x=int(input())
#     print(x)
# except (ValueError,ZeroDivisionError):
#     print("wrong value")

# try:
#     x=int(input())
#     print(x/0)
# except ValueError:
#     print("wrong value")
# except ZeroDivisionError:
#     print("U divide by zero")
# finally:
#     print("finally result")

# x= "apple"
# if type(x) is not int:
#     raise Exception("type not match")

# x= 5
# if type(x) is not int:
#     raise Exception("type not match")

# file= open("text.txt",'r')
# print(file.read())
# file.seek(0)
# file.close()

# file= open("text.txt",'w')
# file.write(" hi , how r u")
# file.close()

# file = open('text.txt', 'w+')
# file.write(' \n Hello, world!')
# file.seek(0)
# print(file.read())
# file.close()

# file = open('text.txt', 'a+')
# file.write(' \n Hello, world222!')
# file.seek(0)
# print(file.read())
# file.close() 

# with open('myfile.txt', 'r') as file:
#     file.seek(0)
#     # Perform operations on the file
#     content = file.read()
# File is automatically closed outside the 'with' block


# class Car:
#     x=5

# c1=Car()
# c2=Car()
# print(Car.x)
# print(c1.x)

# c1.x=10
# c2.x=20
# print(c2.x)
# print(c1.x)

# Car.x=30
# print("after")
# print(Car.x)
# print(c1.x)
# print(c2.x)

# class Car:
#     x=5
#     y=77
        
#     def classFunc():
        # print("class xxx")
        
#     def __init__(self,name):    
#         self.name=name
    
        
#     def objFunc(self):
#          print(self.name)
         
# c1=Car("c1 carAA")
# c2=Car("c2 carBB")           
 
# c1.objFunc()
# c2.objFunc()

# Car.classFunc()

# def test(y):
#     y()
    
# def printer():
#     print(" i m boy")
    
# test(lambda: printer()) 

# final_list=list(map(lambda x:x*3, [1,2,3,4,5]))

# print(final_list)   

# final_list=list(filter(lambda x: (x%2!=0), [1,2,3,4,5]))

# print(final_list)  

# a=[1,2,3]
# b=["one","two","three"]

# final_list= list(zip(a,b))
# print(final_list) 


# class Emp:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def sed(self):
#         print ("name", self.name)
#         print ("age", self.age)
#         print ("salary",self.salary)
        
# class Empp(Emp):
#     def __int__(self,name,age,salary,gender,dob):
#         super().__init__(name,age,salary)
#         self.gender = gender
#         self.dob = dob
        
#     def sedd(self):
#         print ("gender", self.gender)
#         print ("DOB", self.dob)
#         print ("add two other properties")   
        
             
        
# e1 = Empp('Ali',32,234324,'male',1992)
# e1.sedd()



# import random

# # List of words for the game
# words = ["apple", "banana", "cherry", "grape", "orange", "kiwi", "mango", "pear"]

# def choose_word():
#     return random.choice(words)

# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def hangman():
#     word = choose_word()
#     guessed_letters = []
#     attempts_left = 6

#     print("Welcome to Hangman!")
    
#     while True:
#         print("\n" + display_word(word, guessed_letters))
#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess in word:
#             print("Correct!")
#         else:
#             attempts_left -= 1
#             print(f"Wrong! You have {attempts_left} attempts left.")

#         if "_" not in display_word(word, guessed_letters):
#             print("\nCongratulations! You guessed the word:", word)
#             break

#         if attempts_left == 0:
#             print("\nGame Over! The word was:", word)
#             break

# if __name__ == "__main__":
#     hangman()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
