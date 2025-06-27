z=12
def sum(a,b):
  print("Global Changing Scopes")
  c=a+b
  global z # Please modify global z
  z=10 # This will refer to a global z and not create a local variable
  return c
z=20
print(sum(3,4))
print(z)