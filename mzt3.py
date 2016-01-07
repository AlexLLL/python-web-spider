from bs4 import BeautifulSoup
import urllib
import requests
import os

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0
c = '.jpeg'
PWD="/home/lyx/pic"

pageUrl = 'http://www.meizitu.com/a/1.html'
htmlDoc = requests.session().get(pageUrl,headers=head,timeout=TimeOut)
soup = BeautifulSoup(htmlDoc)
#print (soup.prettify())
#print ("now downloading(%d)"%(i))
divHtml = soup.find_all("img",'class="scrollLoading"')
imgUrl = 'http://mm.howkuai.com' + divHtml[0].img.attrs['src']
data = urllib.requests.urlopen(imgUrl).read()
fileName = soup.title.contents[22] + '.jpg'
filePath = os.path.join('/home/lyx/pic',fileName)
image = open(filePath,'wb')
image.write(data)
image.close()
