#Lists are ordered and mutable
marks = [54,67,43,86,92]
print(marks[0:2]) #Slicing of Lists


extra_marks = [120,240]
#Lists methods

print(marks.append(100))
print(marks.pop())
print(marks.extend(extra_marks))
print(marks.insert(1,"Hello"))
print(marks.sort)
print(marks)


for i in range(1,11):
  print("5 X",i,"=",5*i)


#Create a list containing the table of 5 
a =5 
table =[]
for j in range(1,11):
  table.append(5*j)
print(table)


#Shortcut
tables =[6*k for k in range(1,11)]
print(tables)

square = [l**2 for l in range(5)]
print(square)