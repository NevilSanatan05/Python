'''
Two Types in modules in Python :
--  Built in Modules 
--  External Modules

'''

import math
import os
import mymodules
import requests

print(math.sqrt(4))
print(math.pow(2,3))
print(mymodules.hello("Nevil"))
r = requests.get("https://www.google.com")
print(r.text)