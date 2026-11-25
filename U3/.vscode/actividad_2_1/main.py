import sys
from PySide6.QtWidgets import QApplication
from tarjeta_tarea import TarjetaTarea

app = QApplication(sys.argv)

tarjeta = TarjetaTarea()
tarjeta.setWindowTitle("Mi primera tarjeta")
tarjeta.resize(360, 160)
tarjeta.show()

sys.exit(app.exec())
