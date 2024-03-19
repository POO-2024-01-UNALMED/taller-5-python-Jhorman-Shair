from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave.agregarListado(self)
        
    def agregarListado(cls,a):
        cls.listado.append(a)
    
    def cantidadPeces(cls):
        return (len(cls.listado))
    
    def crearHalcon(cls,nombre,edad,genero):
        halcon=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones+=1
        Ave.agregarlistado(halcon)
        return halcon
    
    def crearAguila(cls,nombre,edad,genero):
        aguila=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas+=1
        Ave.agregarlistado(aguila)
        return aguila
    
    def getColorPlumas(self):
        return self._colorEscamas
    
    def setColorPlumas(self,colorEscamas):
        self._colorEscamas=colorEscamas