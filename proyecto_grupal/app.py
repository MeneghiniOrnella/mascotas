class mascota:
    nombre="a"
    hambre=0
    animo=0
    energia=0

def __init__(self,nombre,hambre,animo,energia):
    self.nombre=nombre
    self.hambre=hambre
    self.animo=animo
    self.energia=energia
def jugar(self):
    self.animo+=1
    self.energia-=1
def alimentar(self):
    self.animo+=1
    self.hambre-=1
def dormir(self):
    self.hambre+=1
    self.energia+=1
def pasear(self):
    self.animo-=1
    self.hambre+=1
    self.energia-=1
 
def __str__(self):
    return ("Nombre:%s Estado: Hambre:%d Animo:%d Energia:%d ") %(self.nombre,self.hambre,self.animo,self.energia)

# Programa Principal
t=mascota("mascota",10,10,10)
t.dormir()
t.jugar()
t.alimentar()
t.pasear()
print(t)
