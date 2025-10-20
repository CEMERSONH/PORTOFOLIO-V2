# on lance 3 dés , équilibres , à 6 faces
# on mise 500 €
# on gagne 1000 €
# si 2 numeros seulement sont identiques,
# on gagne 500 €
# Et on recommance 3 fois
# Et on affiche les gains cumulés

from random import randint
gain = -500
print("lancer #1")
de1= randint (1,6)
de2= randint (1,6)
de3= randint (1,6)
print (de1 , de2 , de3)  

if de1==de2==de3 :
    gain= gain + 1000
    print ("vous avez gagné 100 €.gain cumulé=" , gain )
if (de1== de2 and de3!=de1) or (de1== de3 and de2 != de1) or (   ):
    gain= gain + 500
    print ("vous avez gagné 500 €.gain cumulé=" , gain )
