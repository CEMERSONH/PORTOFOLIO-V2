 
prenom = str (input ("quel est votre prénom ? "))
nom = str(input ("quel est votre nom ? "))
annee = int (input ("quelle est votre année de naissance ? "))
genre =int (input ("Entrez 1 si vous etres un homme,2 si vous etres une femme "))
taille = float(input("combiens mesurez-vous ? "))
poids = float(input("combiens pesez-vous ? "))
age = 2024-annee
imc = poids/taille**2
print("bonjour" , prenom , nom)
print ( " vous avez " , age ," ans ")
if genre ==1:
    print("Bonjour monsieur",prenom,nom)
else:
    print("Bonjour Madame",prenom,nom)
print ("vous avez" , age , "ans")
print ("vous mesurez" , taille , "mètres")
print ("vous pesez" , poids , "kilos")

if imc<= 18:
    print("Attentions! vous etres trop maigrichons")
    
if 18<=imc<25:
    print("vous avez un pois mormal")

if 25<=imc< 30:
    print("Attentions! vous etres en surpoids ")
    
if 30<=imc<40:
    print("Attentions! obesite")
    
if imc>40:
    print("Attentions! obesite")
    
    


