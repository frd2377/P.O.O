class Robot_Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
    
    def ver_status(self):
        if self.model.esta_encendido():
            return print(f'El robot esta encendido su posicion es {self.model.posicion_robot} y la posicion del brazo robotico es {self.model.posicion_brazo}\n')
        return print(f'El robot esta apagado su poscicion es {self.model.posicion_robot} y la posicion del brazo robotico es {self.model.posicion_brazo}\n')

    def encender_robot(self):
        if self.model.esta_encendido():
            return print(f'El robot esta encendido\n')
        self.model.encender()
        print('El robot esta encendiendose...')
        return print(f'Robot encendido\n')
    
    def apagar_robot(self):
        if not self.model.esta_encendido():
            return print(f'El robot esta apagado\n')
        self.model.apagar()
        print('El robot esta apagandose...')
        return print(f'Robot apagado\n')
    
    def mover_robot(self):
        if not self.model.esta_encendido():
            return print(f'El robot esta apagado\n')
        print('Ingrese las coordenadas a donde desea mover al robot: (x,y)')
        try:
            posicionx = float(input('x: '))
            posiciony = float(input('y: '))
            self.model.posicion_robot = [posicionx,posiciony]
        except:
            print('Ha ocurrido un error')
    
    def mover_brazo(self):
        if not self.model.esta_encendido():
            return print(f'El robot esta apagado\n')
        print('Ingrese las coordenadas a donde desea moverlo el brazo robotico: (x,y,z)')
        try:
            posicionx = float(input('x angulo de elevacion: '))
            posiciony = float(input('y angulo de giro: '))
            posicionz = float(input('z longitud: '))
            self.model.posicion_brazo = [posicionx,posiciony,posicionz]
        except:
            print('Ha ocurrido un error')

    def ver_posicion_brazo(self):
        return print(f'La posicion del brazo robotico es {self.model.posicion_brazo}\n')
    
    def ver_posicion_robot(self):
        return print(f'La posicion del robot es {self.model.posicion_robot}\n')











