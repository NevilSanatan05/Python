# name = "Nevil"
# print(type(name))
# game = ''' i a kf jaf'''
# print(game)

# name = "Nevil Sanatan Barick"
# print(name[2:-1])
# print(name[0::2])

#strings are immutable
# name = "Nevil"
# print(name)

# a=len(name)
# print(a)

# name = "Nevil"
# print(name.lower())
# print(name.upper())
# print(name.replace("N","A"))
# print(name.count("a"))
# print(name.index("v"))
# print(name.find("vi"))
# print(name.isalnum())
# print(name.title())

# fruits = "Mango, Banana, Apple"
# print(fruits.split(","))


# a="John"
# a1=10000
# template = f"Dear {a}, your balance is {a1}."
# print(template)

#Q1
# name = "Nevil Sanatan Barick"
# print(name[0])
# print(name[-1])
# print(len(name))

#Q2
# str1 = "Hello"
# str2 = "World"
# print(str1+" "+str2)

#Q3
# text = "Python Programming"
# print(text[0:5])
# print(text[-6:])

#Q4 
# string = " i love python programming "
# print(string.strip())
# print(string.title())
# print(string.count("o"))

#Q5
# str = "123abc"
# print(str.isalnum())

#Q6
# name = "John"
# age = 25
# print(f"My name is {name} and I am {age} years old .")

#Q7
# sentence = "Coding in Python is fun"
# print(sentence.replace("fun","awesome"))
# print(sentence.index("Python"))
# print(sentence.upper())

#Q8
# sentence = "Coding in Python is fun"
# sum = 0
# vowels = ["a","e","i","o","u","A","E","I","O","U"]
# for har in sentence:
#     if har in vowels:
#         sum+=1
# print("Number of vowels in the sentence is : ",sum)


#Q9
str1="madam"
if(str1==str1[::-1]):
  print("Palindrome")
else:
  print("Not a Palindrome")

