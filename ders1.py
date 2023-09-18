import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,400,400)
    win.setWindowTitle("İlk Proje")

    #lbl1
    lbl_isim=QtWidgets.QLabel(win)
    lbl_isim.setText("İsim:")
    lbl_isim.move(120,30)

    #lbl2
    lbl_soyisim=QtWidgets.QLabel(win)
    lbl_soyisim.setText("Soyisim:")
    lbl_soyisim.move(120,80)

    #input
    txt_isim=QtWidgets.QLineEdit(win)
    txt_isim.move(200,30)

    #input
    txt_soyisim = QtWidgets.QLineEdit(win)
    txt_soyisim.move(200,80)

    #lbl yazdırma bölümü
    lbl_sonuc=QtWidgets.QLabel(win)
    lbl_sonuc.move(200,160)

    #buton
    def yazdir():
        print("Butona Tıklanıldı")
        print(txt_isim.text(),txt_soyisim.text())
        lbl_sonuc.setText(txt_isim.text()+ ' ' + txt_soyisim.text())

    buton=QtWidgets.QPushButton(win)
    buton.move(200,120)
    buton.setText("Yazdır")
    buton.clicked.connect(yazdir)


    win.show()
    sys.exit(app.exec_())
window()
