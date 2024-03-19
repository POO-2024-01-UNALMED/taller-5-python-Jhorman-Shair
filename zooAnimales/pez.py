
from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super.__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=cantidadAletas
        Pez.agregarListado(self)
        
    def agregarListado(cls,a):
        cls.listado.append(a)
    
    def cantidadPeces(cls):
        return (len(cls.listado))
    
    def crearSalmon(cls,nombre,edad,genero):
        salmon=Pez(nombre,edad,"oceano",genero,"rojo",6)
        cls.salmones+=1
        Pez.agregarlistado(salmon)
        return salmon
    
    def crearBacalao(cls,nombre,edad,genero):
        bacalao=Pez(nombre,edad,"oceano",genero,"gris",6)
        cls.bacalaos+=1
        Pez.agregarlistado(bacalao)
        return bacalao
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,cantidadAletas):
        self._cantidadAletas=cantidadAletas