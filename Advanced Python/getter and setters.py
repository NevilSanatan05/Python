class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, first):  # <-- Name must match the property
        parts = self.name.split(" ")
        if len(parts) > 1:
            self.name = f"{first} {' '.join(parts[1:])}"
        else:
            self.name = first

e = Employee("Jack Doe", 30000)

print(e.first_name)      # Output: Jack
e.first_name = "John"    # Updates first name
print(e.name)            # Output: John Doe
