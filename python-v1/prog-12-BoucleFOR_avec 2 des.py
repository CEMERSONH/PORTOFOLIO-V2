# On entre un entier N
# Et on repète N fois :

# On lance 2 dés équilibrés à 6 faces
# si l'un des NBRES est >=5 alors
# on gagne 100€
# si les 2 NBRES sont <=2 , on perd
# 20€
# Aff: lancer 1 de1= 3  de2= 6   gain cumulé =100€
# Aff: lancer 2 de1= 2  de2= 1   gain cumulé =80€
# Aff: lancer ...
# Aff: lancer N

N = int ( input ( " Entrez un NBRES entier " ))

print ( " N= " , N )
from random import randint
gain= 0
for K in range ( 1 , N + 1 ):
    de1= randint ( 1 , 2 )
    de2= randint ( 1 , 6 )
    if de1>= 5 or de2>= 5 :
        gain = gain + 100
    if de1<=2 and de2<=2 :
        gain = gain -20

    print ( " lancer " , K , " de1= "  , de1 , " de2= " , de2 , " gain cumulé= " , gain , " € ")
