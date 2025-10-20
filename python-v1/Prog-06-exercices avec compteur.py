mot = str (input ("Entrez un mot de 4 lettres "))
c = 0 #initialisation du compteur
if len (mot) ==4:
    print ("dans le if")
    if mot[0] == "a" or mot [0] == "A":
        print ("la 1er lettre est a ou A ")
    if mot[1] == "a" or mot [1] == "A":
        print ("la 2emme lettre est a ou A ")
    if mot[2] == "a" or mot [2] == "A":
        print ("la 3eme lettre est a ou A ")
    if mot[3] == "a" or mot [3] == "A":
        print ("la 4eme lettre est a ou A ")
        c = c + 1
    print ("ce mot contient" , c , " a ou A ")
    
else:
    print("Eureur!!! ce mot contient " , len (mot) ,"lettre ")

compt = 0
a = float (input ( "Entrez un 1er nombre a "))
b = float (input ( "Entrez un 1er nombre b "))
c = float (input ( "Entrez un 1er nombre c "))
print (a , b , c )
if 5 < a < 10 :
    compt = compt + 1
if 5 < b < 10 :
    compt = compt + 1
if 5 < c < 10 :
    compt = compt + 1
print ("il y a " , compt , "nombres entre 5 et 10 ")
    
    
