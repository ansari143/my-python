import requests

getRequestvalue = requests.api.get("https://tcsglobal.udemy.com/course/codewithharry-python/learn/lecture/48757253#overview")
print(getRequestvalue.text)