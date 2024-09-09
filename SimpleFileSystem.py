import os

class SimpleFileSystem:
    def crear_archivo(self, ruta, contenido):
        try:
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)
            print(f"Archivo '{ruta}' creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def leer_archivo(self, ruta):
        try:
            if os.path.exists(ruta):
                with open(ruta, 'r') as archivo:
                    contenido = archivo.read()
                return contenido
            else:
                print(f"El archivo '{ruta}' no existe.")
                return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    def escribir_archivo(self, ruta, contenido_adicional):
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido_adicional + '\n')
            print(f"Contenido agregado al archivo '{ruta}'.")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def eliminar_archivo(self, ruta):
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
                print(f"Archivo '{ruta}' eliminado exitosamente.")
            else:
                print(f"El archivo '{ruta}' no existe.")
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")