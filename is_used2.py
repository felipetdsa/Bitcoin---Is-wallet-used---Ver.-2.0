# directory.io

import urllib2

#def pp2(wallet, page, num_pages = 0):
#    count = page + num_pages
#    current = page
#    flag = True
#    if num_pages == 0:
#        page = 0
#    while page <= count and flag:
#        a = urllib2.urlopen('http://anonymouse.org/cgi-bin/anon-www.cgi/http://directory.io/' + str(current))
#        print current
#        for i in xrange(0, 129):
#            if wallet in a.readline():
#                print '----------', current
#                flag = False
#                break
#        current += 1
#    return current

def pp2(wallet, page, num_pages):
    count = 0
    res = []
    while count <= num_pages:
        print page
        for line in openurl(page):
            #print line
            if wallet in line:
                print page, line
                res.append(page)
        page += 1
        count += 1
    return res
                

def openurl(page):
    urllist = []
    a = urllib2.urlopen('http://anonymouse.org/cgi-bin/anon-www.cgi/http://directory.io/' + str(page))
    for i in xrange(129):
        urllist.append(a.readline())
    return urllist
