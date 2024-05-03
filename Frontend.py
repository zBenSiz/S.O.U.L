from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from Backend import FantasmaAssistant

class FantasmaAssistantUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Configurar ventana flotante sin bordes
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Configurar el tamaño de la ventana
        self.resize(200, 200)

        # Configurar la posición inicial de la ventana en la esquina superior derecha
        desktop = QtWidgets.QApplication.desktop()
        screen_rect = desktop.availableGeometry(desktop.primaryScreen())
        self.move(screen_rect.right() - self.width(), 0)

        # Definir una etiqueta para mostrar el GIF
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.label.setObjectName("label")

        # Integrar QMovie a la etiqueta e iniciar el GIF
        self.movie = QMovie("img/gh-afk-op_1_1_1.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # Iniciar el asistente
        self.assistant = FantasmaAssistant()
        self.assistant.on_button_click()

        # Variables para el seguimiento del arrastre
        self.dragging = False
        self.offset = None

    # Métodos para manejar el arrastre de la ventana
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToGlobal(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False
            self.offset = None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = FantasmaAssistantUI()
    ui.show()
    sys.exit(app.exec_())
