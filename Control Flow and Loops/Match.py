age  = int(input("Enter your age : "))

match age:
  case _ if age>=18:
    print("You can Drive")
  case _:
    print("You can't Vote")