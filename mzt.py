#coding:utf-8
from bs4 import BeautifulSoup
import requests
import urllib
import re
import os

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5

for x in range(1,11):     #using range  traversie all sites  from 1 to x-1
    site = "http://www.meizitu.com/a/%d.html" %x    #%d represent 'number' in the original site
    Page = requests.session().get(site,headers=head,timeout=TimeOut)
    Coding =  (Page.encoding)
    Content = Page.content
    ContentSoup = BeautifulSoup(Content, "html5lib")
    jpglist = ContentSoup.find_all('img',{'class':'scrollLoading'})
    #print jpglist 
    path = '/home/lyx/pic/'+ ContentSoup.title.contents[0]
    print '[Now downloading to]: '+path
    os.mkdir(path)
    #mkdir for each site
    for jpg in jpglist:
        imgUrl = 'http://mm.howkuai.com' + jpg['src'][22:]
        #print imgUrl
        data = urllib.urlopen(imgUrl).read()
        picName = jpg['src'][42:47]+'-'+jpg['src'][48:50]+'-'+jpg['src'][51:53]+'-'+jpg['src'][54:56]+'.jpg'
        #print picName
        filePath = os.path.join(path,picName)
        #print filePath
        image = open(filePath,'wb')
        image.write(data)
        image.close()
        #iwrite pic data to file
