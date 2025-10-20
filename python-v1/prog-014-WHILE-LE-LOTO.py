#UNE Urne contient 50 BOULES NUMEROTEE

#DE 1 à 50

#ON extrait une boule au hasard


#pour chaque boule , si le numero

#est superieur ou égale a 40 on gagne 10 euros

#sinon on perd 1 euros

#affichage finale "le premier 50 est apparu au 17em tirage

# gain cumulé= 229 €

from random import randint

#b=randint (1,50)

#print (b)

b=0 ; gain=0 ; c=0

while b!=50:
    b=randint(1 , 50)
    print(b)
    c=c+1
    print("le premier 50 est apparu au" , c , "emme tirage")

    if b >=40:
        gain=gain+10
        
    else:
        gain=gain-1
        
    print ("tirage=" , "boule =" , b , "gain =" , gain )
    print ("tu as gagné " , gain , "€")
    
    
