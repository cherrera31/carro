'''
from carro import Carro
carro_1 = Carro("Chevrolet","Camaro",2015,"Amarillo")
carro_2 = Carro("Toyota", "Tacoma",2024,"Rojo")
print(carro_1.modelo)
print(carro_2)

from carro import Felino
felino_1 = Felino("amarillo", "peludo","de tamano mediano","edad:5","gato domestico")
felino_1.comer()
'''
from carro import Barcos

from turtle import*
p = Turtle()

''''
B_Carguero = Barcos("rojo","grande","1990","Barco Carguero")
B_Carguero.VP()
print ("B.Carguero :", B_Carguero.color, B_Carguero.tamano, B_Carguero.edad) 
for i in range (1):
#Barco
    p.color("black","orange")
    p.penup()
    p.goto(-100,-150)
    p.begin_fill()
    p.pendown()
    p.forward(200)
    p.left(60)
    p.forward(80)
    p.setheading(180)
    p.forward(280)
    p.left(120)
    p.forward(80)
    p.end_fill()
    p.backward(80)
    p.setheading(0)
    p.forward(140)
    p.left(90)
done()


B_Velero = Barcos("verde","chico","1999", "Barco Velero")
B_Velero.VA()
print ("B.Velero :", B_Velero.color, B_Velero.tamano, B_Velero.edad) 
for i in range (1):
#Barco
    p.color("black","orange")
    p.penup()
    p.goto(-100,-150)
    p.begin_fill()
    p.pendown()
    p.forward(200)
    p.left(60)
    p.forward(80)
    p.setheading(180)
    p.forward(280)
    p.left(120)
    p.forward(80)
    p.end_fill()
    p.backward(80)
    p.setheading(0)
    p.forward(140)
    p.left(90)

    #Draw the stick of the boat
    p.pensize(8)
    p.forward(125)
    p.backward(5)
    p.penup()

    #draw the white left wings of the boat
    p.pensize(2)
    p.pendown()
    p.left(130)
    p.forward(4)
    p.color("red")
    p.begin_fill()
    p.forward(165)
    p.setheading(0)
    p.forward(125)
    p.end_fill()
    p.penup()
    p.left(90)
    p.forward(108)
    p.right(90)
    p.forward(7)

   #draw the right white wing of the boat
    p.pensize(2)
    p.pendown()
    p.right(40)
    p.color("red")
    p.begin_fill()
    p.forward(168)
    p.setheading(180)
    p.forward(125)
    p.end_fill()
    p.penup()
done()
'''
B_Viajero = Barcos("azul","mediano","2000", "Barco Viajero")
B_Viajero.VP()
print ("B.Viajero :", B_Viajero.color, B_Viajero.tamano, B_Viajero.edad) 
#Barco
for i in range (1):
    p.color("black","orange")
    p.penup()
    p.goto(-100,-150)
    p.begin_fill()
    p.pendown()
    p.forward(200)
    p.left(60)
    p.forward(80)
    p.setheading(180)
    p.forward(280)
    p.left(120)
    p.forward(80)
    p.end_fill()
    p.backward(80)
    p.setheading(0)
    p.forward(140)
    p.left(90)
#cuadrado
    
    for i in range(4):
        p.forward(tamano)
        p.right(90)
        p.end_fill()
done()

'''
from turtle import*
p = Turtle()
#colores = ["red", "purple", "orange", "blue", "green", "yellow"]
for i in range (1):
    p.color("black","orange")
    p.penup()
    p.goto(-100,-150)
    p.begin_fill()
    p.pendown()
    p.forward(200)
    p.left(60)
    p.forward(80)
    p.setheading(180)
    p.forward(280)
    p.left(120)
    p.forward(80)
    p.end_fill()
    p.backward(80)
    p.setheading(0)
    p.forward(140)
    p.left(90)
done()
'''