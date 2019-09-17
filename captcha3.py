import requests
import webbrowser
from selenium import webdriver

url = "http://192.168.60.134/captcha/example3/"
r = requests.get(url)
c = r.cookies # get the cookie 
v = c.items()

for value in v:
   s = str(value)
   string = s[13:-2]
print string

url = url + "submit?captcha="+string+"&submit=Submit+Query" #Answer that the webpage sends to the server to validate.
r = requests.get(url,cookies=c) # send the request with the cookie set to the server
print r
