# random=hasard integrer=entier
# on lance un dé , equilibre , à 6 faces 
# on lance un dé , equilibre , à 8 faces

from random import randint

# à partir de la bibliothèque random
# importer la commande randint

# si on obtient 6or8 , on gagne 1000 €
# si on obtient 5or7 , on gagne 500 €
# si on obtient 1or1 , on relance les dés 1 seule fois
# ET on recommance 3 fois

gain =0
print ("#lancer 1")#1
de6 = randint (1 , 6)
de8 = randint (1 , 8)
print( "de6=" , de6 , "de8=" , de8)
if de6 == 6 or de8== 8 :
    print ( "6et8 !!!OMG!!!vous avez gagnez 1000 € " )
    gain= 1000 + gain

if de6== 5 or de8== 7 :
    print ( "5et7.vous avez gagnez 500 € ")
    gain= 500 + gain

if de6== 1 or de8== 7 :
    de6 = randint (1 , 6)
    de8 = randint (1 , 8)
    
    if de6== 6 or de8== 8 :
        print ( "6et8. OMG!!!vous avez gagnez 1000 € " )
        gain=1000 + gain

    if de6== 5 or de8== 7 :
        print ( "5et7.vous avez gagnez 500 € " )
print ("gain= cumulé" , gain)

print("#lancer 2")#2
de6 = randint (1 , 6)
de8 = randint (1 , 8)
print( "de6=" , de6 , "de8=" , de8)
if de6 == 6 or de8== 8 :
    print ( "6et8 !!!... 1000 € " )
    gain= 1000 + gain

if de6== 5 or de8== 7 :
    print ( "5et7.vous avez gagnez 500 € ")
    gain= 500 + gain
if de6== 1 or de8== 7 :
    de6 = randint (1 , 6)
    de8 = randint (1 , 8)
    
    if de6== 6 or de8== 8 :
        print ( "6et8. OMG!!!vous avez gagnez 1000 € " )
        gain= 1000 + gain
    if de6== 5 or de8== 7 :
        print ( "5et7.vous avez gagnez 500 € " )
        gain= 500 + gain
print ("gain= cumulé" , gain)
print ("#lancer 3")#3
de6 = randint (1 , 6)
de8 = randint (1 , 8)
print( "de6=" , de6 , "de8=" , de8)
if de6 == 6 or de8== 8 :
    print ( "6et8 !!!OMG!!!vous avez gagnez 1000 € " )
    gain= 1000 + gain 
if de6== 5 or de8== 7 :
    print ( "5et7.vous avez gagnez 500 € ")
    gain=500 + gain
if de6== 1 or de8== 7 :
    de6 = randint (1 , 6)
    de8 = randint (1 , 8)
    
    if de6== 6 or de8== 8 :
        print ( "6et8. OMG!!!vous avez gagnez 1000 € " )
        gain= 1000 + gain
    if de6== 5 or de8== 7 :
        print ( "5et7.vous avez gagnez 500 € " )
        gain=500 + gain
print ("gain= cumulé " , gain)



































        
