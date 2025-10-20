#on lance 10 fois un dé équilibré à 6 faces
#si ou obtien 6 , on gagne 100 €
#si ou obtien 5, on gagne 50 €
#dans les autres cas , on perd 20 €

#AFFICHAGE :LANCER 1 Dé =3 gain cumulé =-20
#           LANCER 2 Dé =5 gain cumulé =-30
#           LANCER 3 
#           LANCER 4 
            
#           LANCER 10

from random import randint
gain = 0

N = int ( input ( " entrez un entier N " ))

for k in range (1 , N+1 ) :
    de = randint (1 , 6 )
    
    if de==6 :
        gain= gain + 100
    
    if de== 5 : 
        gain = gain + 50
    if de == 1 or de == 2 or de == 4 :
        gain = gain -20
        
   #print ("dé = " , de )
    print (" lancer " , k , "de = " , de   , "gain cumulé = " , gain ,"€" )



