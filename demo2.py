import re
import urlparse

import requests
# Get all the internal links of the page
from BeautifulSoup import BeautifulSoup


def getInternalLinks(soup, includeUrl):
    internalLinks = []
    # Find all the links starting with '/'
    includeUrl = urlparse.urlparse(includeUrl).scheme + "://" + urlparse.urlparse(includeUrl).netloc
    print includeUrl

    for link in soup.findAll("a", href=re.compile("^(/|.*'+includeUrl+')")):
        print link
        interLink = link.get("href")
        # print interLink
        # print link.attrs
        if interLink is not None and interLink not in internalLinks:
            if interLink.startswith("/"):
                internalLinks.append(includeUrl + interLink)
            else:
                internalLinks.append(interLink)
    return internalLinks


# Get all the external links of the page
def getExternalLinks(soup):
    externalLinks = []
    # Find all the links starting with 'http' or 'www'
    for link in soup.findAll("a", href=re.compile("^(http|www).*$")):
        # print link
        extLink = link.get('href')
        # print extLink
        if extLink is not None and extLink not in externalLinks:
            externalLinks.append(extLink)
    return externalLinks


# Get all the external links of the website

allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = requests.get(siteUrl).text
    soup = BeautifulSoup(html)
    internalLinks = getInternalLinks(soup, siteUrl)
    # print internalLinks
    externalLinks = getExternalLinks(soup)

    for link in externalLinks:
        allExtLinks.add(link)
        # print link

    for link in internalLinks:
        if link not in allIntLinks:
            # print "Coming internal url is:" + link
            allIntLinks.add(link)
            # print link
            getAllExternalLinks(link)


startingPage = "http://www.qmtjr.com"
html = requests.get(startingPage).text
soup = BeautifulSoup(html)
# links = getExternalLinks(soup, "")
# links = getInternalLinks(soup, startingPage)
getAllExternalLinks(startingPage)

# print allExtLinks
# print links
