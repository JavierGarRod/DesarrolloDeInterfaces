import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class VentanaProgreso(QMainWindow):
    """Ventana principal con el deslizador y la barra de progreso."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de progreso")

        # Deslizador horizontal de 0 a 100, inicialmente en 0
        self.deslizador = QSlider(Qt.Orientation.Horizontal)
        self.deslizador.setRange(0, 100)
        self.deslizador.setValue(0)

        # Barra de progreso con el mismo intervalo, inicialmente en 0
        self.progreso = QProgressBar()
        self.progreso.setRange(0, 100)
        self.progreso.setValue(0)
        # %p se sustituye por el porcentaje completado: "Progreso: 40 %"
        self.progreso.setFormat("Progreso: %p %")

        # Conexión directa señal -> ranura: el valor del deslizador pasa tal cual a la barra
        self.deslizador.valueChanged.connect(self.progreso.setValue)

        # Se colocan los dos widgets en vertical (fragmento facilitado en el enunciado)
        central = QWidget()
        layout = QVBoxLayout(central)

        layout.addWidget(self.deslizador)
        layout.addWidget(self.progreso)

        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaProgreso()
    ventana.resize(400, 100)
    ventana.show()
    sys.exit(app.exec())
