# Append to a file called "raj.txt"
# It should contain the data about raj
try:
  f= open("r.txt", "a")
  string = '''Raj is a software engineer.
  He works at a tech company and enjoys coding in Python.
  He is passionate about software development and loves to learn new technologies.'''
  f.write(string)
  f.close()
except FileNotFoundError:
  print("File not found. Please create the file first.")