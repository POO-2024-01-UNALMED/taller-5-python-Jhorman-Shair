class Zoologico:
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
    
    def getZonas(self):
        return self._zonas
    
    def agregarzonas(self,zona):
        self.getZonas().append(zona)
        
    def cantidadTotalAnimales(self):
        a=0
        for i in self.zonas:
            a+=i.cantidadAnimales()
        return a
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    
    def getZonas(self):
        return self._zonas
    
    def setZonas(self,zonas):
        self._zonas=zonas