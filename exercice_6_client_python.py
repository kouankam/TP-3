import webbrowser
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your host IP:", self)
        self.text1 = QLineEdit(self)
        self.label1.move(10,30)
        self.text1.move(10, 60)
        
        
        #************************************************************************************************
        self.label2 = QLabel("Enter your api_key:", self)
        self.text2 = QLineEdit(self)
        self.label2.move(10,90)
        self.text2.move(10, 120)
        
        #**************************************************************************************************
        self.label2 = QLabel("Enter your hostname:", self)
        self.text3 = QLineEdit(self)
        self.label2.move(10,150)
        self.text3.move(10, 180)
        
        self.label3 = QLabel("Answer:", self)
        self.label3.move(10, 210)
        self.button = QPushButton("Send", self)
        self.button.move(10, 240)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text3.text()
        hostIp = self.text1.text()
        apiKey = self.text2.text()


        if hostname == "" or hostIp == "" or apiKey =="":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,hostIp,apiKey)
            print(res)
            if res:
                self.__processing(hostname,hostIp,apiKey)
                self.label4.setText("Answer%s" % (res["Hello"]))
                self.label4.adjustSize()
                self.show()

    def __query(self, hostname,hostIp,apiKey):
        url = "http://%s/ip/%s?key=%s" % (hostname,hostIp,apiKey)
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
        
    def __processing(self, hostname,hostIp,apiKey):
        lat = self.__query(hostname,hostIp,apiKey)["lat"]
        long = self.__query(hostname,hostIp,apiKey)["long"]
        print(long,lat)

        url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (lat,long)
        webbrowser.open_new(url)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
    #interface graphique 6