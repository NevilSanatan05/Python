# while True:
#     try:
#       a = int(input("enter a number 1: "))
#       b = int(input("enter a number 2: "))
#       print(f"The sum is {a/b}")
#     except ValueError:
#        print("Please dont perform bad typecasts")
#     except ZeroDivisionError:
#        print("Hey dont divide by 0")
#     except Exception as e:
#        print("Some error occured",e)

while True:
  a = int(input("enter a number 1: "))
  b = int(input("enter a number 2: "))
  if b==0:
   raise ValueError("Please dont divide by 0")
  print(f"The division is {a/b}")