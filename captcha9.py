import cookielib, urllib2, urllib
from bs4 import BeautifulSoup
import urllib
import requests
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r = opener.open("http://192.168.60.134/captcha/example9/")
soup = BeautifulSoup(r,"lxml")
print type(soup)
string = soup.find_all("form", limit=1)
string = str(string)
print string
num1= string[27:29]
num2= string[29:32]
op= string[26:31]

import re
num1= re.sub("[^0-9]", "",num1)
num1= int(num1)

num2= re.sub("[^0-9]", "",num2)
num2= int(num2)


from string import digits
op = op.translate(None, digits)
op= str (op)

result = 0

if op ==" +" or op=="+": result = num1 + num2 
elif op==" -" or op=="-": result =  num1-num2
elif op==" /" or op=="/": result =  num1/num2
elif op==" *" or op=="*": result =  num1*num2
print "Result = "+ str(result)
url = "http://192.168.60.134/captcha/example9/submit?captcha="+str(result)+"&submit=Submit+Query" #Answer that the webpage sends to the server to validate.
r1 = requests.get(url, cookies= cj) # send the request with the cookie set to the server
print r1


