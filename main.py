import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 250, 100, 50))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Начать"))


class Circles(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = False
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.f = True
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QtGui.QPainter()
            qp.begin(self)
            c = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setBrush(c)
            qp.setPen(c)
            r = random.randint(1, 400)
            qp.drawEllipse(QtCore.QPointF(random.randint(0, 800), random.randint(0, 600)), r, r)
            qp.end()
            self.f = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec())
