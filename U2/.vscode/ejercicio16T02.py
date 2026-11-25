import getpass
import platform
import sys

from PySide6.QtCore import Qt, QTimer, Slot
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
        self.setWindowTitle("Actividad 16 - Barra de estado")
        self.resize(640, 320)

        self.veces_mensaje = 0  # cuántas veces se ha mostrado el mensaje
        self.mostrando_a = True  # para alternar entre dos mensajes (ampliación)

        centro = QLabel("Usa el menú, la barra de herramientas o los atajos")
        centro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(centro)

        # Los indicadores se crean UNA sola vez y después solo se actualizan.
        self.crear_indicadores()
        self.crear_acciones()
        self.crear_menu()
        self.crear_barra_herramientas()
        self.crear_temporizador()

    # ------------------------------------------------------------------
    # Indicadores permanentes de la barra de estado
    # ------------------------------------------------------------------
    def crear_indicadores(self):
        self.etiqueta_so = QLabel("SO: (sin consultar)")
        self.etiqueta_usuario = QLabel(f"Usuario: {getpass.getuser()}")
        # addPermanentWidget los coloca a la derecha y no los borra
        # cuando aparece un mensaje temporal.
        self.statusBar().addPermanentWidget(self.etiqueta_so)
        self.statusBar().addPermanentWidget(self.etiqueta_usuario)

    @Slot()
    def actualizar_indicadores(self):
        # Se reutilizan las etiquetas existentes: setText, nunca un QLabel nuevo.
        self.etiqueta_so.setText(f"SO: {platform.system()}")
        self.etiqueta_usuario.setText(f"Usuario: {getpass.getuser()}")

    # ------------------------------------------------------------------
    # Acciones
    # ------------------------------------------------------------------
    def crear_accion(self, texto, icono, atajo, ayuda, slot):
        accion = QAction(icono, texto, self)
        accion.setShortcut(QKeySequence(atajo))
        accion.setToolTip(f"{ayuda} ({atajo})")
        accion.triggered.connect(slot)
        return accion

    def crear_acciones(self):
        estilo = self.style()
        sp = QStyle.StandardPixmap

        self.accion_mostrar = self.crear_accion(
            "Mostrar mensaje",
            estilo.standardIcon(sp.SP_MessageBoxInformation),
            "Ctrl+M",
            "Muestra un mensaje durante 3 segundos",
            self.mostrar_mensaje,
        )
        self.accion_borrar = self.crear_accion(
            "Borrar mensaje",
            estilo.standardIcon(sp.SP_DialogDiscardButton),
            "Ctrl+B",
            "Elimina el mensaje temporal",
            self.borrar_mensaje,
        )
        self.accion_so = self.crear_accion(
            "Mostrar sistema operativo",
            estilo.standardIcon(sp.SP_ComputerIcon),
            "Ctrl+O",
            "Muestra el nombre del sistema operativo",
            self.actualizar_indicadores,
        )

        # Ampliación: alternar mensajes con QTimer
        self.accion_iniciar = self.crear_accion(
            "Iniciar alternancia",
            estilo.standardIcon(sp.SP_MediaPlay),
            "Ctrl+I",
            "Alterna dos mensajes cada 1,5 segundos",
            self.iniciar_alternancia,
        )
        self.accion_detener = self.crear_accion(
            "Detener alternancia",
            estilo.standardIcon(sp.SP_MediaStop),
            "Ctrl+T",
            "Detiene el temporizador",
            self.detener_alternancia,
        )
        self.accion_detener.setEnabled(False)  # aún no hay nada que detener

    def crear_menu(self):
        menu = self.menuBar().addMenu("&Información")
        menu.addAction(self.accion_mostrar)
        menu.addAction(self.accion_borrar)
        menu.addAction(self.accion_so)
        menu.addSeparator()
        menu.addAction(self.accion_iniciar)
        menu.addAction(self.accion_detener)

    def crear_barra_herramientas(self):
        barra = QToolBar("Barra principal", self)
        barra.setMovable(False)
        barra.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        barra.addAction(self.accion_mostrar)
        barra.addAction(self.accion_borrar)
        barra.addAction(self.accion_so)
        barra.addSeparator()
        barra.addAction(self.accion_iniciar)
        barra.addAction(self.accion_detener)
        self.addToolBar(barra)

    # ------------------------------------------------------------------
    # Mensajes temporales
    # ------------------------------------------------------------------
    @Slot()
    def mostrar_mensaje(self):
        self.veces_mensaje += 1
        # El segundo argumento son milisegundos: 3000 ms = 3 segundos.
        # Si se vuelve a llamar, el mensaje anterior se sustituye (no se apila).
        self.statusBar().showMessage(
            f"Mensaje temporal (mostrado {self.veces_mensaje} veces)", 3000
        )

    @Slot()
    def borrar_mensaje(self):
        self.statusBar().clearMessage()

    # ------------------------------------------------------------------
    # Ampliación: alternar dos mensajes con QTimer
    # ------------------------------------------------------------------
    def crear_temporizador(self):
        self.temporizador = QTimer(self)
        self.temporizador.setInterval(1500)  # milisegundos
        self.temporizador.timeout.connect(self.alternar_mensaje)

    @Slot()
    def alternar_mensaje(self):
        if self.mostrando_a:
            self.statusBar().showMessage("Mensaje A: tic")
        else:
            self.statusBar().showMessage("Mensaje B: tac")
        self.mostrando_a = not self.mostrando_a

    @Slot()
    def iniciar_alternancia(self):
        if not self.temporizador.isActive():  # evita arrancarlo dos veces
            self.temporizador.start()
            self.alternar_mensaje()  # primer mensaje sin esperar al primer tic
        self.accion_iniciar.setEnabled(False)
        self.accion_detener.setEnabled(True)

    @Slot()
    def detener_alternancia(self):
        self.temporizador.stop()
        self.statusBar().showMessage("Alternancia detenida", 2000)
        self.accion_iniciar.setEnabled(True)
        self.accion_detener.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
