import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QMainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Widget central: precio de inscripción del curso
        self.spin = QDoubleSpinBox()
        self.spin.setRange(0.00, 1000.00)  # intervalo de precios permitido
        self.spin.setDecimals(2)           # dos decimales
        self.spin.setSingleStep(5.00)      # incremento de 5 €
        self.spin.setValue(100.00)         # precio inicial
        self.spin.setSuffix(" €")

        self.spin.valueChanged.connect(self.valor_cambiado)

        self.setCentralWidget(self.spin)
        self.actualizar_titulo(self.spin.value())

    def actualizar_titulo(self, valor):
        self.setWindowTitle(f"Precio de inscripción: {valor:.2f} €")

    @Slot(float)
    def valor_cambiado(self, valor):
        print(f"Precio de inscripción: {valor:.2f} €")
        self.actualizar_titulo(valor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.resize(300, 80)
    ventana.show()
    sys.exit(app.exec())
