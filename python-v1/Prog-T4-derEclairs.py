
import turtle
turtle.width (5)
def Eclairgrand (a , b , couleur):
    #(a , b) sont les coordonnées du bas de l'eclair
    turtle.color(couleur)
    turtle.penup ( )
    turtle.goto (a , b)
    turtle.pendown ( )
    turtle.goto (a + 30 , b + 30)
    turtle.goto (a + 20 , b + 70)
    

def Eclairpetit (a , b , couleur):
    #(a , b) sont les coordonnées du bas de l'eclair
    turtle.color(couleur)
    turtle.penup ( )
    turtle.goto (a , b)
    turtle.pendown ( )
    turtle.goto (a + 20 , b + 90)
    turtle.goto (a + 10 , b + 40)
    #turtle.goto (a + 30 , b + 30)
    
    

for K in range (1 , 6):
    turtle.width (K)
                
    Eclairgrand(50*K , 50*K , "blue")
    Eclairpetit(50*K , 50*K , "green")

    Eclairgrand(-50*K , 50*K , "blue")
    Eclairpetit(-50*K , 50*K , "green")

    Eclairgrand(50*K , -50*K , "blue")
    Eclairpetit(50*K , -50*K , "green")

    Eclairgrand(-50*K , -50*K , "blue")
    Eclairpetit(-50*K , -50*K , "green")
