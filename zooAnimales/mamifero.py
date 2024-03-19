from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super.__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero.agregarListado(self)
        
    def agregarListado(cls,a):
        cls.listado.append(a)
    
    def cantidadMamiferos(cls):
        return (len(cls.listado))
    
    def crearCaballo(cls,nombre,edad,genero):
        caballo=Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos+=1
        Mamifero.agregarlistado(caballo)
        return caballo
    
    def crearLeon(cls,nombre,edad,genero):
        leon=Mamifero(nombre,edad,"selva",genero,True,4)
        cls.leones+=1
        Mamifero.agregarlistado(leon)
        return leon
    
    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self,pelaje):
        self._pelaje=pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self,patas):
        self._patas=patas