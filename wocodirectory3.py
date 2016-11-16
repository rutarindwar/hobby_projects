#get woffod directory
# Python 3
#import urllib.request
import urllib
from time import *
import sys
import os
ub = "http://www.wofford.edu/search/searchFacultyStaffResults.aspx?\
students=True&facultyStaff=False&first=&last="

al = "abcdefghijklmnopqrstuvwxyz"
nhint = 'style="font-weight:bold;">'
ehint = 'mailto:'
md = {}
mc = []
st = time()

outf = open('wocodirectory.txt', 'w')

old = 0
for i in al:
##    print ('====> fetching all %s ...'%i)
    #p = urllib.request.urlopen(ub+i)
    p = urllib.urlopen(ub+i)
    f = p.read()
    d = f.decode("utf8")
    p.close()
    t = d.count(nhint)
    mc.append(t)
##    print ('There are %i names matching this search'% t)
    l = 0
    old = len(md)
    for j in range(t):
        ns = d.find(nhint,l) + len(nhint)
        n = d[ns: d.find('</span',ns)].strip()
        es = d.find(ehint, ns) + len(ehint)
        e = d[es: d.find('">', es)]
        if n not in md.keys():
            md[n] = e
            #print ('%s: %s'% (n,e))
            outf.write('%s: %s\n'% (n,e))
        l = es
    print('After %s, we have %i students'%(i,len(md)))
    old = len(md)
endt = time()

outf.close()
