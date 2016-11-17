# Webscraping the website of 88.9 radio milwaukee

from BeautifulSoup import BeautifulSoup
import urllib2
import calendar
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import operator
import os

def merge(d1, d2, merge_fn=lambda x,y:y):
    """merge(d1, d1, lambda x,y: x+y)"""
    
    result = dict(d1)
    for k,v in d2.iteritems():
        if k in result:
            result[k] = merge_fn(result[k], v)
        else:
            result[k] = v
    return result



chdr = "/Users/rutarindwa/Documents/Docs/Python Scripts/chromedriver"
os.environ["webdriver.chrome.driver"] = chdr
driver = webdriver.Chrome(chdr)

ha = 'div class="storyName">        <div><a href='
hs = '<div class="sectionTitle">        <span><a href='
month = 12
c = calendar.TextCalendar()
mtmp = c.monthdatescalendar(2014,month)
m = [i for s in mtmp for i in s]
daylst = [i for i in m if i.month == month]
masterList = {}


tabc = 0

for dind in range(len(daylst)):
    day = daylst[dind]
    tic = time.time()
    daystr = day.strftime('%Y-%m-%d')
    url = "http://radiomilwaukee.org/playlist/%s"%daystr
    driver.get(url)
    page = driver.page_source
    tabc += 1

    if (tabc == 5):
        driver.close()
        driver = webdriver.Firefox()
        tabc = 0        
####    else:
####        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
####    
    txt = page.encode('utf-8')
    count = txt.count(ha)
    tmpdic = {}

    aend = 0
    for i in range(count):
        tmp = txt.find(ha, aend)
        abegin = txt.find('>', tmp+len(ha))
        aend = txt.find('<', abegin)
        artist = txt[abegin+1:aend]

        tmp = txt.find(hs, aend)
        sbegin = txt.find('>', tmp+len(hs))
        send = txt.find('<', sbegin)
        title = txt[sbegin+1:send]
        if (artist, title) not in tmpdic.keys():
            tmpdic[(artist, title)] = 1
        else:
            tmpdic[(artist,title)] += 1
    tmplen = len(masterList)
    masterList = merge(masterList, tmpdic, lambda a,b:a+b)
    print "Found %d new songs on %s in %3.2f secs (%d)"%(len(masterList)-tmplen,\
                                                         daystr,\
                                                         time.time() - tic,\
                                                         len(masterList))



sml = sorted(masterList.items(), key=operator.itemgetter(1), reverse=True)
fout = open('RadioMilwaukee_12_2014.txt', 'w') # change _2_ to value of month

for it in sml:
    st = "%s, %s, %d\n" %(it[0][1], it[0][0], it[1])
    fout.write(st)

fout.close()
















