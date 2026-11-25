import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider


class VentanaVolumen(QMainWindow):
    """Ventana principal con el regulador de volumen."""

    def __init__(self):
        super().__init__()

        # QSlider horizontal como widget central
        self.deslizador = QSlider(Qt.Orientation.Horizontal)
        self.deslizador.setRange(0, 100)   # intervalo entre 0 y 100
        self.deslizador.setValue(50)       # valor inicial
        self.setCentralWidget(self.deslizador)

        # Título correcto desde el inicio (setValue(50) se hizo antes de conectar la señal)
        self.actualizar_titulo(self.deslizador.value())

        # Cada cambio de valor llama al método receptor
        self.deslizador.valueChanged.connect(self.volumen_cambiado)

    def actualizar_titulo(self, valor):
        self.setWindowTitle(f"Volumen: {valor} %")

    @Slot(int)
    def volumen_cambiado(self, valor):
        """Receptor de valueChanged: actualiza el título y registra el cambio en consola."""
        self.actualizar_titulo(valor)
        print(f"Volumen cambiado a {valor} %")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVolumen()
    ventana.resize(400, 60)
    ventana.show()
    sys.exit(app.exec())
