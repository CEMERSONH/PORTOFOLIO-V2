#phrase = str(input ("Entrez une phrase " ))
#longueur = len (phrase)             
#print (phrase)
#print ( "cettre phrase contient" , longueur , "caracteres" )

#l1 = phrase [1]
#l5 = phrase [4]
#dl = phrase [len (phrase)-1]
#adl= phrase [len (phrase)-2]
#print ("le 1er caracter est" , l1 , "et le 5emme est" , l5 )
#print ("le dernier caracter est" , dl )
#print ("l'avant dernier caracter est" , adl )
#print (l1*7 + l5*7 + "je suis beau"*3)
prenom = str(input("quel est votre prénom? "))
nom = str (input ("quel est votre nom "))
genre=int(input("Entrez 1 si vous etres un homme,2 si vous etres une femme "))
           
if genre ==1:
    print("Bonjour monsieur",prenom,nom)
           
else:
    print("Bonjour Madame",prenom,nom)
    
print ("vos initiales sont" , prenom[0],nom[0])
print ("votre prenom finit par" , prenom[len(prenom)-1])
print ("votre nom finit par"    ,   nom[len(nom)-1])
print (prenom[0]*2 + prenom +"  " + nom[0]*2+nom)

         





