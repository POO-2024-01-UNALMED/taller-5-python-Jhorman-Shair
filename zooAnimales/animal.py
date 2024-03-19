from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

class Animal:
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=[]
    def movimiento(self):
        return "desplazarse"
    
    def totalPorTipo(cls):
        return "Mamiferos: "+str(Mamifero.cantidadMamiferos())+"\n"+"Aves: "+str(Ave.cantidadAves())+"\n"+"Reptiles: "+str(Reptil.cantidadReptiles())+"\n"+"Peces: "+str(Pez.cantidadPeces())+"\n"+"Anfibios: "+str(Anfibio.cantidadAnfibios())
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad
        
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat=habitat
        
    def getGenero(self):
        return self._genero
    
    def setGenero(self,genero):
        self._genero=genero
        
    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona=zona
    
    def toString(self):
        if self._zona!=[]:
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self.habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona[0].getNombre()+", en el "+self._zona[0].getZoo().getNombre()
        else:
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self.habitat+" y mi genero es "+self._genero