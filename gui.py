from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from huffman import HuffmanCoding
import sys

class HuffmanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Layout y elementos de la interfaz
        layout = QVBoxLayout()
        
        self.label = QLabel("Selecciona un archivo para comprimir o descomprimir", self)
        layout.addWidget(self.label)

        self.compressButton = QPushButton('Comprimir archivo', self)
        self.compressButton.clicked.connect(self.compressFile)
        layout.addWidget(self.compressButton)

        self.decompressButton = QPushButton('Descomprimir archivo', self)
        self.decompressButton.clicked.connect(self.decompressFile)
        layout.addWidget(self.decompressButton)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Compresor Huffman')
        self.show()

    def compressFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona el archivo para comprimir", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            print(f"Archivo seleccionado para comprimir: {fileName}")
            h = HuffmanCoding(fileName)
            output_path = h.compress()
            print(f"Archivo comprimido guardado en: {output_path}")  # Mensaje de depuración
            self.label.setText(f"Archivo comprimido guardado en: {output_path}")

    def decompressFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona el archivo para descomprimir", "", "Binary Files (*.bin);;All Files (*)", options=options)
        if fileName:
            print(f"Archivo seleccionado para descomprimir: {fileName}")
            h = HuffmanCoding(fileName)
            decom_path = h.decompress(fileName)
            print(f"Archivo descomprimido guardado en: {decom_path}")  # Mensaje de depuración
            self.label.setText(f"Archivo descomprimido guardado en: {decom_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HuffmanApp()
    sys.exit(app.exec_())
