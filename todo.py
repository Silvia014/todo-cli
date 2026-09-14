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


add_one_task("Revisar pedido de Miami")
add_one_task("Llamar al proveedor")
add_one_task("Preparar documentación")

print_list()

delete_task(2)

print("\nDespués de eliminar:")
print_list()