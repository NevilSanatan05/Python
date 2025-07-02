def mark(**kwargs):
  for item in kwargs.keys():
    print(f"the marks of {item} are {kwargs[item]}")

mark(shubham=34,vikrant=67,jack=90)