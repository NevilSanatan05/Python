# f = open("ra.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("raj.txt", "r") as f:
    content = f.read()
    print(content)
# The 'with' statement automatically closes the file after the block is executed.