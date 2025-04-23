tareas = ["Limpiar la habitacion", "Hacer las tareas de la escuela", "Pasear al perro", "Comprar cartulina"]
def mostar_menu():
    print("Menu de opciones")
    print("1: Añadir una tarea")
    print("2: Ver todas las tareas")
    print("3: Marcar tarea como completada")
    print("4: Salir")

def añadir_tarea():
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)
    print("tarea añadida")

def ver_todas_las_tareas():
    if not tareas:
        print("No hay tareas todavía.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def marcar_completada():
    ver_todas_las_tareas()
    if tareas:
        try:
            numero = int(input("Número de la tarea a eliminar: "))
            if 1 <= numero <= len(tareas):
                tarea_eliminada = tareas.pop(numero - 1)
                print(f"Tarea completada y eliminada: {tarea_eliminada}")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Debes escribir un número.")
# --- Programa principal ---
while True:
    mostar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        añadir_tarea()
    elif opcion == "2":
        ver_todas_las_tareas()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta otra vez.")
