#on lance un dé équilibre 20 faces
#et on arrête au 1er "six" obtenue 
#affichage : le 1er six est apparu au 8 eme lancer 
from random import randint

de=0 ; c=0
while de!= 20 :
    print("dans le while")
    c= c + 1
    de=randint(1 , 20)
    print ("dé=" , de)
print("le premier 20 est apparu au " , c , "ème lancer")

