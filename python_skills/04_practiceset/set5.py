'''5. Modules and Pip – Using External Libraries
Import the math module and use it to:
Find the square root of 144
Calculate sin(90°) (hint: use math.radians() )
Install and import the requests module (if available) and use it to fetch data
from "https://api.github.com"'''

import math as m
import requests as req
x = m.sqrt(144)
print(x)

angle_in_radians= m.radians(90)
result = m.sin(angle_in_radians)
print(result)
web_result = req.get("https://api.github.com")
print(web_result.text)

