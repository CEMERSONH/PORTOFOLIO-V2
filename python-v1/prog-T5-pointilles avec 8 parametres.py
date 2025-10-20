import turtle
def pointillesH (a,b,h1,ep1,coul1,h2,ep2,coul2):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.width(ep1)
    turtle.color(coul1)
    turtle.goto(a+h1,b)
    turtle.width(ep2);turtle.color(coul2);turtle.goto(a+h1+h2,b)
    turtle.width(ep1);turtle.color(coul1);turtle.goto(a+2*h1+h2,b)
    turtle.width(ep2);turtle.color(coul2);turtle.goto(a+2*h1+2*h2,b) 

#def pointillesV (a,b,h1,ep1,coul1,h2,ep2,coul2):
#    turtle.penup()
#    turtle.goto(a,b)
#    turtle.pendown()
#    turtle.width(ep1)
#    turtle.color(coul1)
#    turtle.goto(a+h1,b)
#    turtle.width(ep2);turtle.color(coul2);turtle.goto(b+h1+h2)
#    turtle.width(ep1);turtle.color(coul1);turtle.goto(a,b+h1+h2)
#    turtle.width(ep2);turtle.color(coul2);turtle.goto(a,b+2*h1+h2)
    
    
for k in range (1,11):
    coul1="blue"
    coul2="red"
    pointillesH(0,20*k,20*k,k,coul1,20*k,k,coul2)

for k in range (1,11):
    coul1="gren"
    coul2="gold"
    pointillesH(-20*k,0,20,2,coul1,30,3,coul2)

