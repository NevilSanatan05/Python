#Dictionaries are mutable
student = {"name":"Raj","age":23}
print(student["name"])
print(student.keys())
print(student.values())
print(student.items())
# print(student.clear())

table = { i: 5*i for i in range(1,11)}
print(table)