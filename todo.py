import csv
# este va a guardar temporalemente las tareas que se van a agregar a la lista de tareas
tasks = []
# primera función que agrega una tarea a la lista de tareas
def add_one_task(title):
    tasks.append(title)
# función para mostrar las tareas
def print_list():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
# eliminar una tarea de la lista de tareas
def delete_task(number_to_delete):
    tasks.pop(number_to_delete - 1)
# guardar las tareas en un archivo CSV
def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for task in tasks:
            writer.writerow([task])
# cargar las tareas desde un archivo CSV con task clear vaciamos la lista actual para evitar duplicados y luego leemos cada fila y recuperamos el titulo
def load_todos():
    tasks.clear()

    try:
        with open("todos.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    tasks.append(row[0])

    except FileNotFoundError:
        print("No existe el archivo todos.csv.")

# creamos un show menu para mostrar las opciones al usuario
def show_menu():
    print("\n===== TODO LIST =====")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Guardar tareas")
    print("5. Cargar tareas")
    print("6. Salir")
# creamos main para ejecutar el programa y mostrar el menu al usuario
def main():
    load_todos()

    while True:
        show_menu()

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            title = input("Título de la tarea: ").strip()
            add_one_task(title)

        elif option == "2":
            print_list()

        elif option == "3":
            number = int(input("Número de tarea a eliminar: "))
            delete_task(number)

        elif option == "4":
            save_todos()

        elif option == "5":
            load_todos()

        elif option == "6":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")
if __name__ == "__main__":
    main()
