# Función para escribir notas en un archivo
def write_notes(filename):
    # Abrimos el archivo en modo escritura
    with open(filename, 'w') as file:
        # Escribimos varias notas
        file.write("Nota 1: Completar el proyecto de matemáticas.\n")
        file.write("Nota 2: Reunión con de trabajo el lunes.\n")
        file.write("Nota 3: Comprar víveres para la semana.\n")
        file.write("Nota 4: Leer el codigo organico integral penal COIP.\n")
        file.write("Nota 5: Practicas en el poligono de tiro.\n")
        file.write("Nota 6: Actividd fisica.\n")

# Función para leer y mostrar notas de un archivo
def read_notes(filename):
    # Abrimos el archivo en modo lectura
    with open(filename, 'r') as file:
        # Leemos cada línea y la mostramos
        for line in file:
            print(line.strip())  # .strip() elimina saltos de línea y espacios

# Nombre del archivo
file_name = 'my_notes.txt'

# Escribimos notas en el archivo
write_notes(file_name)

# Leemos las notas desde el archivo
read_notes(file_name)