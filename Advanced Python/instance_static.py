class Employee:
  company="HP"
  def __init__(self,name,salary):
    self.name = name
    self.salary=salary
  def print_info(self):
    return f"The name is {self.name} and the salary is {self.salary}"
  
  @staticmethod
  def sum(a,b):
    return a+b
  
e1 = Employee("Nevil",300000)
e2 = Employee("raj",300000)
# print(Employee.company)
print(Employee.print_info(e1))

print(e2.sum(4,5))
