def sum(a,b):
  return a+b
print(sum(3,4))

'''
Types of functions scopes :- 
-  Local Varibale 
-  Global Variable
'''
 

x = 10 # Global Variable
def my():
  x = 2 #Local Variable
  return x
print(my())
print(x)