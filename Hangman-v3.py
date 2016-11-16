## Hangman

import sys
ALPH = 'abcdefghijklmnopqrstuvwxyz'


def openfile():
    dictfile= open('words.txt', 'r') # use Dictionary.txt or words.txt
##    dictfile= open('USdictionary.txt', 'r')    
    d = dictfile.readlines()
    d = [i[:-1].lower() for i in d[1:]]
##    print (d[:10])            
    return d

def checkWord(s, wl):
    if s in wl:
        print('y')
        return 1
    else:
        print ('This word is not in my dictionary.')
        return 0
##    
##def adjustLength(l, n):
##    for item in l:
##        if len(item) != n:
##            l.remove(item)
##    return l

def statistics(lst, pval):
    n = len(lst)
    statsdic = {}
    lst = ''.join(lst)

    for i in pval:
        statsdic[i] = lst.count(i)*100/n
    return statsdic

def maxstat(dic):
    maxm = max(dic.values())
    for i in dic.keys():
        if dic[i] == maxm:
            return i

def verify(word, lst, values, misses, guessedltr):
    newInput = input(': ').lower()

    # The new input is the same as earlier; no change occurs.
    if newInput == word:
        misses -= 1
        values = values.replace(guessedltr, '')
        lst = [j for j in lst if guessedltr not in j]
        return word, lst, values, misses

    # Changes occur.
    else:
        d = {}

        # create dictionary {'index': '-'/'a'}
        for i in range(len(newInput)):
            d[i] = newInput[i]

        # scan new input and update word, wlst and values.
        # i is a tuple (key: value)
        for i in d.items():
            if i[1] != '-':
                
                # update list of possible values/letters.
                values = values.replace(i[1],'')

                # update range in dictionary. 
                lst = [ j for j in lst if j[i[0]] == i[1]]

                ## finish this function, see whatelse I need to update
                ## beside wlst, posval, misses.
                ## TRON time !!
        word = newInput
        return word, lst, values, misses
                
            
            
    
    
def main():
    wlst = openfile()
##    print (wlst[:10])
    hangword = input(': ')
    wlst = [ i for i in wlst if len(i) == len(hangword)]
    print (len(wlst))
    mistakes = 13
    posval = ALPH
##    print (hangword)

    while ((mistakes > 0) and (hangword.count('-') != 0)):
        if len(wlst) == 1:
            print ('The word is %s' % wlst[0])
            mistakes = 0
        else:
            stat = statistics(wlst, posval)
            letter = maxstat(stat)
            print ('%s ...?' % letter)
            hangword, wlst, posval, mistakes = verify(hangword, wlst, posval, mistakes, letter)
            print (len(posval))
            print ('errors left: %i' % mistakes)
            print ('list of possible words : %i'% len(wlst))

    if len(wlst) !=0:
        for i in wlst:
            print (i)
    print ('Done')          

main()
