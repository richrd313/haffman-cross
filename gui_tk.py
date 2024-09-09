import tkinter as tk
from tkinter import filedialog, messagebox
from huffman import HuffmanCoding
import os

class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compresor y Descompresor Huffman")
        self.root.geometry("600x300")
        self.root.configure(bg='#2E2E2E')

        # Etiqueta de selección de archivo
        self.label = tk.Label(root, text="Seleccione un archivo", bg='#2E2E2E', fg='#FFFFFF', font=('Arial', 16))
        self.label.pack(pady=20)

        # Botón para seleccionar archivo
        self.select_button = tk.Button(root, text="Seleccionar archivo", command=self.select_file, bg='#4CAF50', fg='white', font=('Arial', 12), padx=20, pady=10, relief='flat')
        self.select_button.pack(pady=10)

        # Botón para comprimir
        self.compress_button = tk.Button(root, text="Comprimir archivo", command=self.compress_file, bg='#2196F3', fg='white', font=('Arial', 12), padx=20, pady=10, relief='flat')
        self.compress_button.pack(pady=10)

        # Botón para descomprimir
        self.decompress_button = tk.Button(root, text="Descomprimir archivo", command=self.decompress_file, bg='#FF5722', fg='white', font=('Arial', 12), padx=20, pady=10, relief='flat')
        self.decompress_button.pack(pady=10)

        # Variable para guardar la ruta del archivo seleccionado
        self.file_path = None

    def select_file(self):
        # Abrir diálogo para seleccionar un archivo
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.label.config(text=f"Archivo seleccionado: {os.path.basename(self.file_path)}")
        else:
            self.label.config(text="No se seleccionó ningún archivo")

    def compress_file(self):
        if self.file_path:
            h = HuffmanCoding(self.file_path)
            output_path = h.compress()
            self.show_popup("Comprimir", f"Archivo comprimido guardado en: {output_path}")
        else:
            self.show_popup("Advertencia", "Primero seleccione un archivo")

    def decompress_file(self):
        if self.file_path:
            h = HuffmanCoding(self.file_path)
            output_path = h.decompress(self.file_path)
            self.show_popup("Descomprimir", f"Archivo descomprimido guardado en: {output_path}")
        else:
            self.show_popup("Advertencia", "Primero seleccione un archivo")

    def show_popup(self, title, message):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("1000x250")
        popup.configure(bg='#2E2E2E')

        label = tk.Label(popup, text=message, bg='#2E2E2E', fg='#FFFFFF', font=('Arial', 12))
        label.pack(pady=20)

        button = tk.Button(popup, text="Cerrar", command=popup.destroy, bg='#4CAF50', fg='white', font=('Arial', 12), padx=20, pady=10, relief='flat')
        button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanApp(root)
    root.mainloop()
