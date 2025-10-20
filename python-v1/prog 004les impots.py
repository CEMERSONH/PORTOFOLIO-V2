
e= int (input("entrez le Nbres d'enfants"))
s= float (input("entrez le salaire annuel"))
print ("vous avez ",e,"enfants")
print ("votre salaire est de",s,"€")

if e==0 :
    if s<= 18000:
        print("impots = 500€")
    elif s>= 36000:
        print("impots = 2000€")
    else:
        print("impots = 1000€")
                      
elif e==1 or e==2:
    if s<= 18000:
        print("impots = 300€")
    elif s>= 36000:
        print("impots = 1600€")
    else:
        print("impots = 800€")
                      
else:
    if s<= 18000:
        print("impots = 100€")
    elif s>= 36000:
        print("impots = 1200€")
    else:
        print("impots = 500€")
    
    
                
                
                
