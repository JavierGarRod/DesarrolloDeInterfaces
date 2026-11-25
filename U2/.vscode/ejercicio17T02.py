import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QDockWidget,
    QLabel,
    QMainWindow,
    QStyle,
    QTextEdit,
    QToolBar,
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad 17 - Espacio de trabajo con paneles")
        self.resize(900, 600)

        # Requisito 1: widget central
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Área central de trabajo")
        self.setCentralWidget(self.editor)

        self.crear_paneles()
        self.crear_menu_ver()
        self.crear_barra_herramientas()

        # Requisito 7: mensaje en la barra de estado (sin tiempo límite)
        self.statusBar().showMessage("Espacio de trabajo preparado")

    # ------------------------------------------------------------------
    # Paneles acoplables (QDockWidget)
    # ------------------------------------------------------------------
    def crear_paneles(self):
        Caracteristica = QDockWidget.DockWidgetFeature

        # Requisito 2: «Notas», a la izquierda, sin movimiento, cierre
        # ni flotación.
        self.dock_notas = QDockWidget("Notas", self)
        self.dock_notas.setObjectName("dock_notas")
        self.dock_notas.setWidget(QTextEdit("Escribe aquí tus notas..."))
        self.dock_notas.setFeatures(Caracteristica.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_notas)

        # Requisito 3: «Estado», a la derecha, puede moverse y flotar
        # (pero no cerrarse).
        self.dock_estado = QDockWidget("Estado", self)
        self.dock_estado.setObjectName("dock_estado")
        etiqueta_estado = QLabel("Proyecto: en curso\nTareas pendientes: 3")
        etiqueta_estado.setAlignment(Qt.AlignmentFlag.AlignTop)
        etiqueta_estado.setMargin(8)
        self.dock_estado.setWidget(etiqueta_estado)
        self.dock_estado.setFeatures(
            Caracteristica.DockWidgetMovable | Caracteristica.DockWidgetFloatable
        )
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_estado)

        # Requisito 4: «Ayuda», en la parte inferior, puede moverse,
        # flotar y cerrarse.
        self.dock_ayuda = QDockWidget("Ayuda", self)
        self.dock_ayuda.setObjectName("dock_ayuda")
        etiqueta_ayuda = QLabel(
            "Usa el menú Ver para mostrar u ocultar los paneles.\n"
            "Arrastra la barra de título de «Estado» o «Ayuda» para moverlos."
        )
        etiqueta_ayuda.setMargin(8)
        self.dock_ayuda.setWidget(etiqueta_ayuda)
        self.dock_ayuda.setFeatures(
            Caracteristica.DockWidgetMovable
            | Caracteristica.DockWidgetFloatable
            | Caracteristica.DockWidgetClosable
        )
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dock_ayuda)

        self.paneles = [self.dock_notas, self.dock_estado, self.dock_ayuda]

    # ------------------------------------------------------------------
    # Menú Ver
    # ------------------------------------------------------------------
    def crear_menu_ver(self):
        menu_ver = self.menuBar().addMenu("&Ver")
        # Requisito 5: toggleViewAction() devuelve una QAction «marcable»
        # que ya está conectada al panel: mostrarla/ocultarla y mantener
        # la marca sincronizada es automático (también cuando el usuario
        # cierra el panel con su propio botón).
        for panel in self.paneles:
            menu_ver.addAction(panel.toggleViewAction())

    # ------------------------------------------------------------------
    # Barra de herramientas
    # ------------------------------------------------------------------
    def crear_barra_herramientas(self):
        # Requisito 6: una barra de herramientas con una acción.
        icono = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarNormalButton)
        self.accion_mostrar_todos = QAction(icono, "Mostrar todos los paneles", self)
        self.accion_mostrar_todos.setShortcut(QKeySequence("Ctrl+Shift+P"))
        self.accion_mostrar_todos.setStatusTip("Vuelve a mostrar los paneles ocultos")
        self.accion_mostrar_todos.triggered.connect(self.mostrar_todos_los_paneles)

        barra = QToolBar("Barra principal", self)
        barra.setMovable(False)
        barra.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        barra.addAction(self.accion_mostrar_todos)
        self.addToolBar(barra)

    @Slot()
    def mostrar_todos_los_paneles(self):
        for panel in self.paneles:
            panel.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
