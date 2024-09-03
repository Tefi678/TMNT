import tkinter as tk
from tkinter import filedialog, messagebox
from file_system import SimpleFileSystem

class FileSystemGUI:
    def __init__(self):
        self.directorio = "mis_archivos"
        self.file_system = SimpleFileSystem(self.directorio)
        self.root = tk.Tk()
        self.root.title("Sistema de Archivos")

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        self.lbl_directorio = tk.Label(self.root, text=f"Directorio: {self.directorio}")
        self.lbl_directorio.pack()

        self.btn_crear = tk.Button(self.root, text="Crear Archivo", command=self.crear_archivo)
        self.btn_crear.pack()

        self.btn_leer = tk.Button(self.root, text="Leer Archivo", command=self.leer_archivo)
        self.btn_leer.pack()

        self.btn_escribir = tk.Button(self.root, text="Escribir en Archivo", command=self.escribir_archivo)
        self.btn_escribir.pack()

        self.btn_eliminar = tk.Button(self.root, text="Eliminar Archivo", command=self.eliminar_archivo)
        self.btn_eliminar.pack()

        self.btn_listar = tk.Button(self.root, text="Listar Archivos", command=self.listar_archivos)
        self.btn_listar.pack()

    def run(self):
        self.root.mainloop()

    def crear_archivo(self):
        nombre = self.ask_user("Nombre del archivo", "Ingrese el nombre del archivo:")
        contenido = self.ask_user("Contenido del archivo", "Ingrese el contenido del archivo:")
        try:
            self.file_system.crear_archivo(nombre, contenido)
            messagebox.showinfo("Éxito", f"Archivo '{nombre}' creado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def leer_archivo(self):
        nombre = self.ask_user("Nombre del archivo", "Ingrese el nombre del archivo:")
        try:
            contenido = self.file_system.leer_archivo(nombre)
            messagebox.showinfo("Contenido del Archivo", contenido)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def escribir_archivo(self):
        nombre = self.ask_user("Nombre del archivo", "Ingrese el nombre del archivo:")
        contenido_adicional = self.ask_user("Contenido Adicional", "Ingrese el contenido adicional:")
        try:
            self.file_system.escribir_archivo(nombre, contenido_adicional)
            messagebox.showinfo("Éxito", f"Contenido agregado al archivo '{nombre}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def eliminar_archivo(self):
        nombre = self.ask_user("Nombre del archivo", "Ingrese el nombre del archivo:")
        try:
            self.file_system.eliminar_archivo(nombre)
            messagebox.showinfo("Éxito", f"Archivo '{nombre}' eliminado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def listar_archivos(self):
        try:
            archivos = self.file_system.listar_archivos()
            archivos_list = "\n".join(archivos)
            messagebox.showinfo("Archivos en el Directorio", archivos_list)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def ask_user(self, title, prompt):
        return tk.simpledialog.askstring(title, prompt)

