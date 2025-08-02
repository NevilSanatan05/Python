#For Loop

''' for i in range(0,11):
  print(i)


fruits = ["Apple","Banana","Cherry"]
for fruit in fruits:
  print(fruit) '''

#While Loop
'''count = 1

while(count<=5):
  print("Count:",count)
  count+=1'''

#Break 
for i in range(0,11):
  if i==5:
    break
  print(i)

count = 1
while(count < 11):
  if count == 5:
    count+=1
    continue
  print(count)
  count+=1