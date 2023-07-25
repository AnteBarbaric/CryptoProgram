def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    plaintext = ''.join([i for i in plaintext if not i.isdigit()])
    order = {int(val): num for num, val in enumerate(key)} ##dict, svakom znaku kljuca pridruzili vrijednost
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext

def standardText(text):
    while((len(text))%5!=0):
        text+="0"
    return text
    
def ispisText(x,t):
    list=[]
    i=0
    nova_rijec=""
    for word in x:
        nova_rijec+=word
        i+=1
        if(i>t-1):
            i=0
            list.append(nova_rijec)
            nova_rijec=""
    return list
    
def listToString(text):
    return ' '.join(text)
    
x=encode('234615', 'SHESAIDDONTLETGONEVERGIVEUPITSSUCHAWONDERFULLIFE')
##x=encode('3276451', 'THISISASECRETTEXTENCRYPTEDBYTHEDOUBLETRANSPOSITIONCHIPER')
##y=encode("521436",x)

z=listToString(ispisText(standardText(x),5))
print(z)

def removeZeroFromText(text):
    text=text.replace("0","")
    return text

def lengthOfText(text):
    return len(text)

import math
import numpy as np
def getPrimeFactors(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) +1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))
    return prime_factors

def listPrimeFactors(primeFact):
    import itertools
    from functools import partial
    combinations_with_r = partial(lambda r: itertools.combinations(primeFact, r = r))
    list1=[]
    for r in map(combinations_with_r, range(1, len(primeFact) + 1)):
        for j in r:
            list1.append(np.prod(j))
    list1 = list( dict.fromkeys(list1) )
    return list1[:-1]

def chooseNumb(lista):
    numb=input("Unesite neki broj iz dane liste faktora(koji ce biti broj stupaca): ")
    b=False
    while b==False:
        if numb.isdigit():
            b=True
        else:
            numb=input("Ponovo unesite broj jer ste unijeli slovo: ")
            b=False
        
    a=False
    while a==False:
        if(int(numb) in lista):
            a=True
        else:
            numb=input("Ponovo unesite broj: ")
            a=False
    return(numb)
    
lista=listPrimeFactors(getPrimeFactors(lengthOfText("AAOSAJRTIEEAAAUSCEAEIANPIJAJJNFVSOIRZVPHNIONARNZIJINUSSNTRZUTIC")))
duljina=lengthOfText("AAOSAJRTIEEAAAUSCEAEIANPIJAJJNFVSOIRZVPHNIONARNZIJINUSSNTRZUTIC")
print(listPrimeFactors(getPrimeFactors(lengthOfText("AAOSAJRTIEEAAAUSCEAEIANPIJAJJNFVSOIRZVPHNIONARNZIJINUSSNTRZUTIC"))))
t=chooseNumb(lista)
t=int(t)
h=ispisText(standardText("AAOSAJRTIEEAAAUSCEAEIANPIJAJJNFVSOIRZVPHNIONARNZIJINUSSNTRZUTIC"),int(duljina/t))
print(h)

def listOfLists(h):
    letters = [ list(x) for x in h ]
    arr = (np.array(letters)).transpose()
    return arr

def listOfOmjers(arr):
    listOmjera=[]
    for i in range(0,len(arr)):
        brSam=0
        brSug=0
        for j in range(0,len(arr[i])):
            if (arr[i][j]=='A' or arr[i][j]=='E' or arr[i][j]=='I' or arr[i][j]=='O' or arr[i][j]=='U'):
                brSam+=1
            else:
                brSug+=1
        listOmjera.append(str(brSam)+":"+str(brSug))
    return listOmjera
    
def finalPrint(arr,listOmjera):
    for i in range(0,int(duljina/t)):
        print(str(arr[i])+" "+str(listOmjera[i]))
        
finalPrint(listOfLists(h),listOfOmjers(listOfLists(h)))