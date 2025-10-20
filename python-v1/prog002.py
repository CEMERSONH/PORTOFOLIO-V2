 #on entre la note francais (coeff 2)
#on   "        "    maths       "
#"        "      d'informatique (coeff 5)
#si la moyenne est >=10:Admins
#si  "     "    "  >=8 :Eliminé
#si 8<= moyenne <10
#sinon eliminé


f=float(input("entrez la notre de francais"))
m=float(input("entrez la notre de maths"))
i=float(input("entrez la notre de informatique"))

print(f,m,i)

moy=(f*2+m*2+i*5)/9
print(moy)
        
if moy >=10:
    print("candidat admis")
elif moy<8:
    print("candidat éliminé")
else:
    r=float(input("entrez la note de ratrapage"))
    if r>=10:
        print("candidat admis")
    else:
        print("inafff")
        
