import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QDial, QMainWindow


class VentanaVolumen(QMainWindow):
    """Ventana principal con el regulador de volumen en forma de dial."""

    def __init__(self):
        super().__init__()

        # QDial como widget central
        self.dial = QDial()
        self.dial.setRange(0, 100)         # intervalo entre 0 y 100
        self.dial.setValue(50)             # valor inicial
        self.dial.setNotchesVisible(True)  # muescas alrededor del dial
        self.setCentralWidget(self.dial)

        # Título correcto desde el inicio (setValue(50) se hizo antes de conectar la señal)
        self.actualizar_titulo(self.dial.value())

        # Cada cambio de valor llama al método receptor
        self.dial.valueChanged.connect(self.volumen_cambiado)

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
    ventana.resize(250, 250)
    ventana.show()
    sys.exit(app.exec())
