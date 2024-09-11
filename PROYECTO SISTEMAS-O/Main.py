import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

class SimpleFileSystem:
    def __init__(self):
        self.archivos = {}  

    def crear_archivo(self, nombre, contenido):
        self.archivos[nombre] = contenido  
        return f"Archivo '{nombre}' creado."

    def leer_archivo(self, nombre):
        if nombre in self.archivos:
            return self.archivos[nombre]  
        return None

    def escribir_archivo(self, nombre, contenido_adicional):
        if nombre in self.archivos:
            self.archivos[nombre] += "\n" + contenido_adicional  
            return f"Archivo '{nombre}' actualizado."
        return None

    def eliminar_archivo(self, nombre):
        if nombre in self.archivos:
            del self.archivos[nombre]  
            return f"Archivo '{nombre}' eliminado."
        return None

    def listar_archivos(self):
        return list(self.archivos.keys())  

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Archivos")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.file_system = SimpleFileSystem()

        self.bg_image = Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Fondo_Final.jpg")
        self.bg_image = self.bg_image.resize((1366, 768), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=768, height=1366)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.img_crear = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Crear_Archivos.png").resize((50, 50)))
        self.img_buscar = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Buscar_Archivos.png").resize((50, 50)))
        self.img_eliminar = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Eliminar_Archivos.png").resize((50, 50)))
        self.img_actualizar = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Actualizar_Archivos.png").resize((50, 50)))
        self.img_listar = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Listar_Archivos.png").resize((50, 50)))
        self.img_salir = ImageTk.PhotoImage(Image.open("C:\\Users\\USUARIO\\Documents\\ARCHIVOS\\PROYECTO SISTEMAS-O\\Imagenes\\Salir.png").resize((50, 50)))

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg='#f0f0f0')
        frame.place(relx=0.5, rely=0.5, anchor="center") 

        self.btn_crear = tk.Button(frame, text="Crear Archivo", image=self.img_crear, compound='left',
                                   command=self.crear_archivo, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'),
                                   relief='flat', padx=10, pady=5)
        self.btn_crear.grid(row=0, column=0, padx=10, pady=10)

        self.btn_buscar = tk.Button(frame, text="Buscar Archivo", image=self.img_buscar, compound='left',
                                    command=self.buscar_archivo, bg='#2196F3', fg='white', font=('Helvetica', 12, 'bold'),
                                    relief='flat', padx=10, pady=5)
        self.btn_buscar.grid(row=0, column=1, padx=10, pady=10)

        self.btn_eliminar = tk.Button(frame, text="Eliminar Archivo", image=self.img_eliminar, compound='left',
                                      command=self.eliminar_archivo, bg='#F44336', fg='white', font=('Helvetica', 12, 'bold'),
                                      relief='flat', padx=10, pady=5)
        self.btn_eliminar.grid(row=0, column=2, padx=10, pady=10)

        self.btn_actualizar = tk.Button(frame, text="Actualizar Archivo", image=self.img_actualizar, compound='left',
                                        command=self.actualizar_archivo, bg='#FF9800', fg='white', font=('Helvetica', 12, 'bold'),
                                        relief='flat', padx=10, pady=5)
        self.btn_actualizar.grid(row=0, column=3, padx=10, pady=10)

        self.btn_listar = tk.Button(frame, text="Listar Archivos", image=self.img_listar, compound='left',
                                    command=self.listar_archivos, bg='#9C27B0', fg='white', font=('Helvetica', 12, 'bold'),
                                    relief='flat', padx=10, pady=5)
        self.btn_listar.grid(row=0, column=4, padx=10, pady=10)

        self.btn_salir = tk.Button(frame, text="Salir", image=self.img_salir, compound='left',
                                   command=self.root.quit, bg='#9E9E9E', fg='white', font=('Helvetica', 12, 'bold'),
                                   relief='flat', padx=10, pady=5)
        self.btn_salir.grid(row=0, column=5, padx=10, pady=10)

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
            mensaje = self.file_system.eliminar_archivo(nombre_archivo)
            if mensaje:
                messagebox.showinfo("Archivo Eliminado", mensaje)
            else:
                messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")

    def actualizar_archivo(self):
        nombre_archivo = simpledialog.askstring("Actualizar Archivo", "Ingrese el nombre del archivo:")
        if nombre_archivo:
            contenido_adicional = simpledialog.askstring("Contenido Adicional", "Ingrese el contenido adicional:")
            if contenido_adicional:
                mensaje = self.file_system.escribir_archivo(nombre_archivo, contenido_adicional)
                if mensaje:
                    messagebox.showinfo("Archivo Actualizado", mensaje)
                else:
                    messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")

    def listar_archivos(self):
        archivos = self.file_system.listar_archivos()

        if archivos:
            archivos_str = "\n".join(archivos) 
            messagebox.showinfo("Archivos", f"Archivos en el sistema:\n{archivos_str}")
        else:
            messagebox.showinfo("Archivos", "No hay archivos en el sistema.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()