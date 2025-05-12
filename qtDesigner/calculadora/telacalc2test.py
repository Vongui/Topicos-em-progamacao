from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputNumero1 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumero1.setGeometry(QtCore.QRect(30, 30, 142, 27))
        self.inputNumero1.setObjectName("inputNumero1")

        self.inputNumero2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumero2.setGeometry(QtCore.QRect(280, 30, 141, 27))
        self.inputNumero2.setObjectName("inputNumero2")

        self.labelNumero1 = QtWidgets.QLabel(self.centralwidget)
        self.labelNumero1.setGeometry(QtCore.QRect(60, 10, 66, 19))
        self.labelNumero1.setObjectName("labelNumero1")

        self.labelNumero2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNumero2.setGeometry(QtCore.QRect(320, 10, 66, 19))
        self.labelNumero2.setObjectName("labelNumero2")

        self.btnSoma = QtWidgets.QPushButton(self.centralwidget)
        self.btnSoma.setGeometry(QtCore.QRect(20, 160, 88, 27))
        self.btnSoma.setObjectName("btnSoma")

        self.btnSub = QtWidgets.QPushButton(self.centralwidget)
        self.btnSub.setGeometry(QtCore.QRect(130, 160, 88, 27))
        self.btnSub.setObjectName("btnSub")

        self.btnDivisao = QtWidgets.QPushButton(self.centralwidget)
        self.btnDivisao.setGeometry(QtCore.QRect(350, 160, 88, 27))
        self.btnDivisao.setObjectName("btnDivisao")

        self.btnMulti = QtWidgets.QPushButton(self.centralwidget)
        self.btnMulti.setGeometry(QtCore.QRect(240, 160, 91, 27))
        self.btnMulti.setObjectName("btnMulti")

        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(190, 70, 81, 19))
        self.labelResultado.setObjectName("labelResultado")

        self.screenResult = QtWidgets.QLCDNumber(self.centralwidget)
        self.screenResult.setGeometry(QtCore.QRect(160, 90, 121, 41))
        self.screenResult.setObjectName("screenResult")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.btnSoma.clicked.connect(self.soma)
        self.btnSub.clicked.connect(self.sub)
        self.btnMulti.clicked.connect(self.multi)
        self.btnDivisao.clicked.connect(self.divisao)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def obterNums(self):
        n1 = float(self.inputNumero1.text())
        n2 = float(self.inputNumero2.text())

        return n1, n2

    def soma(self):
        n1, n2 = self.obterNums()
        result = n1 + n2
        self.screenResult.display(result)

    def sub(self):
        n1, n2 = self.obterNums()
        result = n1 - n2
        self.screenResult.display(result)

    def multi(self):
        n1, n2 = self.obterNums()
        result = n1 * n2
        self.screenResult.display(result)

    def divisao(self):
        n1, n2 = self.obterNums()
        if n2 != 0:
            result = n1 / n2
            self.screenResult.display(result)
        else:
            self.screenResult.display("Erro")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.labelNumero1.setText(_translate("MainWindow", "Número 1"))
        self.labelNumero2.setText(_translate("MainWindow", "Número 2"))
        self.btnSoma.setText(_translate("MainWindow", "Soma"))
        self.btnSub.setText(_translate("MainWindow", "Subtração"))
        self.btnDivisao.setText(_translate("MainWindow", "Divisão"))
        self.btnMulti.setText(_translate("MainWindow", "Multiplicação"))
        self.labelResultado.setText(_translate("MainWindow", "Resultado"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
