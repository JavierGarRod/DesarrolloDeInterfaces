import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStyle,
    QToolBar,
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titulo_original = "Actividad 15 - Acciones sincronizadas"
        self.setWindowTitle(self.titulo_original)
        self.resize(560, 320)

        self.etiqueta_estado = QLabel("Acciones activadas")
        self.etiqueta_estado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.etiqueta_estado)

        # La barra de estado muestra la ayuda contextual (statusTip) al pasar
        # el ratón por encima de una acción del menú o de la barra.
        self.statusBar()

        self.crear_acciones()
        self.crear_menu()
        self.crear_barra_herramientas()

    # ------------------------------------------------------------------
    # Acciones: se crean UNA sola vez y se reutilizan en menú y barra
    # ------------------------------------------------------------------
    def crear_accion(self, texto, icono, atajo, ayuda, slot):
        accion = QAction(icono, texto, self)
        accion.setShortcut(QKeySequence(atajo))
        accion.setToolTip(f"{ayuda} ({atajo})")  # ayuda emergente
        accion.setStatusTip(ayuda)  # ayuda en la barra de estado
        accion.triggered.connect(slot)
        return accion

    def crear_acciones(self):
        estilo = self.style()  # iconos estándar disponibles en cualquier sistema
        sp = QStyle.StandardPixmap

        self.accion_mensaje = self.crear_accion(
            "Mostrar mensaje",
            estilo.standardIcon(sp.SP_MessageBoxInformation),
            "Ctrl+M",
            "Muestra un mensaje en la consola",
            self.mostrar_mensaje,
        )
        self.accion_titulo = self.crear_accion(
            "Cambiar título",
            estilo.standardIcon(sp.SP_FileDialogDetailedView),
            "Ctrl+L",
            "Cambia el título de la ventana",
            self.cambiar_titulo,
        )
        self.accion_desactivar = self.crear_accion(
            "Desactivar acciones",
            estilo.standardIcon(sp.SP_DialogCancelButton),
            "Ctrl+D",
            "Deshabilita «Mostrar mensaje» y «Cambiar título»",
            self.desactivar_acciones,
        )
        self.accion_reactivar = self.crear_accion(
            "Reactivar acciones",
            estilo.standardIcon(sp.SP_DialogApplyButton),
            "Ctrl+R",
            "Vuelve a habilitar «Mostrar mensaje» y «Cambiar título»",
            self.reactivar_acciones,
        )

        # Acciones que se activan y desactivan. «Reactivar acciones» NO está
        # en esta lista: nunca se deshabilita, así que siempre se puede volver
        # al estado inicial.
        self.acciones_controladas = [self.accion_mensaje, self.accion_titulo]

    def crear_menu(self):
        menu = self.menuBar().addMenu("&Acciones")
        menu.addAction(self.accion_mensaje)
        menu.addAction(self.accion_titulo)
        menu.addSeparator()
        menu.addAction(self.accion_desactivar)
        menu.addAction(self.accion_reactivar)

    def crear_barra_herramientas(self):
        barra = QToolBar("Barra principal", self)
        barra.setMovable(False)
        barra.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # Se añaden LAS MISMAS instancias de QAction que usa el menú.
        barra.addAction(self.accion_mensaje)
        barra.addAction(self.accion_titulo)
        barra.addSeparator()
        barra.addAction(self.accion_desactivar)
        barra.addAction(self.accion_reactivar)
        self.addToolBar(barra)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------
    @Slot()
    def mostrar_mensaje(self):
        print("Hola desde una acción compartida")

    @Slot()
    def cambiar_titulo(self):
        if self.windowTitle() == self.titulo_original:
            self.setWindowTitle("Título cambiado")
        else:
            self.setWindowTitle(self.titulo_original)

    @Slot()
    def desactivar_acciones(self):
        for accion in self.acciones_controladas:
            accion.setEnabled(False)
        self.etiqueta_estado.setText("Acciones desactivadas")

    @Slot()
    def reactivar_acciones(self):
        for accion in self.acciones_controladas:
            accion.setEnabled(True)
        self.etiqueta_estado.setText("Acciones activadas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
