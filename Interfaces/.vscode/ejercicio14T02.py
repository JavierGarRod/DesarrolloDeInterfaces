import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titulo_original = "Actividad 14 - Menú Archivo"
        self.setWindowTitle(self.titulo_original)
        self.resize(480, 300)

        self.crear_acciones()
        self.crear_menu()

    def crear_acciones(self):
        # Acción 1: Mostrar mensaje (Ctrl+M)
        self.accion_mensaje = QAction("Mostrar mensaje", self)
        self.accion_mensaje.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_mensaje.triggered.connect(self.mostrar_mensaje)

        # Acción 2: Cambiar título (Ctrl+L)
        self.accion_titulo = QAction("Cambiar título", self)
        self.accion_titulo.setShortcut(QKeySequence("Ctrl+L"))
        self.accion_titulo.triggered.connect(self.cambiar_titulo)

        # Acción 3: Salir (Ctrl+Q)
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut(QKeySequence("Ctrl+Q"))
        self.accion_salir.triggered.connect(self.salir)

    def crear_menu(self):
        menu_archivo = self.menuBar().addMenu("&Archivo")
        menu_archivo.addAction(self.accion_mensaje)
        menu_archivo.addAction(self.accion_titulo)
        menu_archivo.addSeparator()  # separador antes de «Salir»
        menu_archivo.addAction(self.accion_salir)

    @Slot()
    def mostrar_mensaje(self):
        print("Hola desde el menú")

    @Slot()
    def cambiar_titulo(self):
        # Alterna entre el título original y uno nuevo para poder
        # comprobar el cambio varias veces seguidas.
        if self.windowTitle() == self.titulo_original:
            self.setWindowTitle("Título cambiado desde el menú")
        else:
            self.setWindowTitle(self.titulo_original)

    @Slot()
    def salir(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())