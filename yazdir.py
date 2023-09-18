import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from isimyazdir import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buton.clicked.connect(self.yazdir)

    def yazdir(self):
        print("Butona Tıklandı.")

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
