from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Almacena MainWindow como una variable de instancia
        MainWindow.setObjectName("MainWindow")

        # Configura la ventana para que sea transparente y sin bordes
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Define una etiqueta para mostrar el GIF
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setObjectName("label")

        # Inserta la etiqueta en la ventana principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Integra QMovie a la etiqueta e inicia el GIF
        self.movie = QMovie("img/gh-afk-op_1_1.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # Inicia el temporizador para mover la ventana
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_window)
        self.timer.start(50)  # Mueve la ventana cada 50 milisegundos

        # Configura las posiciones de inicio y fin del movimiento
        self.start_pos = QtCore.QPoint(0, 0)
        self.end_pos = QtCore.QPoint(QtWidgets.QDesktopWidget().availableGeometry().width() - 200, QtWidgets.QDesktopWidget().availableGeometry().height() - 200)
        self.direction = QtCore.QPoint(1, 1)

    def move_window(self):
        current_pos = self.MainWindow.pos()  # Usa la variable de instancia aquí

        # Calcula la siguiente posición de la ventana
        next_pos = current_pos + self.direction
        if next_pos.x() >= self.end_pos.x() or next_pos.x() <= self.start_pos.x():
            self.direction.setX(-self.direction.x())
        if next_pos.y() >= self.end_pos.y() or next_pos.y() <= self.start_pos.y():
            self.direction.setY(-self.direction.y())

        # Mueve la ventana a la siguiente posición
        self.MainWindow.move(next_pos)  # Usa la variable de instancia aquí

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.showFullScreen()  # Hace que la ventana sea de pantalla completa
    sys.exit(app.exec_())
