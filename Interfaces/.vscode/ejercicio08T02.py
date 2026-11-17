import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Widget central: selector numérico de participantes
        self.spin = QSpinBox()
        self.spin.setRange(1, 30)          # intervalo permitido: 1 a 30
        self.spin.setValue(15)             # valor inicial
        self.spin.setSuffix(" personas")   # sufijo mostrado junto al número

        # Se conecta DESPUÉS de fijar el valor inicial para que no se
        # registre en consola un cambio que no ha hecho el usuario.
        self.spin.valueChanged.connect(self.valor_cambiado)

        self.setCentralWidget(self.spin)

        # El título debe mostrar el número desde el inicio
        self.actualizar_titulo(self.spin.value())

    def actualizar_titulo(self, valor):
        self.setWindowTitle(f"Participantes: {valor}")

    @Slot(int)
    def valor_cambiado(self, valor):
        print(f"Número de participantes: {valor}")
        self.actualizar_titulo(valor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.resize(300, 80)
    ventana.show()
    sys.exit(app.exec())
