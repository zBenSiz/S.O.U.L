from PyQt5 import QtWidgets
import sys
from Frontend import FantasmaAssistantUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = FantasmaAssistantUI()
    ui.show()
    sys.exit(app.exec_())
