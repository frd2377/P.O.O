class PrimeraClase:
    pass

objeto1 = PrimeraClase()
objeto2 = PrimeraClase()

class Persona:
    def __init__(self,nombre:str,apellido:str,genero:str):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero

estudiante1 = Persona('nombre1','apellido1','M')
estudiante2 = Persona('nombre2', 'apellido2', 'M')

class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print(f'Total employee {self.empCount}')
        
    def displayEmployee(self):
        print('name: ',self.name,'salary: ',self.salary)

empleado1 = Employee('nombre',1000)
empleado1.displayCount()
empleado1.displayEmployee()

empleado2 = Employee('nombre2',2000)
empleado2.displayCount()
empleado2.displayEmployee()

'''
Arbol,Iot,Cine,robot,animal,pelicula,coche
'''
class Arbol:
    def __init__(self,tipo,altura,edad):
        self.tipo = tipo
        self.altura = altura
        self.edad = edad
    def mostrarAltura(self):
        print(f'La altura de el arbol es: {self.altura}')
    def mostrarTipo(self):
        print(f'El tipo de arbol es: {self.tipo}')
    def mostrarEdad(self):
         print(f'La edad arbol es: {self.edad}')

class Iot:
    def __init__(self,uso,almacenamiento,velConexion):
        self.uso = uso
        self.almacenamiento = almacenamiento
        self.velConexion = velConexion
    def mostrarUso(self):
        print(f'Su uso es: {self.uso}')
    def mostrarAlmacenamiento(self):
        print(f'su almacenamiento: {self.almacenamiento}')
    def mostrarVelocidad(self):
        print(f'velocidad de coneccion  {self.velConexion}') 
    
class Cine :
    def __init__(self, nombre,horarios,boletos,salas,ubicacion):
        self.nombre=nombre
        self.horarios=horarios
        self.boletos=boletos
        self.salas=salas
        self.ubicacion 
        
    def mostrarNombreCine(self):
        print(f'el cine se llama: {self.nombre}')

cine1 = Cine('pedro', 19, 40, 20, 'quito')






