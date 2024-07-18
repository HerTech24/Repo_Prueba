import csv

def procesar_lista_estudiantes():
    estudiantes = []
    try:
        with open('ListaCurso5B.csv', 'r', newline='') as curso5B:
            lector_csv = csv.DictReader(curso5B)
            for fila in lector_csv:
                fila['Nota 1'] = float(fila['Nota 1'])
                fila['Nota 2'] = float(fila['Nota 2'])
                estudiantes.append(fila)
    except FileNotFoundError:
        print("Archivo no encontrado. Asegúrese de que el archivo 'ListaCurso5B.csv' exista.")
    except Exception as e:
        print(f"Error al procesar la lista de estudiantes: {e}")
    return estudiantes

def guardar_estudiantes(estudiantes):
    try:
        # Verificar si alguno de los estudiantes tiene el campo 'Promedio'
        fieldnames = ["Rut", "Nombre", "Nota 1", "Nota 2"]
        if 'Promedio' in estudiantes[0]:
            fieldnames.append('Promedio')
        
        with open('ListaCurso5B.csv', 'w', newline='') as curso5B:
            writer = csv.DictWriter(curso5B, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(estudiantes)
    except PermissionError:
        print("Permiso denegado. Asegúrese de que el archivo no esté siendo utilizado por otro programa.")
    except Exception as e:
        print(f"Error al guardar los estudiantes: {e}")

def registrar_estudiante(estudiantes):
    rut = input("Ingrese el Rut del estudiante: ").strip()
    
    # Verificar si el estudiante ya está registrado
    for estudiante in estudiantes:
        if estudiante["Rut"] == rut:
            print("El estudiante con este Rut ya está registrado.")
            return
    
    nombre = input("Ingrese el Nombre del estudiante: ").strip()
    nota_1 = float(input("Ingrese la Nota 1 del estudiante: ").strip())
    nota_2 = float(input("Ingrese la Nota 2 del estudiante: ").strip())
    
    estudiante = {
        'Rut': rut,
        'Nombre': nombre,
        'Nota 1': nota_1,
        'Nota 2': nota_2
    }
    
    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes)
    print("Estudiante registrado exitosamente.")

def modificar_nota(estudiantes):
    rut = input("Ingrese el Rut del Estudiante: ").strip()
    for estudiante in estudiantes:
        if estudiante["Rut"] == rut:
            nota_a_modificar = input("Elija la nota que desea modificar (Nota 1/Nota 2): ").strip()
            if nota_a_modificar in ["Nota 1", "Nota 2"]:
                nueva_nota = float(input(f"Ingrese la nueva {nota_a_modificar}: ").strip())
                estudiante[nota_a_modificar] = nueva_nota
                guardar_estudiantes(estudiantes)
                print("Nota modificada exitosamente.")
                return
            else:
                print("Opción Inválida. Intente nuevamente.")
                return
    print("Estudiante no encontrado.")

def eliminar_estudiante(estudiantes):
    rut = input("Ingrese el Rut del estudiante a eliminar: ").strip()
    estudiante_a_eliminar = None
    for estudiante in estudiantes:
        if estudiante['Rut'] == rut:
            estudiante_a_eliminar = estudiante
            break
    
    if estudiante_a_eliminar:
        confirmacion = input(f"¿Está seguro de eliminar a {estudiante_a_eliminar['Nombre']}? (s/n): ").strip().lower()
        if confirmacion == 's':
            estudiantes.remove(estudiante_a_eliminar)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado exitosamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("Estudiante no encontrado.")
    return estudiantes

def generar_promedio(estudiantes):
    for estudiante in estudiantes:
        promedio = (estudiante['Nota 1'] + estudiante['Nota 2']) / 2
        estudiante['Promedio'] = promedio
    guardar_estudiantes(estudiantes)
    print("Promedios generados correctamente.")

def generar_acta_cierre(estudiantes, filename='ActaCierre.csv'):
    try:
        with open(filename, 'w', newline='') as curso5B:
            fieldnames = ['Rut', 'Nombre', 'Nota 1', 'Nota 2', 'Promedio']
            escritor = csv.DictWriter(curso5B, fieldnames=fieldnames)
            escritor.writeheader()
            for estudiante in estudiantes:
                escritor.writerow(estudiante)
        print("Acta de cierre de curso generada correctamente.")
    except Exception as e:
        print(f"Error al generar el acta de cierre de curso: {e}")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Procesar lista de estudiantes")
    print("2. Registrar estudiante")
    print("3. Modificar nota")
    print("4. Eliminar estudiante")
    print("5. Generar promedio de notas")
    print("6. Generar acta de cierre de curso")
    print("7. Salir")

def main():
    estudiantes = procesar_lista_estudiantes()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            estudiantes = procesar_lista_estudiantes()
            print("Lista de estudiantes procesada.")
        elif opcion == '2':
            registrar_estudiante(estudiantes)
        elif opcion == '3':
            modificar_nota(estudiantes)
        elif opcion == '4':
            estudiantes = eliminar_estudiante(estudiantes)
        elif opcion == '5':
            generar_promedio(estudiantes)
        elif opcion == '6':
            generar_acta_cierre(estudiantes)
        elif opcion == '7':
            guardar_estudiantes(estudiantes)
            print("Datos guardados. Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
