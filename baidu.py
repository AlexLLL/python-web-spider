import urllib2  
response = urllib2.urlopen('http://www.meizitu.com/a/1.html')  
html = response.read()  
print html  
