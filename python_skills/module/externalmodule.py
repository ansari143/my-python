import requests as rs
import pandas as pd

#y= pd.read_csv("hello")

x = rs.get("https://google.com")

print(x.status_code)