# -----------------------------
# LIST
# -----------------------------
print("LIST EXAMPLE")
my_list = [10, 20, 30, 40]
print("List:", my_list)
print("First element:", my_list[0])
my_list.append(50)
print("After append:", my_list)

# -----------------------------
# TUPLE
# -----------------------------
print("\nTUPLE EXAMPLE")
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
print("Second element:", my_tuple[1])

# -----------------------------
# SET
# -----------------------------
print("\nSET EXAMPLE")
my_set = {1, 2, 3, 3, 4}
print("Set:", my_set)  # duplicates removed
my_set.add(5)
print("After add:", my_set)

# -----------------------------
# DICTIONARY
# -----------------------------
print("\nDICTIONARY EXAMPLE")
student = {
    "name": "Mariya",
    "age": 20,
    "course": "Python"
}
print("Student Name:", student["name"])
student["age"] = 21
print("Updated Dictionary:", student)

#Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # from index 1 to 3
print(numbers[:3])    # first 3 elements
print(numbers[2:])    # from index 2 to end
print(numbers[-3:])   # last 3 elements


#WHILE LOOP WITH IF ELSE
i = 1

while i <= 5:
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
    i = i + 1

#BREAK & CONTINUE
for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#for
# Prints a pattern using astrisk symbol

rows = int(input("Enter the rows  :"))    # e.g. 3
for i in range(0, rows+1):               # Outer loop will print number of rows   (+1 because range excludes the second number)
    for j in range(i):                   # Inner loop will print number of Astrisk  
        print("*", end='')               # print() can take different arguments, by default end='\n' i.e. new line
    print()                               # Once inner loop is finished, we want the control to come to the next line, hence blank print()
# -----------------------------
# IF / ELIF / ELSE
# -----------------------------
print("\nIF ELIF ELSE EXAMPLE")
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# -----------------------------
# FUNCTION
# -----------------------------
print("\nFUNCTION EXAMPLE")

def add(a, b):
    return a + b

result = add(5, 3)
print("Addition:", result)

# -----------------------------
# OOPS (CLASS & OBJECT)
# -----------------------------
print("\nOOPS EXAMPLE")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
p1 = Person("Mariya", 21)
p1.show_details()

#--- class 
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)


# Create object
s1 = Student("Mariya", 1)

# Call function
s1.show()


class Dog:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age} ")

dog1 = Dog('Husky', 5, 'Blank')

dog1.details()


# But if you import sqrt() specifically, then you can access it just like that. 
# e.g.

from math import sqrt       # use ctrl + tab to get suggestions after import
sqrt(4)                     # we can use sqrt() now because in the above line, we are explicitly importing sqrt() function
