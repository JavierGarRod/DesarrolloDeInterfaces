import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

MODOS = ["Modo A", "Modo B"]


class DialogoModo(QDialog):
    """Diálogo para elegir el modo de funcionamiento."""

    def __init__(self, modo_actual, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Elegir modo")

        # Combo con los modos; se preselecciona el modo activo actual
        self.combo = QComboBox()
        self.combo.addItems(MODOS)
        if modo_actual in MODOS:
            self.combo.setCurrentText(modo_actual)

        # Botones con rol: el rol decide qué señal se emite
        botones = QDialogButtonBox()
        botones.addButton("Aceptar", QDialogButtonBox.ButtonRole.AcceptRole)
        botones.addButton("Cancelar", QDialogButtonBox.ButtonRole.RejectRole)
        botones.addButton("Ayuda", QDialogButtonBox.ButtonRole.HelpRole)

        botones.accepted.connect(self.accept)  # Aceptar -> cierra con Accepted
        botones.rejected.connect(self.reject)  # Cancelar -> cierra con Rejected
        botones.helpRequested.connect(self.mostrar_ayuda)  # Ayuda -> NO cierra

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Selecciona el modo de funcionamiento:"))
        layout.addWidget(self.combo)
        layout.addWidget(botones)

    def modo_seleccionado(self):
        """Devuelve el texto que hay ahora mismo en el combo."""
        return self.combo.currentText()

    @Slot()
    def mostrar_ayuda(self):
        # Mensaje modal sobre el diálogo; al cerrarlo, el diálogo sigue abierto
        QMessageBox.information(
            self,
            "Ayuda",
            "Modo A y Modo B son los dos modos de funcionamiento del programa.\n\n"
            "Aceptar aplica el modo elegido.\n"
            "Cancelar (o cerrar con la X) conserva el modo anterior.",
        )


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sin modo activado")
        self.resize(320, 120)

        self.modo_actual = None  # Ningún modo hasta que se acepte uno
        self.dialogo = None  # Referencia para que no se destruya con open()

        boton = QPushButton("Elegir modo")
        boton.clicked.connect(self.abrir_dialogo)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(boton)
        self.setCentralWidget(central)

    @Slot()
    def abrir_dialogo(self):
        self.dialogo = DialogoModo(self.modo_actual, self)
        # accepted solo se emite al aceptar; al cancelar o cerrar con la X
        # no se conecta nada, así que el modo anterior se conserva.
        self.dialogo.accepted.connect(self.modo_aceptado)
        # open() no bloquea: el resultado llega por señales
        self.dialogo.open()

    @Slot()
    def modo_aceptado(self):
        self.modo_actual = self.dialogo.modo_seleccionado()
        self.setWindowTitle(f"{self.modo_actual} activado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())