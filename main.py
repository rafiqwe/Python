# name = "Muhammad Rabbi";
# age = 17;

# print("Hello, " + name + "!")
# print("Your age is", age, "year old")
# a = 5
# b=10
# print(a * b)

# input in python 
# input("Enter your name: ")

# a = input("enter the frist number:")
# b = input("enter the last number: ")
# sum = a + b
# print("The sum of 2 number:", sum)


## ------ String ----- ##

# string = "This is a \n string example"
# string1 = """This is a string example 2 """
# string2 = 'This is a string example 1'
# str = "I am studying python "

# print(string);
# print(string1 + string2) 
# print(string[1].upper()) 

# ## ---- Slicing ----- ##

# print(string1[4:]) # the output is "is string example 2"
# print(string1[0:4]) # the output is "This"

# print(string.endswith("ple")) # returns true id string ends with substr
# print(string.capitalize()) # capitalizes 1st char

# print(str.replace('python', 'javascript')) # replaces all occurrences of old
# print(str.find('am')) # return 1st index of 1st occurrer
# print(str.count('am')) # counts the occurrence of substr
# print(str.split())


# ----- Practices 1 ---- #
# name = input('Enter your name: ')
# name = "this is a name "
# print("Length of name =", len(name))

# ----- Practices 1 ---- #
# practice2 = "This is a $ symbol $ $"
# print(practice2.count('$'))

# ---- Conditionals in Python ---- #

light = "green"

if(light == "red") : 
    print("Stop") # indentation
elif(light == "yellow"):
    print('Wating')
elif(light == "green") : 
    print("Go")
else :
    print("Light is broken")

# ---- Practices 1 ---- #
# Grade students based on marks
# I try to write the code 
marks = 96

if(marks <= 70): 
    print("Your grade is 'D' ")
elif(marks <= 80):
    print("Your grade is 'C' ")
elif(marks <= 90):
    print("Your grade is 'B' ")
elif(marks <= 100):
    print("Your grade is 'A' ")

# the code writen by apna collage 
marks2 = 80

if(marks2 >= 90): 
    grade = "A"
elif(marks2 >= 80 and marks2 < 90): 
    grade = "B"
elif(marks2 >= 70 and marks2 < 80): 
    grade = "C"
else:
    grade = "D"

print("The student grade is:", grade)

# ---- nesting in python ---- #

age = 81

if(age >= 18):
    if(age >= 80):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("children can't drive car")

## ---- practices 2 ---- ##
# Check if a number entered by the user is odd or even
num = 6

if(num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")


## ---- practices 2 ---- ##
# Find the greatest of 3 number entered by the user

a= 27
b= 29
c=10

if(a >= b and a > c):
    print("The greatest number is: a", a)
elif(b >= c) :
    print("The greatest number is: b", b)
else:
    print("The greatest number is: c",c)

## ---- practices 3 ---- ##
# Check if a number is a multiple of 7 or not

number = 14

if(number % 7 == 0):
    print("The number is multiple of 7", number)
else:
    print('The number id not multiple of 7', number)