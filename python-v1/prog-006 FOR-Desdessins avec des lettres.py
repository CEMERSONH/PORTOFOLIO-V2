#On entre une lettre (ou n'importe quel caractere du clavier)
#On dessine un carré de cote 10 avec des lettres
#On entre un entier n 

l=str(input("entrez une lettre"))
N=int(input("entrez un entier"))
l2=str(input("entrez une lettre"))

#Un triangle formé de "l" de hauteur N
    
for i in range (1,N+1):
    print (l*i)
    
#On dessine un carré de cote N
    
for i in range (1,N+1):
    print (N*l)
    

#Un carré de côté de N, remplie de "l"
#Entouré d'une rangée de "l2"
    
ligne1=l2*(N+2)
ligne2=l2+l*N+l2
print(ligne1)                        
print(ligne2)

for i in range (1,N+1):
    print(ligne2)
    
print(ligne1)

#Un carré de côté de N, remplie d'une DOUBLE rangée "l2"

ligne1=l2*(N+4)
ligne2=l2*2+l*N+l2*2
print(ligne1)
print(ligne2)

for i in range (1,N+1):
    print(ligne2)
    
print(ligne1)
print(ligne1)










