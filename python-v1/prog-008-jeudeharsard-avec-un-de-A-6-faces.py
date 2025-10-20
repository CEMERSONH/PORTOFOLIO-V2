#random=hasard integer=entier
#randitnt(6),c'est un nbre au hasard entre 1 et 6

#on entre un entier N fois 

from random import randint
N=int(input("entrez un nombre entier"))
gain=0

for i in range (1,N+1):
    de=randint(1,6)
    
    print ("lancer" , i , "de=" , de)
    
    if de==6:
        gain=gain+100
    else:
        gain=gain-10
        
    print("lancer numero" , i , " de=" , de , "gain=" , gain)
