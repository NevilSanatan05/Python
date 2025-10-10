#If statement
# a = int(input("Enter a number : "))
# if a>0:
#   print("The number is positive")

#If-Else statement
# age = int(input("Enter your age :"))
# if age>=18:
#   print("You are eligible to vote")
# else:
#   print("You are not eligible to vote")
# print("Thank you")

#Elif statement
# age = int(input("Enter your age :"))
# if age<18:
#   print("You are not eligible to vote")
# elif age==18:
#   print("You are eligible to vote for the first time")
# elif age>18 and age<60:
#   print("You are eligible to vote")
# else:
#   print("You are eligible to vote and also a senior citizen")
# print("Thank you")

# Match Case
# name = str(input("Enter your name : "))
# match name:
#   case "Nevil":
#     print("Hello Nevil")
#   case "Raj":
#     print("Hello Raj")
#   case "John":
#     print("Hello John")
#   case _:
#     print("Hello Guest")
# print("Thank you")

#For loop
# for i in range(1,11):
#   print(i)

# for i in range(1,10):
#   print(f"5X{i}={5*i}")

#while loop
# i = 10
# while i<=20:
#   print(i)
#   i=i+1

#Break statement
# for i in range(1,11):
#   if i==2:
#     break
#   print(i)

#Continue statement
# for i in range(1,11):
#   if i==2:
#     continue
#   print(i)

#Pass statement
# for i in range(1,11):
#   if i==2:
#     pass
#   print(i)


#Practice Set -2

#Q1
# num = int(input("Enter a number:"))
# if num>0 :
#   print("The number is positive")
# elif num==0:
#   print("Number is zero")
# else:
#   print("The number is negative")

#Q2
# age = int(input("Enter your age :"))
# if age>=18:
#   print("Person is elgible to vote")

#Q3
# num = int(input("Enter a number :"))
# if num%2==0:
#   print("Even number")
# else:
#   print("Odd number")

#Q4
# day = int(input("Enter day number :"))
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Invalid day number")

#Q5
# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# operation = input("Enter operation (+,-,*,/,//,%,**) :")

# match operation:
#   case '+':
#     print(num1+num2)
#   case '-':
#     print(num1-num2)
#   case '*':
#     print(num1*num2)
#   case '/':
#     print(num1/num2)
#   case '//':
#     print(num1//num2)
#   case '%':
#     print(num1%num2)
#   case '**':
#     print(num1**num2)
#   case _:
#     print("Invalid operation") 

#Q6
# for i in range(1,11):
#   print(i)

#Q7
# number = int(input("Enter a number :"))
# for i in range(1,11):
#   print(f"{number}X{i}={number*i}")

#Q8
# total = 0
# for i in range(1,101):
#   total=total+i
# print(total)

#Q9
# for i in range(1,5):
#   print("*"*i)

#Q10
# i=1
# while i<=10:
#   print(i)
#   i=i+1

#Q11
# password="nevil123"
# while True:
#   user_input=input("Enter the password :")
#   if user_input==password:
#     print("Password is correct")
#     break
#   else:
#     print("Incorrect password, try again")

#Q12
num = int(input("Enter a number :"))
reverse = 0
while num>0:
  digit = num%10
  reverse = reverse*10 + digit
  num = num//10
print("The reverse is :",reverse)