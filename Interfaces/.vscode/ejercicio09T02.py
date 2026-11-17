import sys

from PySide6.QtCore import QDate, Slot
from PySide6.QtWidgets import QApplication, QDateEdit, QMainWindow


class VentanaPrincipal(QMainWindow):
    FORMATO = "dd/MM/yyyy"  # en Qt el año de cuatro cifras es «yyyy»

    def __init__(self):
        super().__init__()

        # Widget central: selector de fecha de entrega
        self.fecha = QDateEdit()
        self.fecha.setDisplayFormat(self.FORMATO)   # formato dd/MM/aaaa
        self.fecha.setCalendarPopup(True)           # calendario desplegable
        self.fecha.setDate(QDate.currentDate())     # fecha actual del sistema

        # Se conecta después de fijar la fecha inicial
        self.fecha.dateChanged.connect(self.fecha_cambiada)

        self.setCentralWidget(self.fecha)

        # El título debe mostrar la fecha desde el inicio
        self.actualizar_titulo(self.fecha.date())

    def actualizar_titulo(self, fecha):
        self.setWindowTitle(f"Fecha de entrega: {fecha.toString(self.FORMATO)}")

    @Slot(QDate)
    def fecha_cambiada(self, fecha):
        print(f"Nueva fecha de entrega: {fecha.toString(self.FORMATO)}")
        self.actualizar_titulo(fecha)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.resize(300, 80)
    ventana.show()
    sys.exit(app.exec())
