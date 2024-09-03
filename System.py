import os

class SimpleFileSystem:
    def crear_archivo(self, ruta, contenido):
        try:
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)
            print("Archivo creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def leer_archivo(self, ruta):
        try:
            if os.path.exists(ruta):
                with open(ruta, 'r') as archivo:
                    contenido = archivo.read()
                print("Contenido del archivo:")
                print(contenido)
            else:
                print("El archivo no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def escribir_archivo(self, ruta, contenido_adicional):
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido_adicional + '\n')
            print("Contenido agregado exitosamente.")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def eliminar_archivo(self, ruta):
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
                print("Archivo eliminado exitosamente.")
            else:
                print("El archivo no existe.")
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")

    def listar_archivos(self, directorio):
        try:
            if os.path.isdir(directorio):
                archivos = os.listdir(directorio)
                print("Archivos en el directorio:")
                for archivo in archivos:
                    print(archivo)
            else:
                print("El directorio no existe.")
        except Exception as e:
            print(f"Error al listar archivos: {e}")

if __name__ == "__main__":
    sistema_de_archivos = SimpleFileSystem()

    ruta_archivo = "miArchivo.txt"
    directorio = "."  # Directorio actual

    # Crear un archivo
    sistema_de_archivos.crear_archivo(ruta_archivo, "Este es el contenido inicial del archivo.")

    # Leer el archivo
    sistema_de_archivos.leer_archivo(ruta_archivo)

    # Escribir contenido adicional al archivo
    sistema_de_archivos.escribir_archivo(ruta_archivo, "Este es contenido adicional.")

    # Leer el archivo nuevamente
    sistema_de_archivos.leer_archivo(ruta_archivo)

    # Listar archivos en el directorio actual
    sistema_de_archivos.listar_archivos(directorio)

    # Eliminar el archivo
    sistema_de_archivos.eliminar_archivo(ruta_archivo)
