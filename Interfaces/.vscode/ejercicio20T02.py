import sys
from pathlib import Path

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication, QColorDialog, QFileDialog, QFontDialog, QHBoxLayout,
    QMainWindow, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget,
)


class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor")
        self.color_fondo = QColor("white")

        self.texto = QTextEdit()
        self.setCentralWidget(QWidget())
        layout = QVBoxLayout(self.centralWidget())

        botones = QHBoxLayout()
        for titulo, accion in (
            ("Abrir", self.abrir),
            ("Guardar", self.guardar),
            ("Color de fondo", self.cambiar_color),
            ("Fuente", self.cambiar_fuente),
        ):
            boton = QPushButton(titulo)
            boton.clicked.connect(accion)
            botones.addWidget(boton)

        layout.addLayout(botones)
        layout.addWidget(self.texto)

        self.statusBar().showMessage("Listo")
        self.aplicar_color(self.color_fondo)
        self.resize(700, 500)

    # ---------- Archivos ----------
    def abrir(self):
        nombre, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", "", "Texto (*.txt);;Todos los archivos (*)"
        )
        if not nombre:  # el usuario canceló
            return
        ruta = Path(nombre)
        try:
            contenido = ruta.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            QMessageBox.warning(self, "Error", f"No se pudo leer el archivo:\n{e}")
            return
        self.texto.setPlainText(contenido)
        self.statusBar().showMessage(f"Abierto: {ruta}", 4000)

    def guardar(self):
        nombre, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Texto (*.txt);;Todos los archivos (*)"
        )
        if not nombre:  # el usuario canceló
            return
        ruta = Path(nombre)
        try:
            ruta.write_text(self.texto.toPlainText(), encoding="utf-8")
        except OSError as e:
            QMessageBox.warning(self, "Error", f"No se pudo guardar:\n{e}")
            return
        self.statusBar().showMessage(f"Guardado correctamente en {ruta}", 4000)

    # ---------- Preferencias visuales ----------
    def aplicar_color(self, fondo: QColor):
        # Luminancia percibida -> texto negro o blanco para mantener contraste
        luminancia = 0.299 * fondo.red() + 0.587 * fondo.green() + 0.114 * fondo.blue()
        texto = "black" if luminancia > 128 else "white"
        self.texto.setStyleSheet(
            f"QTextEdit {{ background-color: {fondo.name()}; color: {texto}; }}"
        )
        self.color_fondo = fondo

    def cambiar_color(self):
        color = QColorDialog.getColor(self.color_fondo, self, "Color de fondo")
        if not color.isValid():  # cancelado
            return
        self.aplicar_color(color)
        self.statusBar().showMessage(f"Color de fondo: {color.name()}", 4000)

    def cambiar_fuente(self):
        fuente, aceptado = QFontDialog.getFont(self.texto.font(), self, "Fuente")
        if not aceptado:  # cancelado
            return
        self.texto.setFont(fuente)
        self.statusBar().showMessage(
            f"Fuente: {fuente.family()} {fuente.pointSize()} pt", 4000
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Editor()
    ventana.show()
    sys.exit(app.exec())
