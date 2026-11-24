import sys

from PySide6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMessageBox,
)


class Login(QDialog):
    USUARIO = "admin"
    CLAVE = "admin"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acceso")

        self.usuario = QLineEdit()
        self.clave = QLineEdit()
        self.clave.setEchoMode(QLineEdit.EchoMode.Password)

        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botones.button(QDialogButtonBox.StandardButton.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        botones.accepted.connect(self.comprobar)
        botones.rejected.connect(self.reject)

        layout = QFormLayout(self)
        layout.addRow("Usuario:", self.usuario)
        layout.addRow("Contraseña:", self.clave)
        layout.addRow(botones)

    def comprobar(self):
        if self.usuario.text() == self.USUARIO and self.clave.text() == self.CLAVE:
            self.accept()  # cierra con resultado Accepted
        else:
            QMessageBox.warning(self, "Acceso denegado", "Usuario o contraseña incorrectos.")
            self.clave.clear()
            self.clave.setFocus()  # el diálogo sigue abierto


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación principal")
        self.setCentralWidget(QLabel("Bienvenido, admin", alignment=0x84))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = Login()
    ventana = Principal()

    def abrir_principal():
        ventana.showMaximized()

    # Las señales sustituyen al valor devuelto por exec()
    login.accepted.connect(abrir_principal)  # acceso válido -> ventana principal
    login.rejected.connect(app.quit)         # cancelar o X -> termina el programa

    login.open()  # no bloqueante (modal respecto a la aplicación)
    sys.exit(app.exec())
