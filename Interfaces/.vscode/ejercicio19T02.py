import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad 19")
        self.resize(320, 160)

        self.estado = "Pendiente"  # Estado de la tarea
        self.dialogo = None  # Referencia para que no se destruya con open()

        boton = QPushButton("Gestionar tarea")
        boton.clicked.connect(self.gestionar_tarea)

        self.etiqueta_estado = QLabel(f"Estado de la tarea: {self.estado}")
        self.etiqueta_resultado = QLabel("Resultado: -")

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(boton)
        layout.addWidget(self.etiqueta_estado)
        layout.addWidget(self.etiqueta_resultado)
        self.setCentralWidget(central)

    @Slot()
    def gestionar_tarea(self):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Gestionar tarea")
        dialogo.setIcon(QMessageBox.Icon.Question)
        dialogo.setText("¿Qué quieres hacer con la tarea?")

        # Botones personalizados con addButton(): cada uno con su rol
        self.btn_completar = dialogo.addButton(
            "Completar", QMessageBox.ButtonRole.AcceptRole
        )
        self.btn_posponer = dialogo.addButton(
            "Posponer", QMessageBox.ButtonRole.ActionRole
        )
        self.btn_mantener = dialogo.addButton(
            "Mantener sin cambios", QMessageBox.ButtonRole.RejectRole
        )

        # Es la opción de cancelación: Esc y la X de la ventana la activan
        dialogo.setEscapeButton(self.btn_mantener)
        dialogo.setDefaultButton(self.btn_mantener)  # Enter no cambia nada

        self.dialogo = dialogo
        dialogo.finished.connect(self.tarea_resuelta)
        dialogo.open()  # No bloquea: el resultado llega por señal

    @Slot(int)
    def tarea_resuelta(self, resultado):
        pulsado = self.dialogo.clickedButton()

        if pulsado is self.btn_completar:
            self.estado = "Completada"
            self.etiqueta_resultado.setText("Resultado: Tarea completada")
        elif pulsado is self.btn_posponer:
            self.estado = "Pospuesta"
            self.etiqueta_resultado.setText("Resultado: Tarea pospuesta")
        else:
            # «Mantener sin cambios», Esc o la X: el estado no se toca
            self.etiqueta_resultado.setText("Resultado: Sin cambios")

        self.etiqueta_estado.setText(f"Estado de la tarea: {self.estado}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())