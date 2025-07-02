def repeat(n):
  def decoration(func):
    def wrapper(a):
      for i in range(n):
        func(a)
    return wrapper
  return decoration

@repeat(7)
def say_hello(a):
  print(f"Hello {a}")

say_hello("Harry")