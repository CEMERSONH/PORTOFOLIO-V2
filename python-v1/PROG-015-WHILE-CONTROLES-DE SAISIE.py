# On rentre un nbre superieur ou egal a 100
#L'ordinateur repose la meme question tant que lutilisateur se trompe
#On entre un a ou A ou b ou B
#L'ordinateur
#.........se trompe


N=float(input("Entrez...........ou egal a 100 "))

while not(N>=100):
    N=float(input("Eureur!! Entrez .......a 100 "))


l=str(input("Entrez..un..a.......ou..un..B" ))
while not(l== "a" or l== "A" or l== "b" or l== "B" ):
    l=str(input("Eureur!! Entrez ......un a ou A ou b ou B " ))

#on entre un mot de 4 lettre
    
mot=str(input("Entrez..un..mot..a..4..lettre..ex..BABA..ou..LILI.. " ))
while not(len(mot)==4):
    mot=str(input("Eureur!! Entrez ......un..mot..a..4..lettre.. " ))


#On entre un nbre entre 10 et 100
#


l= 0

N=float(input("entrez un nbre entre 10 et 100 "))
print (N)
while not (10<= N <= 100):
    l = l + 1
    print ("erreur",l)
    N=float(input("!!ENTREZ..UN..NBRE..entre..10..et..100 "))
    
