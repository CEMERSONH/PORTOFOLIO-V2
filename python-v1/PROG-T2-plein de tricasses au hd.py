
from random import randint
import turtle
turtle.speed (100)

#definition de la proocedure carre

def carre (a , b , c ):

#a= abscisse 
#b= ordonnes
#c= la longueur du côté
    turtle.penup ()
    turtle.goto (a-c/2 , b-c/2 ) 
    turtle.pendown () 
    turtle.goto (a+c/2 , b-c/2 )
    turtle.goto (a+c/2 , b+c/2 )
    turtle.goto(a-c/2,b+c/2)
    turtle.goto (a-c/2 , b-c/2 )
    
#carre (0 , 0 , 200)
#carre (-50 , -10 , 20 )

#on choisie a au hasard entre -200 et 200
#           b
#           c                   50 et 50
# et on appelle carre (a , b , c )
# et on recommance 30 fois


def tricarre ():
    turtle.width (13)
    turtle.color ("gold")
    carre (a, b, c)
    turtle.width (6)
    turtle.color ("silver")
    carre (a, b, c)
    turtle.width(2)
    turtle.color("green")
    carre(a, b, c)

for k in range (1 , 51 ):
    a=randint (-200 , 200)
    b=randint (-200 , 200)
    c=randint (5 , 50)
    tricarre( )

    
