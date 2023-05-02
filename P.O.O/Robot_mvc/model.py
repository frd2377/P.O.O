class Robot:
    encendido = False

    def __init__(self,posicion_robot:list,posicion_brazo:list):
        self.posicion_robot = posicion_robot
        self.posicion_brazo = posicion_brazo

    def esta_encendido(self):
        return self.encendido

    def encender(self):
        self.encendido = True
        return self.encendido

    def apagar(self):
        self.encendido = False
        return self.encendido



















