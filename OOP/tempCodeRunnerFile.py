class Student:
  def __init__(self,name,section,division):
    self.name = name
    self.section = section
    self.division = division

def display_details(self):
  print(f"Name : {self.name}, Section: {self.section}, Division: {self.division}")


student1 = Student("John", "A", "Science")  
student1.display_details()