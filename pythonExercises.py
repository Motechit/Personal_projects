#Class Exercise 1
# User input, type casting and format string
"""
miles = input("How many miles left? ")
miles_to_km = int(miles) * 1.60934
print(miles, " miles = {} kilometers".format(miles_to_km))

#OR

miles = int(input("How many miles away are you?: "))
conversion = miles * 1.60934
print(f"{miles} mile equals {conversion} kilometers")
"""

# Class Exercise 2
# Calculator that takes user input
"""
calculation = input("Enter calculation: ")
num1, op, num2 = calculation.split()
num1 = int(num1)
num2 = int(num2)
if op == "+":
    print(f"{calculation} = ", num1 + num2)
elif op == "-":
    print(f"{calculation} = ", num1 - num2)
elif op == "*":
    print(f"{calculation} = ", num1 * num2)
elif op == "/":
    print(f"{calculation} = ", num1 / num2)
elif op == "%":
    print(f"{calculation} = ", num1 % num2)
else:
    print("Enter a valid operation")

#OR

num1, operator, num2 = input("Enter calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
elif operator == "//":
    print("{} // {} = {}".format(num1, num2, num1 // num2))
else:
    print("Use either +, _, *, /, //, %")
"""

# Class Exercise 3
# Use lesser lines of code and use all the knowledge gained in class
# Class based on age
# If age is 5 "Go to kindergarten"
# If age is from 6 to 17 "Go to Grade __". Grade should be btw 1-12
# If age is greater than 17, "Go to College"
"""
age = int(input("Enter age: "))
if (age < 5):
    print("Go to Creche")
elif (age > 5) and (age <= 17):
    class_to_go = age - 5
    print("Go to Grade {}".format(class_to_go))
else:
    print("Go to college")

# OR

age = int(input("Enter your age: "))
if age <= 5:
    print("Go to Kindergarten")
elif age ==6 or age <= 17:
    print("Go to Grade 6")
elif age > 17:
    print("Go to college")
"""

# Class Exercise 4
# Ternary Operator
"""
age = int(input("What is your age?"))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)
"""

# Class Exercise 5
# Print out all odd numbers between 1 to 20
"""
for num in range(21):
    if num % 2 ==0:
        pass
    elif num % 2 !=0:
        print(num, end= ",") # or print("num = ", num)
"""

# Class Exercise 6
# Convert a float to 2 decimal place
"""
float_num = float(input("Enter a float number: "))
print("Rounded to 2 decimals: {:.2f}".format(float_num))
"""

# Class Exercise 7
# import random
# rand_num = random.randrange(1, 51)
# i = 1
# while i != rand_num:
#     i += 1 # i = i + 1
# print("The random number is:",rand_num)

# Guess a random number and if it matches, print out the number
"""
import random
random_num = random.randrange(21)
guessed_num = int(input("Enter a number btw 0 and 20: "))
i = 1
while i != 2:
    if guessed_num != random_num:
        i += 1
        print("Guess again!, random number = ", random_num)
    else:
        print("You guessed right! Random number = ", random_num)
"""

# Class Exercise 8
# Print a pine tree as tall as the user wants it to be
"""
height = int(input("How tall should the tree be?: "))
spaces = height - 1
hashes = 1
stump_spaces = height - 1
while height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    height -= 1
for i in range(stump_spaces):
    print(" ", end="")
print("#")
"""



















