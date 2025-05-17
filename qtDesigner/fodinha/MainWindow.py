# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import urllib.parse


class Ui_CalculadoraWindow(QtWidgets.QMainWindow):
    def setupUi(self, CalculadoraWindow):
        CalculadoraWindow.setObjectName("CalculadoraWindow")
        CalculadoraWindow.resize(352, 600)
        CalculadoraWindow.setStyleSheet("background-color: rgb(119, 118, 123);")

        self.centralwidget = QtWidgets.QWidget(CalculadoraWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelExpressao = QtWidgets.QLabel(self.centralwidget)
        self.labelExpressao.setGeometry(QtCore.QRect(10, 5, 331, 30))
        self.labelExpressao.setStyleSheet("color: white; font-size: 16px;")
        self.labelExpressao.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelExpressao.setText("")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 35, 351, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.lcdNumber.setObjectName("lcdNumber")

        self.textHistory = QtWidgets.QTextEdit(self.centralwidget)
        self.textHistory.setGeometry(QtCore.QRect(0, 125, 351, 60))
        self.textHistory.setReadOnly(True)
        self.textHistory.setStyleSheet("background-color: rgb(70, 70, 75); color: white;")
        self.textHistory.setObjectName("textHistory")

        self._criar_botoes()
        CalculadoraWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CalculadoraWindow)
        self.statusbar.setObjectName("statusbar")
        CalculadoraWindow.setStatusBar(self.statusbar)
        self.retranslateUi(CalculadoraWindow)

        for botao in (
            self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,
            self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,
            self.btnMais, self.btnMenos, self.btnVezes, self.btnDivide,
            self.btnComma
        ):
            botao.clicked.connect(self._adicionar_ao_visor)

        self.btnC.clicked.connect(self.limpar_tela)
        self.btnIgual.clicked.connect(self._calcular_resultado)
        self.btnGpt.clicked.connect(self.abrir_chatgpt)
        self.btnBlackBox.clicked.connect(self.abrir_blackbox)

        QtCore.QMetaObject.connectSlotsByName(CalculadoraWindow)

        self.expressao = ""
        self.numero_atual = ""
        self.resultado_mostrado = False

    def _criar_botoes(self):
        self.btn0 = self._criar_botao("0", 0, 505)
        self.btnComma = self._criar_botao(",", 90, 505)
        self.btnC = self._criar_botao("C", 180, 505)
        self.btnIgual = self._criar_botao("=", 270, 440, 81, 126, "rgb(233,116,74)")
        self.btn3 = self._criar_botao("3", 180, 440)
        self.btn2 = self._criar_botao("2", 90, 440)
        self.btn1 = self._criar_botao("1", 0, 440)
        self.btn6 = self._criar_botao("6", 180, 375)
        self.btn5 = self._criar_botao("5", 90, 375)
        self.btn4 = self._criar_botao("4", 0, 375)
        self.btn9 = self._criar_botao("9", 180, 310)
        self.btn8 = self._criar_botao("8", 90, 310)
        self.btn7 = self._criar_botao("7", 0, 310)
        self.btnDivide = self._criar_botao("÷", 180, 245, cor="rgb(59,59,59)")
        self.btnGpt = self._criar_botao("GPT", 90, 245, cor="rgb(59,59,59)")
        self.btnBlackBox = self._criar_botao("BlackBoxIA", 0, 245, cor="rgb(59,59,59)")
        self.btnVezes = self._criar_botao("×", 270, 245, 81, 61, "rgb(59,59,59)")
        self.btnMenos = self._criar_botao("-", 270, 310, 81, 61, "rgb(59,59,59)")
        self.btnMais = self._criar_botao("+", 270, 375, 81, 61, "rgb(59,59,59)")

    def _criar_botao(self, texto, x, y, largura=88, altura=61, cor="rgb(155,156,156)"):
        botao = QtWidgets.QPushButton(self.centralwidget)
        botao.setGeometry(QtCore.QRect(x, y, largura, altura))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        botao.setFont(font)
        botao.setStyleSheet(f"background-color: {cor}; border-radius: 10%; color: white;")
        botao.setObjectName(f"btn{texto}")
        botao.setText(texto)
        return botao

    def limpar_tela(self):
        self.lcdNumber.display("0")
        self.labelExpressao.setText("")
        self.textHistory.clear()
        self.expressao = ""
        self.numero_atual = ""
        self.resultado_mostrado = False

    def _adicionar_ao_visor(self):
        texto_botao = self.sender().text()
        simbolo = texto_botao

        if simbolo == "÷":
            simbolo = "/"
        elif simbolo == "×":
            simbolo = "*"
        elif simbolo == ",":
            simbolo = "."

        if self.resultado_mostrado:
            if simbolo.isdigit() or simbolo == ".":
                self.expressao = ""
                self.numero_atual = ""
            self.resultado_mostrado = False

        self.expressao += simbolo
        self.labelExpressao.setText(self.expressao.replace("*", "×").replace("/", "÷"))

        if simbolo in "+-*/":
            self.numero_atual = ""
        else:
            self.numero_atual += simbolo

        self.lcdNumber.display(self.numero_atual if self.numero_atual else "0")

    def _calcular_resultado(self):
        try:
            resultado = str(eval(self.expressao, {"__builtins__": None}, {}))
            self.lcdNumber.display(resultado)
            self.textHistory.append(f"{self.labelExpressao.text()} = {resultado}")
            self.labelExpressao.setText("")
            self.expressao = resultado
            self.numero_atual = resultado
            self.resultado_mostrado = True
        except Exception:
            self.lcdNumber.display("Erro")
            self.labelExpressao.setText("")
            self.expressao = ""
            self.numero_atual = ""
            self.resultado_mostrado = False

    def abrir_chatgpt(self):
        if not self.expressao:
            return
        query = urllib.parse.quote(self.expressao)
        url = f"https://chat.openai.com/chat?query={query}"
        webbrowser.open(url)

    def abrir_blackbox(self):
        if not self.expressao:
            return
        query = urllib.parse.quote(self.expressao)
        url = f"https://www.blackbox.ai/search?q={query}"
        webbrowser.open(url)

    def retranslateUi(self, CalculadoraWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculadoraWindow.setWindowTitle(_translate("CalculadoraWindow", "Calculadora Foda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculadoraWindow = QtWidgets.QMainWindow()
    ui = Ui_CalculadoraWindow()
    ui.setupUi(CalculadoraWindow)
    CalculadoraWindow.show()
    sys.exit(app.exec_())
