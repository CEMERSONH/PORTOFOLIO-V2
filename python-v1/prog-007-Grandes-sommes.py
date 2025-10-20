
#on rentre un nbre entier N

#L'ordinateur cacule la "grande" somme 1+2+...+N

N=int(input("Entrez un Nbre entier N "))

print("voici la valeur de la somme 1+2+...+" , N-1 , "+" , N)

s=0

for i in range(1 , N+1 ):
    s=s+i
    print("i=" , i,"s=" , s)
    
print("1+2+...+" , N-1 , "+",N,"=" , s)

#L'ordinateur cacule la "grande" somme 1**2+2**2+3**3+...+N**2

print("voici la valeur de la somme 1**2+2**2+...+" , N-1 , "+" , N**2)

S=0

for i in range(1 , N+1**2 ):
    S=S+i**2
    print("i=" , i**2 , "s=" , S)
    
print("1**2+2**2+...+" , N-1**2 , "+" , N , "**2=" , S)

#print("voici la valeur de la somme 1+2+" , N-1 , "+" , N)
#s=0
#texte=""

#for i in range(1 , N+1 ):
    #s=s+i
    #texte=texte+"+"+ chr(i)
    #print("i=" , i , "s=" , s)
#print(texte , "=" , s)

#calcul de ,si N=100,
#(100+1)/1+(100+2)/2+...+(100+99)/99+(100+100)/100




s3=0

for i in range(1 , N+1 ):
    s3=s3 + (N + i) / i
    print("i=" , i , "s=" , s)
    
print("(" , N , "+1)/1+(" , N , "+2)/2+...+(" , N , "+" , N , ")", N , "=" , s)


#la somme des cubes
#on calcule s4=1**3+2**3+...+(N-1)**3+N**3


s4=0

for i in range(1 , N+1 ):
    s4=s4+i**3
    print("i=" , i**3 , "s4=" , s4)

print("la somme des cubes de 1**3a",N,"**3=")

print("1**3+2**3+...+" , N-1 , "**3+" , N , "**3=" , s4)









