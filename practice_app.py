name = "Finlay"

print (f"Hello {name}")

#STRINGS

string1 = "   hello WORLD  "

string1.strip() #removes surrounding whitespace

string1.lower() #lowercase

string1.upper() #uppercase

string1.replace("hello", "hi") #replaces text

letters = "a,b,c"
letters.split(",") #splits a string

letters = ["a", "b", "c"]
joined = ", ".join(letters) #join strings together

word = "Finlay"
word[0] #F
word[1] #i
word[-1] #y
word[0:3] #Fin

#Strings don't change themselves, you always need a new string (eg string2 = string1.upper())
#Strings are immutable

#LISTS

#used for an ordered collection of things

names = ["Fin", "Bob", "Tim"]

names[0] #Fin

for name in names:
    print(name) #looping through names

names.append("Joe") #add something

names.remove("Bob") #remove something

name = names.pop() #remove and return an item

if "Fin" in names:
    print("Name found") #check membership

len(names) #length of a list

#lists are mutable, which means names.append() actually changes the list

#DICTIONARIES

#stores key-value pairs

person {
    "name": "Finlay",
    "country": "England",
    "age": 19
}

person["name"] #Finlay, use a key

person["age"] = 20 #Change a value

person["surname"] = "Major" #add something

del person["country"] #remove something

if "name" in person: 
    print(person[name]) #check whether a key exists

#useful methods
person.keys()
person.values()
person.items()
person.get("name")

for key, value in names.items():
    print(key, value) #items uses both key and value

#.get() is very useful
#name["height"] causes a key error if it doesn't exist
#name.get("height") returns none
#you can provide a fallback names.get("height", "Unknown")

#CHOOSING THE RIGHT DATA STRUCTURE

#if you want to store 3 of the same things (eg names), a list makes sense because it is multiple of the same items
#if it is information about one person, then a dictionary makes sense because each value has a meaning identified by a key
#if you need several people, then it would be a list of dictionaries

#NESTED DATA

courses = [
    {
        "name": "Python",
        "completed": True
        "topics": ["lists", "dictionaries", "functions"]
    }
    {
        "name": "Git",
        "completed": True,
        "topics": ["GitHub", "commits", "staging"]
    }
]

#if we wanted to get dictionaries:
courses[0] #first course
courses[0][topics] #its topics
courses[0][topics][1] #gives dictionaries

#FUNCTIONS

#bad example
def process_student(student):
    name = student["name"]
    print(name.upper())
#this function is doing multiple jobs, transforming and displaying a name

#better
def format_name(name):
    return name.strip.title()

student_name = format_name("   fin major   ")
print(student_name)
#small functions should have a clear purpose

#FUNCTIONS AS ARGUEMENTS

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply_operation(number, operation):
    return operation(number)

result = apply_operation(5, double)
print(result)

print(apply_operation(5, triple))

#FILTER AND MAPPING

numbers = [1, 2, 3, 4]

def double(number):
    return number * 2

#instead of manually creating a loop to double, you can do

doubled = list(map(double, numbers))

#map means apply this function to every item

#now using filter

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, numbers))

#LIST COMPREHENSIONS

#normal loop

doubled = []

for number in numbers:
    doubled.append(number * 2)

#list comprehension

doubled = [number * 2 for number in numbers]

#add filtering
even numbers = [number for number in numbers if number % 2 == 0]

#DICTIONARY COMPREHENSIONS

numbers = [1, 2, 3, 4]

squares = {number: number * number for number in numbers}

#REFACTORING

#means improving the sturcutre of code without changing what it does

name = input("Name: ")

name = name.strip()
name = name.lower()
name = name.title()

print(name)

#this code works, but is poor

def clean_name(name):
    return name.strip().lower().title()

name = input("Name: ")
print(clean_name(name))

#example 2

if user["age"] >= 18:
    print(f"{user["name"]} is above the age of 18")

#instead of this being repeated all over the page:

def is_adult(user):
    return user["age"] > 18

#then if is_adult(user): ...

#CLASSES

#imagine we have a dictionary

user = {
    "name": "Fin",
    "age": 19
}

#you may also have

def introduce(user):
    print(f"Hello, my name is {user[name]}")

#in classes, related data and behaviour may belong together

#if we had a class called Dog, this describes what dogs in the program have and can do

#there may be individual dog names, the class is the definition, the object or instance is one actual thing created from it

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#then to create an object

fin = User("Fin", 19)

#fin is an instance of user
#you can then access

print(fin.name)
print(fin.age)

#what is __init__

#python creates a new user when User("Fin", 19) is wrote
#__init__ is used to initialize its starting infromation
#name and age come in as arguements
#self.name and self.age become information stored on that particular object

#what is self

#there may be 2 different calls of the class
fin = User("Fin", 19)
alex = User("Alex", 29)
#when code runs on fin, self refers to fin, same with alex it refers to alex
#self.name means the name belonging to this particular User object

#METHODS IN CLASSES

#now behaviour can be added

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name}"

fin = User("Fin", 19)
print (fin.introduce())

#WHY USE A CLASS

#class becomes useful when there is a meningful cocnept that contains both state/data and behaviour connected to that state

class Bank_Account():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = Bank_Account(100)
account.deposit(50)
account.withdraw(100)

#FILES



