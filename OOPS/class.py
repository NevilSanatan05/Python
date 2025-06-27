# Class is a blueprint or a teamplate . ex:- Form 

#Object is a specific instance created from the template (class..) . ex:- Form which contain the data for John and .....



class Employee:
  company = "HP"

  def get_salary(self): #self is imp here because self is a way to reference the object of the class which is being created
    
    return 34000

e = Employee() #An object of class Emplyee is created here
print(e.get_salary())
print(e.company)


e2 = Employee()
print(e2.get_salary())
print(e2.company)