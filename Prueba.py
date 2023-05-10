#Nombre: Javiera Cabezas

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QStackedLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QTableWidget, QTableWidgetItem 
from PyQt6.QtGui import QPixmap

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1 Sección Practica Prueba Individual")
        self.resize(600, 500)
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        self.layout_intermedio = QStackedLayout()
        layout3 = QHBoxLayout()
        
        
        
        self.label_Encabezado = QLabel("Nombre Usuario")
        layout2.addWidget(self.label_Encabezado)
        layout.addLayout(layout2)
        
        self.label2 = QLabel("")
        self.layout_intermedio.addWidget(self.label2)
        
        #caja_izq = QVBoxLayout()
        #self.labelcajaizq = QLabel("Imagen")
        #caja_izq.addWidget(self.labelcajaizq)
        #layout_intermedio.addWidget(caja_izq)
        
        imagen = QPixmap()
        labelimg = QLabel()
        labelimg.setPixmap(imagen)
        self.layout_intermedio.addWidget(labelimg)
        
        
        self.tabla = QTableWidget(6, 2)
        num = 0
        item = QTableWidgetItem('Atributo')
        self.tabla.setItem(0, num, item)
  
            
        self.layout_intermedio.addWidget(self.tabla)
        layout.addLayout(self.layout_intermedio)
        
        boton1 = QPushButton("OK")
        boton1.setFixedSize(150, 40)
        layout3.addWidget(boton1)
        layout.addLayout(layout3)
        
        
        
        
        
        ventana = QWidget()
        ventana.setLayout(layout)
        self.setCentralWidget(ventana)
        
        
        








if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    
    app.exec()