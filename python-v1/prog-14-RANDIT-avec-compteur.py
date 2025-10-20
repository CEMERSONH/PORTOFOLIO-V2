# On entre un entier N 
# On lance un de tetroedrique (4 face)
#                octaédrique (8 face)
#                icosaédrique (20 face)

# on repete N fois ces 3 des
from random import randint 
N= int (input("Entrez un entier "))
c=0
for k in range (1,N+1):
    de4=randint  (1,4)
    de8=randint  (1,8)
    de20=randint (1,20)
    print("lancer", k , "de4=" ,de4, "de8=" ,de8,"de20=" ,de20,"il y a" , c, "un an total " ) 

