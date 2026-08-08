def listar_tareas():
    for tarea in tareas:
        print(
            tarea["nombre"],
            tarea["completada"]
        )