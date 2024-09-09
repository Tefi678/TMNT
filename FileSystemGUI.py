import tkinter as tk
from tkinter import simpledialog, messagebox
from TMNT import SimpleFileSystem

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Archivos")

        # Cambiar color de fondo de la ventana principal
        self.root.configure(bg='#f0f0f0')

        # Crear sistema de archivos
        self.file_system = SimpleFileSystem()

        # Cargar imágenes
        self.img_crear = tk.PhotoImage(file="C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Crear_Archivos.png")  
        self.img_buscar = tk.PhotoImage(file="C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Buscar_Archivos.png") 
        self.img_eliminar = tk.PhotoImage(file="C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Eliminar_Archivos.png") 
        self.img_actualizar = tk.PhotoImage(file="C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Actualizar_Archivos.png")  
        self.img_salir = tk.PhotoImage(file="C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Salir.png")  

        # Crear los widgets con estilo mejorado y agregar imágenes
        self.create_widgets()

    def create_widgets(self):
        # Usar un frame para organizar mejor los botones
        frame = tk.Frame(self.root, bg='#f0f0f0')
        frame.pack(pady=20, padx=20)

        # Botón para crear archivo con imagen
        self.btn_crear = tk.Button(frame, text="Crear Archivo", image=self.img_crear, compound='left',
                                   command=self.crear_archivo, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'),
                                   relief='flat', padx=10, pady=5)
        self.btn_crear.grid(row=0, column=0, pady=10, sticky='ew')

        # Botón para buscar archivo con imagen
        self.btn_buscar = tk.Button(frame, text="Buscar Archivo", image=self.img_buscar, compound='left',
                                    command=self.buscar_archivo, bg='#2196F3', fg='white', font=('Helvetica', 12, 'bold'),
                                    relief='flat', padx=10, pady=5)
        self.btn_buscar.grid(row=1, column=0, pady=10, sticky='ew')

        # Botón para eliminar archivo con imagen
        self.btn_eliminar = tk.Button(frame, text="Eliminar Archivo", image=self.img_eliminar, compound='left',
                                      command=self.eliminar_archivo, bg='#F44336', fg='white', font=('Helvetica', 12, 'bold'),
                                      relief='flat', padx=10, pady=5)
        self.btn_eliminar.grid(row=2, column=0, pady=10, sticky='ew')

        # Botón para actualizar archivo con imagen
        self.btn_actualizar = tk.Button(frame, text="Actualizar Archivo", image=self.img_actualizar, compound='left',
                                        command=self.actualizar_archivo, bg='#FF9800', fg='white', font=('Helvetica', 12, 'bold'),
                                        relief='flat', padx=10, pady=5)
        self.btn_actualizar.grid(row=3, column=0, pady=10, sticky='ew')

        # Botón para salir con imagen
        self.btn_salir = tk.Button(frame, text="Salir", image=self.img_salir, compound='left',
                                   command=self.root.quit, bg='#9E9E9E', fg='white', font=('Helvetica', 12, 'bold'),
                                   relief='flat', padx=10, pady=5)
        self.btn_salir.grid(row=4, column=0, pady=10, sticky='ew')

    def crear_archivo(self):
        nombre_archivo = simpledialog.askstring("Crear Archivo", "Ingrese el nombre del archivo:")
        if nombre_archivo:
            contenido = simpledialog.askstring("Contenido del Archivo", "Ingrese el contenido del archivo:")
            self.file_system.crear_archivo(nombre_archivo, contenido)
            messagebox.showinfo("Archivo Creado", f"Archivo '{nombre_archivo}' creado exitosamente.")

    def buscar_archivo(self):
        nombre_archivo = simpledialog.askstring("Buscar Archivo", "Ingrese el nombre del archivo a buscar:")
        if nombre_archivo:
            contenido = self.file_system.leer_archivo(nombre_archivo)
            if contenido is not None:
                messagebox.showinfo(f"Contenido de '{nombre_archivo}'", contenido)
            else:
                messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")

    def eliminar_archivo(self):
        nombre_archivo = simpledialog.askstring("Eliminar Archivo", "Ingrese el nombre del archivo a eliminar:")
        if nombre_archivo:
            self.file_system.eliminar_archivo(nombre_archivo)
            messagebox.showinfo("Archivo Eliminado", f"Archivo '{nombre_archivo}' eliminado exitosamente.")

    def actualizar_archivo(self):
        nombre_archivo = simpledialog.askstring("Actualizar Archivo", "Ingrese el nombre del archivo:")
        if nombre_archivo:
            contenido_adicional = simpledialog.askstring("Contenido Adicional", "Ingrese el contenido adicional:")
            if contenido_adicional:
                self.file_system.escribir_archivo(nombre_archivo, contenido_adicional)
                messagebox.showinfo("Archivo Actualizado", f"Contenido agregado al archivo '{nombre_archivo}'.")

# Crear y ejecutar la interfaz con estilo e imágenes
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()