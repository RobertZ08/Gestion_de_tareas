def agregar_tarea():
    nombre = input("Tarea: ")
    tarea = {
        "nombre": nombre,
        "completada": False
    }
    tarea.append(tarea)