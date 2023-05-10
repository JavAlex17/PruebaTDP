import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        
    
    def guardar_mascota(self):
        global lista_mascotas
        nombre = self.nombre.text()
        especie = self.especie.text()
        edad = self.edad.text()
        peso = self.peso.text()
        m = Mascota(nombre,especie,edad,peso)
        lista_mascotas.append(m)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    lista_mascotas = []
    
    vista = Ventana()
    vista.show()
    app.exec()