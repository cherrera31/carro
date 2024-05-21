'''
class Carro: # "clase" siempre en minusculas y el nombre siempre en mayuscula
    llantas = 4 #Variable de clase
    def __init__(self,marca,modelo,ano,color):#self palabra reservada
     self.marca = marca #variable de instancia
     self.modelo = modelo
     self.ano = ano
     self.color = color
    def manejar(self):
       print("Este auto"+self.marca+"esta siendo manejado")
    def detener(self):
       print("Este auto"+self.marca+ "se ha detenido")

#fam de felinos
class Felino:
   def __init__(self,color,pelo,tamano,edad,raza):
      self.color = color
      self.pelo = pelo
      self.tamano = tamano
      self.edad = edad
      self.raza = raza
   def ronronear(self):
      print("Este felino de raza:"+self.raza+"esta ronronenado")
   def atacar(self):
      print ("Este felino de raza:"+self.raza+self.pelo+"va a atacar")
   def comer(self):
      print("Este felino de raza:"+self.raza+"esta comiendo")
'''
#Barcos
class Barcos:
    def __init__(self,color, tamano, edad, nombre):
        self.color = color
        self.tamano = tamano
        self.edad = edad
        self.nombre = nombre
    def VP(self):
        print("Viajando por el Pacifico")
    def VA(self):
        print("Viajando por el Atlantico")
    
    