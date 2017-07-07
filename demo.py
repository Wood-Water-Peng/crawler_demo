import datetime
# Using function
import random
import re

import requests
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# value = {"username": "jackypeng", "password": "123"}
# headers = {'User-Agent': user_agent}
# data = urllib.urlencode(value)
# request = urllib2.Request("http://www.baidu.com", data, headers)
# response = urllib2.urlopen(request)
# print response.read()
from BeautifulSoup import BeautifulSoup

# cookie = cookielib.MozillaCookieJar()
#
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
#
# response = opener.open("http://www.baidu.com")
#
# print response.read()
# for item in cookie:
#     print 'Name=' + item.name
#     print 'Value=' + item.value
# url = "http://www.pythonscraping.com/pages/page3.html"
# url = "http://www.qmtjr.com"
# file = open('page3.html', 'w')
# file.write(str(soup))
# file.close()
# print soup.prettify()
# soup.__str__('gb18030')
# namelist = soup.findAll('div', {"id": "header"})
# namelist = soup.findAll(id='header')
# print namelist
# print (soup)
# print soup.find("table", {"id": "giftList"}).children
# for child in :
#     if child is None:
#         print 'Child is not found'
#     else:
#         print child
# rex = "\.\.\/img\/gifts\/img[\d]*\.jpg"
# pattern = re.compile(rex)
# images = soup.findAll('img', {"src": pattern})
#
# for image in images:
#     print image

random.seed(datetime.datetime.now())
pages = set()


def getLinks(articleUrl):
    response = requests.get("https://en.wikipedia.org" + articleUrl)
    html = response.text
    if html is None:
        print 'URL is not found'
    else:
        soup = BeautifulSoup(html)

    try:
        print soup.h1.text
        # print soup.find(id="mw-content-text").findAll("p")[0]
    except AttributeError:
        print "Page is lack of some attributes!"

    links = soup.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

    for link in links:
        print link
        print link.attrs
        attr = link.attrs[0]
        if 'href' in attr:
            if attr[1] not in pages:
                newPage = attr[1]
                print "----------\n" + newPage
                pages.add(newPage)
                getLinks(newPage)


url = "/wiki/Kevin_Bacon"
links = getLinks(url)

# while len(links) > 0:
#     index = (random.randint(0, len(links) - 1))
#     newArticle = links[index].attrs[0][1]
#     if newArticle not in pages:
#         print newArticle
#         pages.add(newArticle)
#         links = getLinks(newArticle)
#         print len(links)




