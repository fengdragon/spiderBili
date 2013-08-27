import urllib2
from BeautifulSoup import BeautifulSoup

urlList = ['http://travel.fengniao.com/slide/334/3344576_%d.html' % i for i in range(1,40)]
imgurl = []

# open every url via urllib2, get the img tag via BeautifulSoup
for i in urlList:
    html = urllib2.urlopen(i)
    soup = BeautifulSoup(html)
    imgsResult = soup.findAll('img', id="mainPic")
    imgurl.append(imgsResult[0]['src'])
print imgurl
