import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from huffman import HuffmanCoding
import os

class HuffmanApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Seleccione un archivo para comprimir o descomprimir")
        self.layout.add_widget(self.label)

        # File chooser for selecting the file
        self.file_chooser = FileChooserIconView()
        self.layout.add_widget(self.file_chooser)

        # Compression button
        self.compress_button = Button(text="Comprimir archivo")
        self.compress_button.bind(on_press=self.compress_file)
        self.layout.add_widget(self.compress_button)

        # Decompression button
        self.decompress_button = Button(text="Descomprimir archivo")
        self.decompress_button.bind(on_press=self.decompress_file)
        self.layout.add_widget(self.decompress_button)

        # Output label
        self.output_label = Label(text="")
        self.layout.add_widget(self.output_label)

        return self.layout

    def compress_file(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            file_path = selected_file[0]
            huffman = HuffmanCoding(file_path)
            output_path = huffman.compress()
            self.output_label.text = f"Archivo comprimido en: {output_path}"
        else:
            self.output_label.text = "No se ha seleccionado ningún archivo."

    def decompress_file(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            file_path = selected_file[0]
            huffman = HuffmanCoding(file_path)
            output_path = huffman.decompress(file_path)
            self.output_label.text = f"Archivo descomprimido en: {output_path}"
        else:
            self.output_label.text = "No se ha seleccionado ningún archivo."

if __name__ == "__main__":
    HuffmanApp().run()
