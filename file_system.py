import os

class SimpleFileSystem:
    def __init__(self, directorio):
        self.directorio = directorio
        if not os.path.exists(directorio):
            os.makedirs(directorio)

    def crear_archivo(self, nombre_archivo, contenido):
        ruta = os.path.join(self.directorio, nombre_archivo)
        try:
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)
        except Exception as e:
            raise e

    def leer_archivo(self, nombre_archivo):
        ruta = os.path.join(self.directorio, nombre_archivo)
        try:
            if os.path.exists(ruta):
                with open(ruta, 'r') as archivo:
                    return archivo.read()
            else:
                raise FileNotFoundError("El archivo no existe.")
        except Exception as e:
            raise e

    def escribir_archivo(self, nombre_archivo, contenido_adicional):
        ruta = os.path.join(self.directorio, nombre_archivo)
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido_adicional + '\n')
        except Exception as e:
            raise e

    def eliminar_archivo(self, nombre_archivo):
        ruta = os.path.join(self.directorio, nombre_archivo)
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
            else:
                raise FileNotFoundError("El archivo no existe.")
        except Exception as e:
            raise e

    def listar_archivos(self):
        try:
            if os.path.isdir(self.directorio):
                return os.listdir(self.directorio)
            else:
                raise FileNotFoundError("El directorio no existe.")
        except Exception as e:
            raise e
