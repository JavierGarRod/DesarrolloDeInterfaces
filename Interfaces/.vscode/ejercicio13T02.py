import sys

from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):
    """Ventana principal: hereda de QMainWindow."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de proyectos")
        self.resize(720, 420)

        # QWidget que actúa como contenedor central de la ventana
        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        # QHBoxLayout: divide la ventana en dos zonas (izquierda | derecha)
        layout_principal = QHBoxLayout(contenedor)
        layout_principal.addLayout(self.crear_zona_navegacion())
        # El 1 es el factor de estiramiento: la zona de contenido se lleva
        # todo el espacio sobrante al cambiar el tamaño de la ventana
        layout_principal.addLayout(self.crear_zona_contenido(), 1)

    def crear_zona_navegacion(self):
        """Zona izquierda: tres botones de navegación en vertical."""
        layout = QVBoxLayout()

        self.boton_proyectos = QPushButton("Proyectos")
        self.boton_usuarios = QPushButton("Usuarios")
        self.boton_configuracion = QPushButton("Configuración")

        layout.addWidget(self.boton_proyectos)
        layout.addWidget(self.boton_usuarios)
        layout.addWidget(self.boton_configuracion)

        # Mantiene los botones agrupados en la parte superior
        layout.addStretch()
        return layout

    def crear_zona_contenido(self):
        """Zona derecha: formulario arriba y botones de acción abajo a la derecha."""
        layout = QVBoxLayout()

        # Formulario con QFormLayout (etiqueta + campo en cada fila)
        formulario = QFormLayout()
        formulario.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        self.campo_nombre = QLineEdit()
        self.campo_responsable = QLineEdit()
        formulario.addRow("Nombre del proyecto:", self.campo_nombre)
        formulario.addRow("Responsable:", self.campo_responsable)
        layout.addLayout(formulario)

        # Espacio elástico entre el formulario y los botones: los empuja hacia abajo
        layout.addStretch()

        # Fila de botones de acción
        fila_botones = QHBoxLayout()
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_guardar = QPushButton("Guardar")

        # Espacio elástico antes de los botones: los empuja hacia la derecha
        fila_botones.addStretch()
        fila_botones.addWidget(self.boton_cancelar)
        fila_botones.addWidget(self.boton_guardar)
        layout.addLayout(fila_botones)

        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
