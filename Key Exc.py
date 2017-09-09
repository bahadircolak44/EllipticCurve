import math
import time
from EllipticCurve import *
from PointAddition import *

def pointDoubling(a,b,x,y,f):
    Alice= EllipticCurve(a,b)
    (x,y) =  Alice.sum_ee(x,y,f)
    return (x,y)

def pointAddition(a,b,x1,y1,x2,y2,f,i):
    Alice= PointAddition(a,b)
    (x3,y3)=Alice.sum_ee(x1,y1,x2,y2,f)
    return (x3,y3)

def Ayse():
    alfa=2
    G = keyExchange(alfa,1)
    print "Ayse %dP yi yayinliyor.... " %alfa,G
    print "-------------------------------------------"
    G2=Bora(G)
    G3=diffieHellman(G2,alfa)
    print"Ayse nin elde ettigi:" ,G3
    
def Bora(G2):
    beta =5
    G = keyExchange(beta,1)
    print "Bora %dP yi yayinliyor...  " %(beta),G 
    print "-------------------------------------------"
    G3=diffieHellman(G2,beta)
    print "Bora nin elde ettigi:",G3
    return G
def keyExchange(k,v):
    (a , b) = (0,1)
    (x1,y1) = (7,5)
    (x2,y2) = (1,1)
    f = 11
    (x2,y2)=pointDoubling(a,b,x1,y1,f)
    if v==1:
        print "  P:" ,(x1,y1)
    for i in range(3,k+1):
        if v==1:
            print"%  dP"%(i-1),(x2,y2)
        if x1 > x2:
            (x2,y2)=pointAddition(a,b,x2,y2,x1,y1,f,i)
        elif(x1 < x2):
            (x2,y2)=pointAddition(a,b,x1,y1,x2,y2,f,i)
        
    if v==1:
        print "-------------------------------------------"
            
    return (x2,y2)
def diffieHellman(G,k):
    (a , b) = (0,1)
    (x1,y1) = G
    f = 11
    (x2,y2) = pointDoubling(a,b,x1,y1,f)
    for i in range(1,k-1):
        if x1 > x2:
            (x2,y2)=pointAddition(a,b,x2,y2,x1,y1,f,i)
        elif(x1 < x2):
            (x2,y2)=pointAddition(a,b,x1,y1,x2,y2,f,i)
        print(x2,y2)
    return (x2,y2)
#pointDoubling(0,1,2,3,11)
timestamp1 = time.time()
Ayse()
timestamp2 = time.time()
print "This took %.2f seconds" % (timestamp2 - timestamp1)
