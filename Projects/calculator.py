def add(num1,num2):
  return num1+num2
def subtract(num1,num2):
  return num1-num2
def multiply(num1,num2):
  return num1*num2
def divide(num1,num2):
  if num2==0:
    return "Error! Division by zero."
  return num1/num2
while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  choice = input("Enter choice (1/2/3/4/5): ")
  if choice == '5':
    print("Exiting the calculator. Goodbye!")
    break
  
  num1 = float(input("Enter first number:"))
  num2 = float(input("Enter second number: "))

  if choice == '1':
    print(f"{num1}+{num2} = {add(num1+num2)}")
  elif choice == '2':
    print(f"{num1}-{num2} = {subtract(num1, num2)}")
  elif choice == '3':
    print(f"{num1}*{num2} = {multiply(num1, num2)}")
  elif choice == '4':
    print(f"{num1}/{num2} = {divide(num1, num2)}")
  else:
    print("Invalid input. Please enter a valid choice (1-5).")