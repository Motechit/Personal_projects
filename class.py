# This is our first program in Python class
"""
I printed my name and age on the console storing my data
in a variable
"""

"""
print("Hello world!")

name = "Khalid Kodaolu"
age = str(18)  #Type casting/conversion

#print("Hello",name, "your age is", age)
print("Hello " + name + " your age is " + age)
# print(type(age))
"""
"""
userNAME = input("Enter your desired user name: ")
DateOfBirth = input("Enter your date of birth: ")
school_of_choice = input("What school do you attend?: ")
print("Data stored successfully")
"""

"""
# print(2 + 4)

num1 = input("First Number: ")
num2 = input("Second Number: ")
print("The sum of the two numbers is: ", int(num1) + int(num2))
"""

"""
Write a program that:
Asks the user to input the number of miles
You’ll convert miles to kilometers (kilometers = miles * 1.6 0934)
Then print this for example 5 miles equals 8.0467 kilometers
"""

"""
# Naming a variable
_name1 = "Python"
# print(_name1)

# Data Types
int_num = 10  # int
float_num = 10.2  # float
complex_num = 1 + 4j  # complex

print(type(complex_num))

cars = ["benz", "toyota", "mazda", "tesla"]  # This is a list
cars2 = ("benz", "toyota", "mazda", "tesla")  # This is a tuple

# a, b, c, d = cars
# print(cars[3])
print(type(cars))  # The type() function helps to check the data type we're working with
print(len(cars2))  # The len() function helps to check the length of the data we're working with


my_dictionary = {
    "name": "khalid",
    "class": "Python",
    "age": 14,
    "option": True
}

my_set = {12, 24, 36, 48, 60}

# Convert a float to 2 decimal place
float_num = float(input("Enter a float number: "))
print("Rounded to 2 decimals: {:.3f}".format(float_num))


age_bracket = range(6, 13)
# print(tuple(age_bracket))

cal = 2 + 3  # -, *, /, //, %, =, ==

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
result = num1 + num2
print("The addition of {} and {} = ".format(num1, num2), result)
# OR
print(F"The addition of {num1} and {num2} = {result}")
"""

# Assignment
# operation = input("Enter 2 operands and an operator")
# print(operation)

# Hint: You can make use of a string method, hence, find out the method suitable


"""
# Connecting to a database
# importing 'mysql.connector' as mysql for convenience
import mysql.connector as mysql


# from mysql.connector import Error
# using the 'connect' method and the 3 required parameters
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dbms"
)
print(db)  # It will print a connection object if everything is fine
"""

# Use lesser lines of code and use all the knowledge gained in class
# Class based on age
# If age is 5 "Go to kindergarten"
# If age is from 6 to 17 "Go to Grade __". Grade should be btw 1-12
# If age is greater than 17, "Go to College"

"""
age = int(input("Enter your age: "))
height = float(input("Enter your height (in inches): "))
year = int(input("Enter jamb year: "))
if 18 <= age <= 21:
    if 5 <= height >= 6:
        if 2023 <= year >= 2028:
            print("Congratulations, candidate is eligible!")
        else:
            print("Candidate is not eligible based on the jamb year")
    else:
        print("Candidate is not eligible based on your height")
else:
    print("Candidate is not eligible based on age")


name = "dimeji"
print(name.capitalize())
print(type(name))
print(len(name))

numbers = [13, 1, 12, 24, 2]
print(min(numbers))
print(max(numbers))


num = -10.298544
nums = 10.945532
print(round(nums))

from math import *
print(ceil(nums))
print(floor(nums))


name = "Khalid"
#
string = "My name is {}"
#print(string.format(name))
string = F"My name is {name}"
print(string)


# Example ="hello sweet"
# print(Example.capitalize())

Example = "Rice, Beans, Garri"
print(type(Example))

print(Example.find("Garri"))

example = "Rice", "Beans", "Garri"
print(type(example))


name = "Alice"
age = 30
city = "Wonderland"
# Using the format() method with curly braces as placeholders

message = "Hello, my name is {}. I am {} years old and I live in {}.".format(name, age, city)
# print(message)
"""

# Classwork
# Collect details you'd need when cooking for a diabetic patient
# Print out your conclusion regarding the meal you've decided and the cooking method you'd recommend.
# Using both format method and f-string

# Booleans
# print(22 == 22)
i = 7
# print("Is 7 even?: ", i % 2 == 0)

# print(bool("Khalid"))

TheString = "I am a Champion"
checkString = TheString.startswith("a")
# print(checkString)

# age = 25
# is_student = False
#
# if age < 18 or is_student:
#     print("You are either a student or under 18")
# if age >= 18 and not is_student:
#     print("You are an adult and not a student")

quotedString = "I will be like the ten \t \\wise virgins"
# print(quotedString)

















