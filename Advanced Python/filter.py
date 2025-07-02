def is_greater_than_9(x):
  if x>9:
    return True
  else:
    return False
a=[1,3,4,234,34,32,9,8]
new = list(filter(is_greater_than_9,a))
print(new)