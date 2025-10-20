#on lance 60 fois un dé équilibré à 6 faces
#on compte le nombre dé 1 obtenus
#on compte le nombre dé 2 obtenus
#on devrait obtenire 10et10



from random import randint

c1=0 ; c2=0 ; c3=0 ; c4=0 ; c5=0 ; c6=0

for i in range (1 , 61 ) :
    de = randint (1 , 6 )
    
    if de==1 :
        c1= c1 + 1
    if de==2:
        c2= c2 + 1
    if de==3:
        c3= c3 + 1
    if de==4:
        c4= c4 + 1
    if de==5:
        c5= c5 + 1
    if de==6:
        c6= c6 + 1

        
print("c1=" , c1 , "c2=", c2 , "c3=" , c3 , "c4=", c5 , "c6=" , c6)
        
