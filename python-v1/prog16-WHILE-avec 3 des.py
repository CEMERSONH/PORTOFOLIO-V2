
#on lance 3 des equilibrés a 6face
#jusqu ' a ce que la somme des 3 soit
#superieur ou egale a  17 
#Et compte le nbre de lancers

from random import randint

de1= randint (1,6)
de2= randint (1,6)
de3= randint(1,6)
c=1
while not (de1+de2+de3>=17):
    de1=randint(1,6); de2=randint(1,6); de3=randint(1,6)
    c=c+1
    print("de1=" ,de1, "de2=" ,de2, "de3=" , de3," lancer" ,c)

print("bravo vous avez obtenu une note superieur ou egale a 17 au lancer",c)
    
