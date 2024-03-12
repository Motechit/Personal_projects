# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello World!")

x = 3
print(x)

print(float(x))

fnumber = int(input("Enter first number..."))
snumber = int(input("Enter second number..."))

total = fnumber + snumber

print(total)

#one value to multiple variables
x = y = z = "Oranges"
print(z)

#many values to multiple variables
n, m, k, = 6, 8, 10
print(m)

#unpack a collection
Fruits = ["A", "B", "C"]
x, y , z = Fruits
print(x)
print(y)
print(z)


#RANDOM NUMBERS

import random
my_random = random.randrange(1,10)
print(my_random)

if my_random ==6:
    print("You win!")
else:
    print("Try again...")


name = '''
My name is Mosunmola
I love programming
I live in Abeokuta.
'''

print(name)

name = "Kazim"

for l in name:
    print(l)

desc = "I am from Nigeria though I was born in the North pole."

if "Ghana" in desc:
    print("Yes it is")
else:
    print("No it isn't")

#Slice string#
a = "Hello, world"

print(a[3:9])
#Slicefromstart andend#
print(a[:10])
print(a[7:])

#Negativeslicing#
print(a[-1])
print(a[11]) #to get "d" both will work#
print(a[-12:-7])

#String modification
a = "hello, world"
print(a.upper())
print(a.lower())
print(a.replace("h", "Y"))
print(a.split(","))

#Stringconcatenation#
a = "hello"
b = "world"
print(a + " " + b)

Fruits = ["A", "B", "C"]
x,y,z = Fruits
print(x + " " + y + " " + z)

#Formatstring
a = "hi "
b = str(5)

print(a + b)

age = 20
my_bio = "My name is john, I am {} years old"

print(my_bio.format(age))

price = 25.38
quantity = 5

my_order = "I bought {1} quantity of milk for {0} naira"

print(my_order.format(price, quantity))

#Escapecharacters#
d = " Former President Obansanjo said \"Nigeria will be great again\""

print(d)

d = 'It\'s alright. It will surely be alright.'
print(d)

d = 'It\'s alright. \nIt will surely be alright. \nJust hang on.'
print(d) #Newline#

d = 'hello\rjohn'
print(d) #carriagereturn#

d = 'hello \bjohn'
print(d) #nackspace#

#Python Booleans
print(4>2)

print(bool(0))

x = 13
print(bool(x))

def myFunc():
    return True

if myFunc():
    print("Yes")
else:
    print("No")

number = 6
print(isinstance(number, int))

