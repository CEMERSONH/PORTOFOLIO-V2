# On entre un NBRE N
# Et on affiche , pour N=10
# N         N*2         N*3
# 1         1           1
# 2         4           8
# .         .           .
# .         .           .
#10         100         1000

N = int ( input ( " entrez un nombre entier " ))

print ( " N = " , N )

print ( " N          N x N        N x N x N " )

for k in range ( 1 , N + 1 ) :
#    print ( " toto " )

    print ( k , "<->" , k**2 , "<->" ,  k**3 )
