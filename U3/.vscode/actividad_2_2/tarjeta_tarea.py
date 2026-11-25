from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)


class TarjetaTarea(QWidget):
    def __init__(self, titulo, descripcion, estado="Pendiente"):
        super().__init__()

        # Crear los widgets
        self.lbl_titulo = QLabel(titulo)
        self.lbl_descripcion = QLabel(descripcion)
        self.lbl_descripcion.setWordWrap(True)
        self.lbl_estado = QLabel(estado)
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
