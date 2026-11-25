from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)


class TarjetaTarea(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets
        self.lbl_titulo = QLabel("Estudiar Python")
        self.lbl_descripcion = QLabel(
            "Repasar las clases y los objetos"
        )
        self.lbl_descripcion.setWordWrap(True)
        self.lbl_estado = QLabel("Pendiente")
        self.btn_completar = QPushButton("Completar tarea")

        # Organizar el estado y el botón
        layout_inferior = QHBoxLayout()
        layout_inferior.addWidget(self.lbl_estado)
        layout_inferior.addStretch()
        layout_inferior.addWidget(self.btn_completar)

        # Organizar el contenido de la tarjeta
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.lbl_titulo)
        layout_principal.addWidget(self.lbl_descripcion)
        layout_principal.addLayout(layout_inferior)

        self.setLayout(layout_principal)
