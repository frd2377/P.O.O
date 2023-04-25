#FRD
class Animal:
    def hablar(self):
        print('Haciendo ruido')

class Perro(Animal):      
    def hablar(self):
        super().hablar()
        print('Ladrando...')
        
class Gato(Animal):      
    def hablar(self):
        super().hablar()
        print('Maullando...')
        
'''mi_perro = Perro()
mi_perro.hablar()

gato = Gato()
gato.hablar()'''

class Robot:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    def saludar(self):
        print('Robot saludando...')

class RobotAsistente(Robot):
    def __init__(self, nombre, color,tareas):
        super().__init__(nombre, color)
        self.tareas = tareas
    def saludar(self):
        print('Soy un robot asistente...')
    def realizar_tareas(self):
        print(f'Realizando tareas: {self.tareas}')

'''robot1 = Robot('Robots1', 'azul')
robot1.saludar()

robot2 = RobotAsistente('Asistant robot', 'negro', ['limpiar','ayudar'])
robot2.realizar_tareas()
robot2.saludar()'''

class RobotLuchador(Robot):
    def __init__(self, nombre, color,tipo_arma):
        super().__init__(nombre, color)
        self.tipo_arma = tipo_arma
    def saludar(self):
        print('Robot pelador saludando...')
    def pelear(self):
        print(f'Robot pelador lanzando un ataque con la {self.tipo_arma}')

'''robot3 = RobotLuchador('robotP3000', 'plateado', 'cierra')
robot3.saludar()
robot3.pelear()'''

class Vehiculo:
    def __init__(self,velecidad,posicion,direccion):
        self.velecidad = velecidad
        self.posicion = posicion
        self.direccion = direccion
        
    def moverse(self):
        print('El vehiculo esta en movimiento')
    def saber_velocidad(self):
        print(f'El vehiculo tiene una velocidad de {self.velecidad} km/h')
    def saber_posicion(self):
        print(f'El vehiculo esta en la posicion {self.posicion}')
    def tipo_direccion(self):
        print(f'El tipo de direccion es {self.direccion}')
        
class Coches(Vehiculo):
    def __init__(self, velecidad, posicion, direccion,num_ruedas):
        super().__init__(velecidad, posicion, direccion)
        self.num_ruedas = num_ruedas
    
    def conducir(self):
        print('El auto esta siendo conducido...')

# forma de control y acelerar
class Moto(Vehiculo):
    def __init__(self, velecidad, posicion, direccion,forma_control):
        super().__init__(velecidad, posicion, direccion)
        self.forma_control = forma_control
    
    def acelerar(self):
        print('La moto esta siendo acelerada...')
        
    def tipo_control(self):
        print(f'El tipo de control es {self.forma_control}')
        
print('--MOTOS--')
moto1 = Moto(100, 10, 'manual', 'automatico')
moto1.moverse()
moto1.saber_velocidad()
moto1.acelerar()
moto1.tipo_control()
print('\n--Carros--')
carro1 = Coches(200, 50, 'automatica', 4)
carro1.moverse()
carro1.saber_velocidad()
carro1.conducir()        
        







