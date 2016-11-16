# Getting Casey's bookshelf.
# Regis Rutarindwa, All rights reserved.

# Python 3
#import urllib.request

import urllib
from time import *
import sys
import os
ub = "http://www.cjob.me/www.cjob.me/index.php?option=com_content&view=article&id=5"

nhint = '</a><br/><i>'
ehint = '</i><br/>'


####outf = open('caseybookshelf.txt', 'w')


def readbookshelf():
    fname = 'caseybookshelf.txt'
    f = open(fname, 'r')
    d = f.readlines()
    f.close()
    d = [i[:-1] for i in d]
    shelf = []
    for j in d:
        l = j.split('|')
        shelf.append((l[1].strip(), l[0].strip()))
    return shelf

outf = open('caseybookshelf.txt', 'a')
inshelf = readbookshelf()
print ('There are currently %d book(s) in the shelf'%len(inshelf))
newbooks = 0
for i in range(200):
    #p = urllib.request.urlopen(ub)
    p = urllib.urlopen(ub)
    f = p.read()
    d = f.decode("utf8")
    p.close()
    ns = d.find(nhint) + len(nhint)
    title = d[ns: d.find(ehint,ns)].strip()
    es = d.find(ehint, ns) + len(ehint)
    author = d[es: d.find('<br/>', es)]
    if (author, title) not in inshelf:
        newbooks += 1
        inshelf.append((author, title))
        print ('%s by %s'%(title, author))
        
        outf.write('%s | %s\n'%(title,author))
    else:
        #print ('Old book: %s by %s ****************'%(title, author))
        print ('.')
outf.close()
print ('***************************************')
print ('\n\nMaster, I have found %i new book(s).' % newbooks) 
