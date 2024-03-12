##ASSIGNMENT 1 (Monday 13/2/23)
import random
first_die = random.randrange(1,7)
second_die = random.randrange(1,7)

print(first_die, "," ,second_die)
if first_die == 6 and second_die == 6:
    print("You won!!!")
else:
    print("You lose! Try again...")


desc = "I am from Nigeria though I was born in the north pole"
word_search = input("Enter word to search - ")

if word_search in desc:
    print("Yes it is")
else:
    print("No it isn't")

#ASSIGNMENT 2 (Wednesday 15/02/2023)
#irrespective of how Nigeria is written let it be a valid answer#
#Hint use slice, upper/lower, concatetion, replace
desc = "I am from Nigeria though I was born in the north pole"
word_search = input("Enter word to search - ")

if word_search.lower() in desc.lower():
        print("Yes, it is")
else:
        print("No, it is not")
#word_search.lower() or upper() or casfold() will still work


#Assignment (ii) use capitalize, count, endswith, isalnum in an example
#Capitalize
string = "mosunmola is a good girl"
print(string.capitalize())

#count
items = ["red", "blue", "green", "red", "yellow", "red"]
count_red = items.count("red")
print(f"{count_red=}")

#endswith
string = "Mosunmola is a good girl"
right_word = "girl"
wrong_word = "Girl!"
print(string.endswith(right_word))

#isalnum
string = "Nigeria is the giant of Africa"
print(string.isalnum())

string1 = "08012345678"
print(string1.isalnum())

string2 = "omituntun2023"
print(string2.isalnum())

#Assignment 3 Monday 20/02/2023
#1
t = 9
s = 3
print(t>>s)

#2
first_number = int(input("Enter a number..."))
second_number = int(input("Enter another number..."))
if first_number < 10 and second_number < 10:
    print(first_number + second_number)

if first_number > 10 and second_number > 10:
    print(first_number - second_number)
#OR
num1 = int(input("===="))
num2 = int(input("===="))

if num1 < 10 and num2 < 10:
    print(num1 + num2)
else:
    if num1 > 10 and num2 > 10:
        print(num1 - num2)
#elif could also be used


#Assignment 4.... using user input, check if a fruit is in the list, irrespective of the capitalization of the fruit

myfruits = list(("apple", "orange", "banana", "pawpaw", "cashew", "mango", "cherry"))
fruitsearch = input("Name fruit...")
if any(fruitsearch.upper() == fruits.upper() for fruits in myfruits):
    print("yes, it is")
else:
    print("No, it is not")


#Assignment 5

#Assignment 6 Friday/3rd,March,2023
#i
nums = [25, 57, 13, 8, 49, 19]
sorted_nums = sorted(nums)
lowest_position = nums.index(sorted_nums[0])
highest_position = nums.index(sorted_nums[-1])

print(f"lowest number is at position {lowest_position}")
print(f"highest number is at position {highest_position}")

#or- unsorted
nums = [25, 57, 13, 8, 49, 19]
print(min(nums))
print(max(nums))
print(nums.index(min(nums)))
print(nums.index(max(nums)))

#or- sorted
nums = [25, 57, 13, 8, 49, 19]
sorted_nums = sorted(nums)
print(min(sorted_nums))
print(max(sorted_nums))
print(sorted_nums.index(min(nums)))
print(sorted_nums.index(max(nums)))

#ii
#a
list_1 = [n for n in range(2, 11, 2)]
list_2 = [n for n in range(1, 10, 2)]
print(list_1)
print(list_2)
#print(list(range(2, 11, 2))), print(list(range(1, 10, 2)))
for i in range(len(list_1)):
    print(list_1[i] + list_2[i])
#b
list_3 = list_1 + list_2
greater_than_5 = [n for n in list_3 if n > 5]
print(greater_than_5)

#iii
fruits = ["apple", "orange", "banana", "pawpaw", "cashew", "mango", "apple"]
y = fruits.count("apple")
print(y)

nums = [25, 57, 13, 8, 49, 19]
x = nums.index(19)
print(x)

#Assignment 7, Monday,6th March, 2023
#remove a country irrespective of the case of the country, using a minimum number of codes

countries = ("Nigeria", "Spain", "Ukraine")
country_to_remove = "spain"
countries = tuple(c for c in countries if c.lower() != country_to_remove.lower())
print(countries)

#or
countries = ("Nigeria", "Spain", "Ukraine")
country_to_remove = "spain"
new_c = list()

for c in countries:
    if c.lower() != country_to_remove.lower():
        new_c.append(c)
print(tuple(new_c))


#Assignment 7 Friday 10th March, 2023
#findouthowmanytimes javascript occurintuplevariable all_lang and return theindexesusingthemthdcountandindexwhereappropriate
#Find a practical scenario of where it is best to use a tuple and a list

languages = ("python", "PHP", "java", "cpp", "ruby", "c")
languages2 = ("javascript", "kotlin", "javascript")

all_lang = (languages + languages2)
print(all_lang)

#1
count = all_lang.count("javascript")
print(count)

#2
repeated_item = "javascript"
indices = [i for i in range(len(all_lang)) if all_lang[i] == repeated_item]
print(indices)
#or
index = []
for i in range(len(all_lang)):
    if all_lang[i] == repeated_item:
        index.append(i)
print(index)


#Assignment 8


kernels = {"ubuntu", "kali", "fedora", "centOs", True}
others = set(("osX", "ibm", "kali", 1))
for x in kernels:
    others.add(x)
print(others)

set = {1,2,3,4,5}
print(set.isdisjoint({6,7,8}))
print({1,2}.issubset(set))
print(set.issuperset({1,2}))


#Assignment 9
#1
myfile = dict(
    name = "kazimee",
    age = 10,
    location = "Abeokuta",
    fav_food = ["amala", "eba", "rice"],
    is_kid = True
)
if "rice" in myfile["fav_food"]:
    print("My name is {name}, my favorite food is rice.".format(
        name=myfile["name"], fav_food=myfile["fav_food"]))

#2
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

for member in myfamily.values():
    if isinstance(member, dict):
        print(member["name"])
    elif isinstance(member, list):
        for child in member:
            print(child["name"])


#Assignment 10
#1
nums = [23, 12, 4, 13, 91, 45, 8]
#i reps the index, j reps highest number
i = 0
j = 1

while i < len(nums):
    if nums[i] > j:
        j = nums[i]
    i +=1

print("The highest number in the is:", j)

#2
names = ["joke", "hakim", "bose"]
age = [23, 25, 30]

for i in range(len(names)):
    print(names[i], age[i])

#print the position of the highest number
nums = [23, 12, 4, 13, 91, 45, 8]

i = 0

mid = len(nums)//2
while i< len(nums) and mid<len(nums):
    if nums[mid]>nums[i]:
        mid = mid
    elif nums[mid]< nums[i]:
        mid = i
    i +=1
print(mid)

#Assignment 11,make it return without error

def add(*b):
    return sum(b)

print(add(2,4,3,5))