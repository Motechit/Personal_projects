#String Exercises
#1
number = 111102
print(f"Olabisi Onabanjo Way, {number}, Abẹ́òkúta, Ìpínlẹ̀ Ògùn")
#2
pie = 3.14159
print(f"The value of pi is {pie:.2f}")
#3
my_school = "Programming College"
print(3 * my_school)
print(my_school[:9])
#4
string1 = "Programming"
string2 = "College"
string1 += " " + string2
print("Welcome to {}!".format(string1))

#NO in manual
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
print(str[39:66] + str[105:111] + str[0:6])

#print(object-oriented programming + with + python)
#i.e concatenate the indices to give object-oriented programming with python

#If statement exercise
#user grading program
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"
print("Your grade is:", grade)

#user Authentication
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Azeezat" and password == "secret1@":
    print("Login successful!")
else:
    print("login failed. Invalid credentials.")

#calculate ticket price based on age and time of day
age = int(input("Enter your age: "))
time_of_day = input("Enter time of day (morning/afternoon/evening): ")

if age <= 18:
    if time_of_day == "morning":
        price = 5
    if time_of_day == "afternoon":
        price = "free"
    else:
        price = 10
else:
    if time_of_day == "afternoon":
        price = 35
    elif time_of_day == "evening":
        price = 15
    else:
        price = 20
print(f"Your ticket price is ${price}.")


#Exercise on loops and error handling
while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number < 0:
            print("Please enter a non-negative integer.")
            continue

        factorial = 1
        for n in range(1, number + 1):
            factorial *= n

        print(f"The factorial of {number} is", factorial)
        break  # Exit the loop when the calculation is successful
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


#Exercise on looping through a Tuple
'''
#No1
my_tuple = (5, 10, 15, 20, 25)
for elements in my_tuple:
    print(elements)

colors = ('red', 'green', 'blue', 'yellow')
for index, color in enumerate(colors):
    print(f"{index}: {color}")

#No2
number = (7, 12, 5, 3, 9)
sum_of_numbers = 0

for num in number:
    sum_of_numbers += num

print(sum_of_numbers)

#No4
numbers = (3, 8, 15, 12, 5, 6)
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

data = ( ('Alice', 25),('Bob', 30), ('Charlie', 22))
for person in data:
    name = person[0]
    # if len(person) > 1:
    age = person[1]
    print(f"{name} is {age} years old.")

number 6
fruits =('apple', 'pineapple', 'guava', 'orange')
for f in fruits:
    l_o_f = len(f)
    print(f"the length of {f} is {l_o_f}")


#N07
numbers = (1, 2, 3, 4, 5)
for num in reversed(numbers):
    print(num)

#No8
values = (7,10,13,16)
total_index = 0
total_element = 0
for index,value in enumerate(values):
    total_index += index
    total_element += value
print(f"total index= {total_index} ,total element= {total_element}")

#9
#a man a plan a canal panama
words = ("apple","level", "banana","civic", "orange")
for word in words:
    check_word = word
    if check_word == check_word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

10
for i in range(1,6):
    print("multiplication table for:" + str(i))
    for j in range(1,11):
        result = i *j
        print(f"{i}*{j} = {result}")
'''

library_catalog = {
    "978-0451524935": {
        "Title": "7 Habits of Successful People",
        "Author": "Steve Covey",
        "Publication Year": 1989,
        "Genre": "Self-help"
    },
    "ISBN of the next book": {

    }
}


#Exception Exercise (11)
try:
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Attempt the division operation
    result = num1 / num2

    # Display the result
    print(f"Result of division: {result}")

except ZeroDivisionError:
    # Handle the division by zero error
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle the ValueError (e.g., if the user enters a non-numeric input)
    print("Error: Invalid input. Please enter numeric values.")

# FizzBuzz Test
# Write a short program that prints each number from 1 to 20 on a new line.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

numbers = range(1, 21)
for num in numbers:
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 15 == 0:
        print("FizzBuzz")
    else:
        print(num)
# Define the data or numbers you're going to be working with
# Use a control flow structure(s)
# State the conditions to be satisfied
#1. If the number is divisible by 3, it should output "Fizz"
#2. If the number is divisble by 5, it should output "Buzz"
#3. If the number is divisible by both 3 and 5, it should output "FizzBuzz"
#4. If none of this conditions hold, it should print the number
# End of Test















#
#import the file calculator_1 import functions
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

def print_list_integer(my_list=[]):
    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))