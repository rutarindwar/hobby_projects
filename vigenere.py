# vigenere cypher

def encodevig(mess,key):
    al = "abcdefghijklmnopqrstuvwxyz"
    mess = ''.join([i.lower() for i in mess if i.lower() in al])    
    numMess = [ al.index(i) for i in mess]
    longKey = (len(mess)//len(key)) * key + key[:(len(mess)%len(key))]
    numKey = [al.index(i) for i in longKey]

    numCypher = [(numMess[i] + numKey[i])%26 for i in range(len(numMess))]

    cypherText = ''.join([al[i] for i in numCypher])
    return cypherText


def decodevig(cyph, key):
    key = key.lower()
    cyph = cyph.lower()
    al = "abcdefghijklmnopqrstuvwxyz"  
    numCyph = [ al.index(i) for i in cyph]
    longKey = (len(cyph)//len(key)) * key + key[:(len(cyph)%len(key))]
    numKey = [al.index(i) for i in longKey]

    numText = [(numCyph[i]- numKey[i])%26 for i in range(len(numCyph))]
    mess = ''.join([al[i] for i in numText])
    return mess



