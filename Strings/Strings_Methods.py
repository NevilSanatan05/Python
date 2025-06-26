# Strings are immutable -> Content cannot be change but it can be reassigned

name = "Nevil"
name = "python is a good Programming Language and it's syntax is easy to understand"
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())

print(name.strip())
print(name.lstrip())
print(name.rstrip())

print(name.find("it's"))
print(name.replace("easy","difficult"))

te = "My123"
print(te.isalpha())
print(te.isalnum())
print(te.isdigit())
print(te.isspace())

fruits = "Apple,Bananas,Mango"
print(fruits.split(","))
print(",".join(['Apple,Bananas,Mango']))