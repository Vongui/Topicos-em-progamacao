import sys
from PyQt5 import QtWidgets, uic

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("telacalc.ui", self)
        self._conectar_sinais()

    def _conectar_sinais(self):

        for botao in (
            self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,
            self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,
            self.btnAdd, self.btnSub, self.btnMul, self.btnDiv
        ):
            botao.clicked.connect(self._adicionar_ao_visor)

        self.btnClear.clicked.connect(self.lineEdit_Display.clear)
        self.btnEqual.clicked.connect(self._calcular_resultado)

    def _adicionar_ao_visor(self):
        texto_botao = self.sender().text()
        self.lineEdit_Display.setText(self.lineEdit_Display.text() + texto_botao)

    def _calcular_resultado(self):
        expressao = self.lineEdit_Display.text()
        try:
            resultado = str(eval(expressao, {"__builtins__": None}, {}))
            self.lineEdit_Display.setText(resultado)
        except Exception:
            self.lineEdit_Display.setText("Erro")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = Calculator()
    janela.show()
    sys.exit(app.exec_())
