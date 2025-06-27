class Employee:
  company = "Asus"
  
  def __init__(self,salary,name,bond,company):
    self.salary=salary
    self.name=name
    self.bond=bond
    self.company=company

  def get_salary(self):
    return self.salary
  def get_info(self):
    return(f"The name of the employee is {self.name}. Salary is {self.salary}")  
  
e1 = Employee(40000,"Hitesh",4,"Dell")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company)


#Object introspection
print(dir(e1))