#python operators
print(5 // 4)
print(5 % 4)

t = 5
t = t + 1 #t += 1
print(t)

t = 5
t -= 2
print(t)

t = 5
t *= 2
print(t)

'''
5 = 101
3 = 011
'''
t = 5
t &= 3 #we have to convert to their binary equivalent
print(t)

t = 5
t |= 3 #convert 111 to base 10
print(t)

t = 5
t ^= 3 #convert 110 to base 10
print(t)

t = 5
t <<= 3
print(t)

t = 5
s = 3
print(t == s) #print(t != s)

#both conditions must be true
t = 5
s = 5
if t > 5 and s < 10:
    print("Absolutely")
else:
    print("Weird")

t = ("hello")
if "z" not in t:
    print("no, not in")

#one condition is sufficient for the opertaion to be executed
t = 5
s = 5
if t > 5 or s < 10:
    print("Absolutely")
else:
    print("Weird")

#not reverses the whole condition
t = 5
s = 5
if not t > 5 or s < 10:
    print("Absolutely")
else:
    print("Weird")

#LISTS
schools = ["unilag", "uniben", "Futminna", "Futa"]
print(schools[3])
#to change a list
schools[3] = "funab"
print(len(schools))
#relationship btw length and the last/any variable in the list
idx = len(schools) - 1
print(schools[idx])
#to find out the data type in a list
values = ["Yes", 6]
a = values[1]
print(type(a))
#creating a list with a list constructor
fruits = list(("apple", "mango", "banana", "guava"))
print(fruits)
#range of index #
print(fruits[1:4])
#using step index to get range
fruits = list(("apple", "orange", "banana", "pawpaw", "cashew", "mango", "cherry"))
print(fruits[0:6:2])
#if statement
fruits = list(("apple", "orange", "banana", "pawpaw", "cashew", "mango", "cherry"))
if "pineapple" in fruits:
    print("yes, it is in fruits")

#list comprehension
list1 = [25, 67, 13, 8, 49, 19]

print([g for g in list1 if g > 20])

#sort lists
nums = [3,5,7,2,0,1,9,8]
nums.sort()
print(nums)

#decendingorder
nums.sort(reverse=True)
print(nums)

nums = [100, 50, 65, 82, 23]
def sort_num(n):
    return abs(n-50)

nums.sort(key=sort_num)
print(nums)

nums = [100, 50, 65, 82, 23]

def sort_num(n):
    return abs(n-50)

nums.sort(key=sort_num)
print(nums)


fruits = ["apple", "orange", "banana", "mango", "Watermelon"]
fruits.sort(key = str.lower)
print(fruits)

#copylist
list1 = [25,67,13,8, 39,19]

list2 = []
list2.copy(list)

print(list2)
print(list1)

#or
list1 = [25,67,13,8, 39,19]

list2 = list(list1)

print(list2)
print(list1)



#join/concatenate 2 lists
list1 = [25,67,13,8, 39,19]

list2 = []
list2.list()
list1.append(45)

print(list2)
print(list1)

list1 = [25,67,13,8, 39,19]
list2 = ["a", "b", "c", "d"]
list3 = list1 + list2
print(list3)

list1 = [25,67,13,8, 39,19]
list2 = ["a", "b", "c", "d"]

for y in list2:
    list1.append(y)
print(list1)

list1 = [25,67,13,8, 39,19]
list2 = ["a", "b", "c", "d"]

list1.extend(list2)
print(list1)

#Tuple
mytuple = ("apple", "orange", "banana")
#relationship btw len and the highest element in a tuple
a = len(mytuple) - 1
print(a)

cars = ("benz",)
print(type(cars))

nums = (1,2,3,1)
print(type(nums))

countries = tuple(("Nigeria", "Spain", "Ukraine"))
#print(countries[1:2])
j = "USA"
for a in countries:
    if j.lower() in a.lower():
        print("yes it is")
        break
    else:
        print("no, it is not")
        break


#changing a tuple by converting to a list
countries = tuple(("Nigeria", "Spain", "Ukraine"))
tup_list = list(countries)
tup_list[1] = "Canada"
print(tup_list)

new_tup = tuple(tup_list)
print(new_tup)


#add to a tuple
countries = tuple(("Nigeria", "Spain", "Ukraine"))
y = list(countries)
y.append("Egypt")
countries = tuple(y)
print(countries)
#or
countries = tuple(("Nigeria", "Spain", "Ukraine"))
new_country = ("Egypt",)
countries = countries + new_country
print(countries)

#remove element of a tuple
countries = tuple(("Nigeria", "Spain", "Ukraine"))
list = list(countries)
list.remove("Spain")
countries = tuple(list)
print(list)

#or
countries = ("Nigeria", "Spain", "Ukraine")
country_to_remove = "spain"
countries = tuple(c for c in countries if c.lower() != country_to_remove.lower())
print(countries)


#unpacking a tuple
languages = ("python", "PHP", "java", "cpp")
(lang1, lang2, *lang3) = languages
print(lang3)

#loop through a tuple
#loop through value/items
languages = ("python", "PHP", "java", "cpp")
for r in languages:
    print(r)

#loop through position/index
languages = ("python", "PHP", "java", "cpp", "ruby", "c")
#for r in range(4):
 #   print(r)

for r in range(len(languages)):
    print(languages[r])

#while loop
languages = ("python", "PHP", "java", "cpp", "ruby", "c")

j = 0

while j < len(languages):
    print(languages[j])
    j +=1

languages = ("python", "PHP", "java", "cpp", "ruby", "c")
languages2 = ("javascript", "kotlin")

all_lang = (languages + languages2 * 2)
print(all_lang)


#SET
myset = {1,2,3,4,5,6}
print(type(myset))

#print an item in the set
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
#print(len(my_set))

for x in my_set:
    if x == "blue":
        print(x)

#check if an item is present in a set
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
#print("blue" in my_set)

if ("blue" in my_set):
    print("of course")
else:
    print("oh no")

#add an item to a set
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
# pink = "pink"
my_set.add("pink")
print(my_set)

#update a set with a set
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
new_set = {"pink", "orange"}
my_set.update(new_set)
print(my_set)

#update a set with an iterable (list)
list1 = ["white", "black"]
my_set.update(list1)
print(my_set)

#remove an item from a set
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
my_set.remove(False)
print(my_set)

#discard
my_set = set(("blue", "red", "purple", "green", "blue", False, 0))
new_set = {"pink", "orange"}
list1 = ["white", "black"]
my_set.update(new_set)
my_set.update(list1)

my_set.discard("red")
print(my_set)

#pop, clear, del
my_set.pop()
my_set.clear()
del my_set

#loop through a set
kernels = {"ubuntu", "kali", "fedora", "centOs"}

for g in kernels:
    print(g)

#join two sets using union and update()
kernels = {"ubuntu", "kali", "fedora", "centOs"}
others = set(("osX", "ibm"))

all_kernels = kernels.union(others)
print(all_kernels)

#keep the duplicate
kernels = {"ubuntu", "kali", "fedora", "centOs"}
others = set(("osX", "ibm", "kali"))

kernels.intersection_update(others)
print(kernels)
#or
all_kernels = kernels.intersection(others)
print(all_kernels)

#keep all but not the duplicate
kernels = {"ubuntu", "kali", "fedora", "centOs"}
others = set(("osX", "ibm", "kali"))

new_kernels = kernels.symmetric_difference(others)
print(new_kernels)

kernels.symmetric_difference_update(others)
print(kernels)

#dictionary
mydict = {
    "name": "kazim",
    "age": 10,
    "location": "abeokuta"
}
print(type(mydict))
print(len(mydict))

print(mydict["name"])
print(mydict["age"])
print(mydict["location"])


myfile = dict(
    name = "kazimee",
    age = 10,
    location = "Abeokuta",
    fav_food = ["amala", "eba", "rice"],
    is_kid = True
)
print(myfile)


myfamily = {
    "child" : {
        "name" : "john",
        "age" : 12
    },
    "child2" : {
        "name" : "akin",
        "age" : 10
    },
    "child3" : {
        "name" : "abiola",
        "age" : 8
    }
}
print(myfamily["child"]["age"])

#Python Conditions

num1 = 5
num2 = 10

if num1 < num1:
    print("num1 is less than num2")
elif num1 != num1:
    print("num1 equals num1")
elif num1 > num1:
    print("num1 is not greater than num1")
elif num1 > num2:
    print("num1 is not greater than num2")
else:
    print("num2 is greater than num1")

#short hand if/Ternary operators/Conditional Expressions
if num2 > num1: print("yes")

print("yes") if num2 > num1 else print("no")


num1 = 5
num2 = 10
num3 = 12

if num1 < num2 or num2 < num1:
    print("OK")

if not (num3 > num1):
    print("yes")

#nested dictionary
if num1 < num2:
    if num2 < num3:
        print("superb!")
    else:
        print("oh, no!")
else:
    print("OK")

#Python loops
#Example

ade_age = 7
biola_age = 18
yinka_age = 20
minimum_age = 18

'''
1. If you are less than 18, you are a child
2. If you are 18, you are an adult
3. If you are greater than 7 but less than 18, you are not an adult 
4. If you are greater than 7 and less than 20, you are both a teenager and an adult
'''

minimum_age = 18

age_range = int(input("enter age.."))
if age_range >= minimum_age:
    if age_range == minimum_age:
        print("you are an adult")
    elif age_range < minimum_age:
        print("you are not an adult")
    elif age_range < 20:
        print("you are both a teenager and an adult")
elif age_range > 7 and age_range < 18:
    print("you are not an adult")
else:
    print("you are a child")

nums = 0
nums -= 1
while nums < 11:
    nums += 1
    if nums == 5:
        continue
    print(nums)

names = ["joke", "hakim", "bose"]

for f in names:
    print(f)
else:
    print("the loop has ended")

names = ["joke", "hakim", "bose"]
age = [23, 25, 30]

for a in names:
    for b in age:
        print(a,b)


#Functions
#1
name = input("What is your name? ")
def myname(fname):
    print("Your name is " + fname)

myname(name)

#2
def myname(*names):
    print("My best friend is " + names[3])

myname("Biola", "Adewale", "John", "Ibrahim")

#3
def myname(name1, name2):
    print("My best friend is " + name1)

myname(name1="Bolaji", name2="John")

#4
def myname(**name):
    print("My best friend is " + name["name2"])

myname(name1 = "Akin", name2 = "Adesewa")

#5 default parameter value
def myname(name="Kazim"):
    print("My best friend is " + name)

myname("Akin")

#6 passing a list as an argument
def profile(candidates, pol_party):
    for i in range(len(aspirants)):
        print(aspirants[i], parties[i])

aspirants = ["Tinubu", "Atiku", "Obi", "Kwankwaso"]
parties = ["APC", "PDP", "ELUPEE", "NNPP"]

profile(aspirants, parties)

# OR 6 passing a list as an argument
def profile(candidates, pol_party):
    for n,m in zip(candidates, pol_party):
        print(n, ":", m)

aspirants = ["Tinubu", "Atiku", "Obi", "Kwankwaso"]
parties = ["APC", "PDP", "ELUPEE", "NNPP"]

profile(aspirants, parties)

#7 return values
def add(a,b):
    return a + b

print(add(3,5))

#8 recursion
def myrecursion(k):
    if k>0:
        result = k + myrecursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("my recursions......")

myrecursion(6)

#9
def add(a,b, *args):
    return a + b

print(add(2,4,3,5))


#Lambda/anonymous function
x = lambda a : a + 10
print(x(5))

#2
number = int(input("Enter a number for me to triple..."))
x = lambda n : n * 3
print(x(number))

#3
x = lambda n,m : n + m
print(x(2,3))

#4
def myfunc(a):
    return lambda n : n * a

mydoubler = myfunc(2)
mytripler = myfunc(3)
quadrupler = myfunc(4)

print("mydoubler: ",mydoubler(2), "\n","mytripler: ",mytripler(2), "\n", "quadrupler: ", quadrupler(2))

#Python Classes/Objects
#1
class myclass:
    x = 5
    y = 3

obj1 = myclass()
obj2 = myclass()

print(obj1.x)
print(obj2.y)

#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Person("Kazim", 20)
print(obj1.name)

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

obj1 = Person("Kazim", 20)
print(obj1)

#4
word = input("Enter a name..." )
num = int(input("Enter your age.."))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_name(self):
        print("my name is " + self.name + "and I am " + str(self.age) + "years old")

#obj1 = Person("Kazim", 20)

obj2 = Person(word, num)
print(obj2.my_name())

#5
word = input("Enter a name..." )
num = int(input("Enter your age.."))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_name(self):
        print("my name is " + self.name + " and I am " + str(self.age) + "years old")

obj1 = Person(word, num)
obj1.age = 30
obj1.name = "Tola"
del obj1.age
del obj1

print(obj1.my_name())
print("No! That is not my age")

#
class full_name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def myname(self):
        print("My full name is", self.fname, self.lname)

obj1 = full_name("Ayo", "Badmus")

(obj1.myname())

class newClass(full_name):
    pass

obj2 = newClass("Tolu", "Odebiyi")
obj2.myname()

#
#python inheritance

class full_name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def myname(self):
        print("My full name is", self.fname, self.lname)

obj1 = full_name("Ayo", "Badmus")

obj1.myname()

class newClass(full_name):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def my_bio(self):
        print("I am ", self.fname, self.lname, "and my age is ", self.age)
obj2 = newClass("Tolu", "Odebiyi",62)
obj2.my_bio()


#python iterator
#1
my_os =["kali", "centOS", "ubuntu", "fedora", "kubuntu"]

myiter = iter(my_os)

print(next(myiter))
print(next(myiter))

#2

class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
           x = self.a
           self.a +=1
           return x
        else:
            raise StopIteration

mynums = mynumbers()
myiter = iter(mynums)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#python scope
#1
a = 6
def my_scope():
    a = 5
    print(a)

my_scope()
print(a)

#2

x = 300

def myfunc():
    global x
    x = 200
    def innerf():
        print(x)
    innerf()

myfunc()
print(x)

#3

x = int(input("Enter amount of card to buy..."))

def myfunc():
    global x
    x += x
    print("congrats!! You've received " + str(x) + " recharge")

myfunc()

#python modules
import MyModule as mm
#import from MyModule *


print(mm.add(5,7,9,11,2,1,1))
print(mm.students["class"])

r = dir(mm)
print(r)


#Pythhon datetime
import datetime

x = datetime.datetime.now()
print(x.hour)

#alarm
y = datetime.datetime(2023, 4, 18, 11)

if (x.hour == y.hour):
    pass
print(y)
print(y.strftime("%y"))


#Python math

r = min(2, 7, 4, 56, 1)
q = max(45, 67, 50, 10)
t = abs(-5)
a = pow(2,5)
print(a)

import math as m

a = m.pi
print(a)


#Python JSON
import json

x = '{"name":"John", "age":30, "city":"Abeokuta"}'
print(x)
#print(type(x))

y = json.loads(x)
y = json.dumps(x)
print(type(y))
print(y["name"])


#Python JSON
#To open json file
f = open("json.txt")
print(f.read())

#or
with open("json.txt", "w") as f:
    #print(f.read())
    f.write("This is our json")
    f.close()
#2
import json
with open("json.txt", "r") as f:
    t = json.load(f)
    print(t)
    f.close()

#3
x = '{"name":"John", "age":30, "city":"Abeokuta"}'
#print(x)
print(type(x))

y = json.loads(x)
y = json.dumps(x, indent = 4, separators = (" : ", " = "))
print(type(y))
#print(y["name"])


#Python RegEx
#1
text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
print(x)

#2
user = input("Where are you based?...")
x = re.findall("abeokuta\Z", user.lower())
if x:
    print("Yes")
else:
    print("Sorry")

#3
enter_text = input("Type a sentence.....")
x = re.split("\s", enter_text)

print("You have typed " + str(len(x)) + " words")

#4
text = "The rain in Spain and the spain is rain"
x = re.sub("rain", "pain", text,1)
print(x)

#Python PIP
import camelcase

c = camelcase.CamelCase()

txt = "hello world"
print(c.hump(txt))

#Python Try Except
try:
    print(z)
except NameError:
    print("that variable doesnt exist man!")
else:
    print(z)
finally:
    print('code has been executed')


#Python String formatting

cost = 50_000
course = ["python", "cpp", "java"]

print(course[0] + " cost " + str(cost))

cost = 50_000
course = ["python", "cpp", "java"]

print(course[0] + " cost " + str(cost))

#or
cost = [50_000, 100_000, 150_000]
course = ["python", "cpp", "java"]

txt = "{} cost {}"
print(txt.format(course[1], cost[1]))

#or
cost = [50_000, 100_000, 150_000]
course = ["python", "cpp", "java"]

txt = "{} cost {}"
print(txt.format(course[1], cost[1]))

