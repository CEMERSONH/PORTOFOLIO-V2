 


#on lance 2 des a 20 faces

# jusqu'a odtenir deux 20

#from random import randint

#de= randint (1 , 20 )
#print ( "dé=", de )

#while not (de==20 ):
#    de=randint (1,20  )
#    print ("dé=", de )
    
#print ("Bravo,vous avez obtenu le 20")

    
    
#from random import randint
#de1 = randint (1,20)
#de2= randint (1 , 20 )
#print ( "dé=", de1 , "de2=" , de2 )

#while not (de1==20 and de2==20):
#    de1=randint (1,20  ); de2=randint (1,20)
#    print ("dé1=", de1,"dé2=" , de2 )
    
#print ("Bravo,vous avez obtenu le 20 et 20")


    
from random import randint
de1 = randint (1,20)
c=1
de2= randint (1 , 20 )
print ( "dé=", de1 , "de2=" , de2 )

while not (de1==20 and de2==20):
    de1=randint (1,20  ); de2=randint (1,20)
    c=c+1
    print ("dé1=", de1,"dé2=" , de2 , "au lancer" , c )
    
print ("Bravo,vous avez obtenu le 20 et 20 au lancer" , c)


