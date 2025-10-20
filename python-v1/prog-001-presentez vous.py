prenom=str(input("quel est votre prénom?"))
#str=string=chaine de caractère
#input=clavier

annee=int(input("quelle est votre année de naissaince?"))
#int=nbre entier

age=2025-annee

f=int(input("combien de frère avez-vous?"))
s=int(input("combien de soeur avez-vous?"))






print("bonjour",prenom)
print("vous avez",age,"ans")
#print("vous avez",f,"frére et",s,"soeurs")

#Pas beau,il faut gerer le singulier,le pluriel

if f==0:
    print("vous n'avez pas de frére")
if s==1:
    print("vous avez 1 frére")
if f>1:
    print("vous avez",f,"frére")

if s==0:
    print("vous n'avez pas de soeur")
if s==1:
    print("vous avez 1 soeur")
if s>1:
    print("vous avez",s,"soeur")
    
#prenom[0] est la 1ere lettre de la variable
#prenom[1]  "  la 2eme  "      "  "    "
#len(prenom)est  le nombre de lettre de prenom
#len(prenom)est  le nombre de la longueur de la variable prenom
#prenom[len(prenom)-1] est la dernierr lettre de la variable prenom

print("votre prénom commence par",prenom[0],"et se termine par",len(prenom)-1)
print("votre prénom contient ",len(prenom),"lettre")
