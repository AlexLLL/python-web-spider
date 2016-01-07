#coding:utf-8
from bs4 import BeautifulSoup
import requests
import urllib
import re
import os

DownPath = "/home/lyx/pic"
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0
c = '.jpeg'
PWD="/home/lyx/pic"

for x in range(1,2):
  site = "http://www.meizitu.com/a/%d.html" %x
  Page = requests.session().get(site,headers=head,timeout=TimeOut)
  Coding =  (Page.encoding)
  Content = Page.content#.decode(Coding).encode('utf-8')
  ContentSoup = BeautifulSoup(Content, "html5lib")
  jpg = ContentSoup.find_all('img',{'class':'scrollLoading'})
  #print jpg
  imgUrl = 'http://mm.howkuai.com' + jpg[0]['src'][22:]
  print imgUrl
  data = urllib.urlopen(imgUrl).read()
  path = '/home/lyx/pic/'+ ContentSoup.title.contents[0]
  print path
  os.mkdir(path)
  picName = jpg[0]['src'][42:47]+'-'+jpg[0]['src'][49:50]+'-'+jpg[0]['src'][52:53]+'-'+jpg[0]['src'][55:56]+ '.jpg'
  print picName
  filePath = os.path.join(path,picName)
  print filePath
  image = open(filePath,'wb')
  image.write(data)
  image.close()
