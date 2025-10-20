#On entre un nbre A
#On entre un nbre ENTIER debet 
#et on affiche la table de multiplication
#par A,de debut xA jusquaaaaa 10XA

A=float(input("Entrez un nombre"))

fin=int(input("Entrez un nombre entier pour la fin de la table"))

debut=int(input("Entrez un nombre entier pour le debut de la table"))

print("voici la table demultiplication par",A,"2,3 à parire de 1x",debut,"x",A,"3 jusqu'a 10x",fin,"x",A)

for i in range (debut,fin+1):
    print (i,"x",A,"=",i*A)

    
    
    
