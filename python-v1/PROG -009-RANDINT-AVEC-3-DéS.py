#ON LANCE UN DE tétraédrique,équilibré (4face)
#ON LANCE UN dé octaédrique ,équilibré  (8face)
#ON LANCE UN dé dodécaédrique,équilibré (12face)
#SI ON OBTIENT 3 NUMEROS IDENTIQUE, ON GAGNE 100€
#SI ON OBTIENT 2 NUMEROS IDENTIQUE, ON GAGNE 50€

#ET ON RECOMMENCE 10 FOIS

from random import randint

print ("lancer 1 du jeu  ")


de4= randint (1 , 4)

de8= randint (1 , 8)

de12= randint (1 , 12)

gain=0

if de4==de8==de12 :
    gain=gain+100

print ( "dé4=" , de4 , "dé8=" , de8 , "dé12=" , de12 , gain)  

for i in range (1 , 101):
    gain=0
    de4= randint (1 , 4)
    de8= randint (1 , 8)
    de12= randint (1 , 12)
    if de4==de8==de12 :
        gain=gain + 100
        print
        print ("dé4=" , de4 , "dé8=" , de8 , "dé12=" , de12 ,"gain cumilé=" , gain)

    elif  de4==de8 or de4==de12 or de8==de12:
        gain=gain+50
        print("hooo hoooo 50€")
        print("de4=...")
    else:
        gain=gain-300

print ("bilan des 100 lancees:",gain,"€")
    



    
