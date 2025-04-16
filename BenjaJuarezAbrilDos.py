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
        numero = input("Número de la tarea a marcar como completada: ")
        if numero.isdigit():
            numero = int(numero)
            if 1 <= numero <= len(tareas):
                tareas[numero - 1]["completada"] = True  # Marca la tarea como completada
                print("Tarea marcada como completada.")
            else:
                print("Número fuera de rango.")
        else:
            print("Por favor, ingresa un número válido.")
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
