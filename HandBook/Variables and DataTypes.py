user = str(input("Enter your name: "))
#print(f"Good Afternoon {user}")

Name = str(input("Enter your name: "))
Date = str(input("Enter today's date: "))
letter = (f"Dear {Name} You are selected! {Date}")
print(letter)

text = input("Enter a  text: ")
if "  " in text:
    print("The text contains spaces.")
else:
    print("The text does not contain spaces.")
