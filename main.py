from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from logger import LogManagemnet
 
class MeuApp(QMainWindow):
 
    num1 = 0
    num2 = 0
    resultado = 0
    op = None
 
 
    log = LogManagemnet(__file__)
 
 
    def __init__(self):
        super().__init__()
        loadUi("interCalcIphone.ui", self)
        self.log.info("Iniciei a interface")
        self.setCalc()

    def setCalc(self):
        self.num_0.clicked.connect(lambda: self.btnNumeros(0))
        self.num_1.clicked.connect(lambda: self.btnNumeros(1))
        self.num_2.clicked.connect(lambda: self.btnNumeros(2))
        self.num_3.clicked.connect(lambda: self.btnNumeros(3))
        self.num_4.clicked.connect(lambda: self.btnNumeros(4))
        self.num_5.clicked.connect(lambda: self.btnNumeros(5))
        self.num_6.clicked.connect(lambda: self.btnNumeros(6))
        self.num_7.clicked.connect(lambda: self.btnNumeros(7))
        self.num_8.clicked.connect(lambda: self.btnNumeros(8))
        self.num_9.clicked.connect(lambda: self.btnNumeros(9))
 
        self.btnTotal.clicked.connect(self.mostrarResultado)
        self.btnLimpar.clicked.connect(self.limparNumeros)
        self.btnVirgula.clicked.connect(lambda: self.virgula(','))
        self.btnPosNeg.clicked.connect(self.trocaSinal)

        self.btnSoma.clicked.connect(lambda: self.definirOperacao(self.somarNumeros))
        self.btnSubtracao.clicked.connect(lambda: self.definirOperacao(self.subtrairNumeros))
        self.btnDivisao.clicked.connect(lambda: self.definirOperacao(self.divisaoNumeros))
        self.btnMultiplicacao.clicked.connect(lambda: self.definirOperacao(self.multiplicarNumeros))
        self.btnPorcentagem.clicked.connect(self.porcentagem)     
 
    def exibirDisplay(self, value):
        value = str(value).replace('.',  ',')
        self.btnTela.setText(str(value))
 
    def acessarDisplay(self):
        value = self.btnTela.text()
        value = value.replace(',', '.')
        try:
            value = int(value)
        except: 
            value = float(value)
        return value

    def btnNumeros(self, num):
        if self.acessarDisplay() == 0:
            self.exibirDisplay(num)
        else:
            numAtual = self.acessarDisplay()
            self.exibirDisplay(str(numAtual) + str(num) )
 
    def limparNumeros(self):
        self.num1 = 0
        self.num2 = 0
        self.numResultado = 0
        self.btnTela.clear()
        self.exibirDisplay(0)
 
    def somarNumeros(self):
        return self.num1 + self.num2
   
    def subtrairNumeros(self):
        return self.num1 - self.num2
 
    def multiplicarNumeros(self):
        return self.num1 * self.num2
   
    def divisaoNumeros(self):
        return self.num1 / self.num2
   
    def porcentagem(self):
        porcento = self.acessarDisplay() / 100
        if self.op == self.somarNumeros or self.op == self.subtrairNumeros:
            porcento = self.num1 * porcento
        self.exibirDisplay(porcento)
            
    def resultadoFinal(self):
        numeros = self.acessarDisplay()
        if self.op:
            self.num2 = numeros
            return self.op()
        else:
            print("Não tem operação feita!")
 
    def definirOperacao(self, operacao):
        self.op = operacao
        numeros = str(self.acessarDisplay())
        self.num1 = self.acessarDisplay()
        self.num2 = 0
        self.exibirDisplay(0)
            
    def virgula(self):
        pass

    def mostrarResultado(self):
        
        if self.op:
            if self.num2:
                self.num1 = self.acessarDisplay()
            else:
                self.num2 = self.acessarDisplay()
            self.numResultado = self.op()
            self.exibirDisplay(self.numResultado)
 
    def trocaSinal(self):
        numero = self.acessarDisplay()
        numero *= -1
        self.exibirDisplay(str(numero))

if __name__ == "__main__":
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()