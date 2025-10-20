# ON entre un nbre entre 10 et 100
# et l'ordinateur fait la meme demande
# tant que l'utilisateur
# Et a partir de la 10eme eureur, lodinateur
# affiche "ereur ! tu ne comprends rien !
# on entre deux mots qui commencent par la meme
# lettre et 
c = 0
N=float(input("entrez un nbre entre 10 et 100 "))
print (N)
while not (10<= N <= 100):
    c = c + 1
    print ("erreur",c)
    if c >=5 :
        print ("fates attention ")
    N=float(input("Erreurrrrrrrrr!ENTREZ..UN..NBRE..entre..10..et..100 "))


mot1=str(input("entrrrez un premier mot "))
mot2=str(input("entrrrez un 2nd  mot qui commence par la meme lettre que le 1re"))

while not (mot1 [0] == mot2 [0] ) :
    print ("erreur")
    mot1=str(input("entrrrez un premier mot "))
    mot2=mot2=str(input("entrrrez un 2nd  mot qui commence par la meme lettre que le 1re"))




    
    
    
   
    
    
    
        
