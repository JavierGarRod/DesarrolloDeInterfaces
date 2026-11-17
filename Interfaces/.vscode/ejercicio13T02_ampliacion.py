"""
Actividad 13 (ampliación). Una interfaz organizada por zonas con QStackedLayout
Archivo: ejercicio13T02_ampliacion.py

Igual que ejercicio13T02.py, pero la zona derecha es un QStackedLayout con dos páginas
que se alternan con los botones de navegación:
  - Página 0 (botón «Proyectos»): formulario con los botones Cancelar y Guardar.
  - Página 1 (botón «Usuarios»): una lista de usuarios de ejemplo.
El botón «Configuración» queda sin función, como en la versión base.
"""
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):
    """Ventana principal: hereda de QMainWindow."""

    # Posición de cada página dentro del QStackedLayout
    PAGINA_PROYECTOS = 0
    PAGINA_USUARIOS = 1

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

        self.pila = self.crear_zona_contenido()
        layout_principal.addLayout(self.pila, 1)

        # Los botones de navegación cambian la página visible
        self.boton_proyectos.clicked.connect(self.mostrar_proyectos)
        self.boton_usuarios.clicked.connect(self.mostrar_usuarios)

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
        """Zona derecha: QStackedLayout con las páginas de contenido."""
        pila = QStackedLayout()
        pila.addWidget(self.crear_pagina_proyectos())  # índice 0
        pila.addWidget(self.crear_pagina_usuarios())   # índice 1
        return pila

    def crear_pagina_proyectos(self):
        """Página 0: formulario y botones de acción abajo a la derecha."""
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        formulario = QFormLayout()
        formulario.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        self.campo_nombre = QLineEdit()
        self.campo_responsable = QLineEdit()
        formulario.addRow("Nombre del proyecto:", self.campo_nombre)
        formulario.addRow("Responsable:", self.campo_responsable)
        layout.addLayout(formulario)

        # Espacio elástico entre el formulario y los botones: los empuja hacia abajo
        layout.addStretch()

        fila_botones = QHBoxLayout()
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_guardar = QPushButton("Guardar")

        # Espacio elástico antes de los botones: los empuja hacia la derecha
        fila_botones.addStretch()
        fila_botones.addWidget(self.boton_cancelar)
        fila_botones.addWidget(self.boton_guardar)
        layout.addLayout(fila_botones)

        return pagina

    def crear_pagina_usuarios(self):
        """Página 1: lista de usuarios de ejemplo."""
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        layout.addWidget(QLabel("Usuarios del proyecto"))

        lista = QListWidget()
        lista.addItems(["Usuario 1", "Usuario 2", "Usuario 3"])
        layout.addWidget(lista)

        return pagina

    @Slot()
    def mostrar_proyectos(self):
        self.pila.setCurrentIndex(self.PAGINA_PROYECTOS)

    @Slot()
    def mostrar_usuarios(self):
        self.pila.setCurrentIndex(self.PAGINA_USUARIOS)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
