from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio.agregarListado(self)
        
    def agregarListado(cls,a):
        cls.listado.append(a)
    
    def cantidadPeces(cls):
        return (len(cls.listado))
    
    def crearRana(cls,nombre,edad,genero):
        rana=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
        Anfibio.agregarlistado(rana)
        return rana
    
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.aguilas+=1
        Anfibio.agregarlistado(salamandra)
        return salamandra
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso