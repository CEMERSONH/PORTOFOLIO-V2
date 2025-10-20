
#L'ordinateur demande d'entrer un mot de 5 lettres avec exactement 2 "a"
#Et l'ordinateur repose la questions tant que l'utilisateur se trompe.



#pour les 5 lettres


mot=str(input("Entrez un mot de 5 lettres avec 2 a "))

while not(len(mot)==5):
    mot=str(input("Erreur!!ce mot n'a pas de 5 lettres..Entrez un mot..avec 2a " ))
print("Le mot " ,mot, " a bien 5 lettres ")

#Pour les 2 "a"

c=0
for i in range (0 , 5):
    if mot[i]=="a":
        c=c+1
        print(" un A trouvé!!")
        
print("le mot" ,mot, "contient",c,"a") 

while not (c==2):
    #on recommence tout , le input,commpter les "A"
    mot=str(input("entrez un mot de 5 lettres avec 2 "))
    c=0
    for i in range (0,5):
        if mot[i]=="a":
            c=c+1
            print ("un a trouvé")
    print(mot,"contient",c,"a")
