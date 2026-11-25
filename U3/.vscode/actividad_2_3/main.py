import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout
)
from tarjeta_tarea import TarjetaTarea

app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Mis tareas")

layout = QVBoxLayout(ventana)

# Crear las instancias del componente
tarea1 = TarjetaTarea(
    "Preparar presentación",
    "Crear las diapositivas del proyecto."
)

tarea2 = TarjetaTarea(
    "Revisar documentación",
    "Comprobar los documentos antes de entregar.",
    "Completada"
)

tarea3 = TarjetaTarea(
    "Preparar examen",
    "Resolver los ejercicios de repaso",
    "En progreso"
)

# Modificar las tarjetas con los métodos públicos
tarea1.set_titulo("Presentación de la UD3")
tarea1.set_descripcion("Preparar cinco diapositivas.")
tarea2.set_estado("En progreso")

# Actividad 2.3: cambiar el texto del botón solo en la segunda tarjeta
tarea2.set_texto_boton("Revisar tarea")

# Añadir las tarjetas a la ventana
layout.addWidget(tarea1)
layout.addWidget(tarea2)
layout.addWidget(tarea3)

ventana.resize(420, 450)
ventana.show()

sys.exit(app.exec())
