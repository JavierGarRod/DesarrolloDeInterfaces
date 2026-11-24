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
    # Este if controla el paso del diálogo a la ventana principal
    if login.exec() != QDialog.DialogCode.Accepted:
        sys.exit(0)  # cancelado o cerrado con la X: no se muestra nada

    ventana = Principal()
    ventana.showMaximized()
    sys.exit(app.exec())
