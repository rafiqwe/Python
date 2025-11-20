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

string = "This is a \n string example"
string1 = """This is a string example 2 """
string2 = 'This is a string example 1'
str = "I am studying python "

print(string);
print(string1 + string2)
print(string[1].upper()) 

## ---- Slicing ----- ##

print(string1[4:]) # the output is "is string example 2"
print(string1[0:4]) # the output is "This"

print(string.endswith("ple")) # returns true id string ends with substr
print(string.capitalize()) # capitalizes 1st char

print(str.replace('python', 'javascript')) # replaces all occurrences of old
print(str.find('am')) # return 1st index of 1st occurrer
print(str.count('am')) # counts the occurrence of substr
print(str.split())


# ----- Practices 1 ---- #
# name = input('Enter your name: ')
name = "this is a name "
print("Length of name =", len(name))

# ----- Practices 1 ---- #
practice2 = "This is a $ symbol $ $"
print(practice2.count('$'))

