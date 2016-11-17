# finding visa restrictions for Rwandan citizen.
# webscraping visahq.com
# Author: Regis Rut.
# Released under MIT BSD and GPL licenses. :-P

import urllib2
from bs4 import BeautifulSoup
import time

f = open('visahq.txt', 'r')
d = f.readlines()
d = [k.strip() for k in d]
d = [k for k in d if len(k) > 0]


h1 = '<dd class=""><span class='
h2 = '<div><font class="vigreenb'
base = 'requirements/Rwanda/resident-United_States/'
t = [h[15:h.find('/',22)+1]+base for h in d]
tokeep = []
maybe = []
for i in range(len(t)):
    url = t[i]
    page = urllib2.urlopen(url)
    dat = page.read(65000)
    page.close()

    dec = dat[dat.find(h1)+len(h1)+1:dat.find('>', dat.find(h1)+len(h1))-1]
    if dat.find(h2) >= 0:
        mes = dat[dat.find(h2)+len(h2)+2:dat.find('<', dat.find(h2)+len(h2))]
        maybe.append(url[url.find('/')+2:url.find('.')])
        print
        print '%s ----> %s' %(url[url.find('/')+2:url.find('.')],str(dec))
        print '%s : %s' %(url[url.find('/')+2:url.find('.')],mes)
        print
    else:
        print '%s ----> %s'%(url[url.find('/')+2:url.find('.')],str(dec))

    if dec == 'not required':
        tokeep.append(url[url.find('/')+2:url.find('.')])
    #time.sleep(3)
