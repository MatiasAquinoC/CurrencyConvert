import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton
from PyQt5 import uic

class Dialogo(QMainWindow):
    exchange_rates = {
        'USD': {'PEN': 3.84, 'EUR': 0.93, 'GBP': 0.79, 'USD': 1.0},
        'EUR': {'USD': 1.08, 'PEN': 4.13, 'GBP': 0.85, 'EUR': 1.0},
        'PEN': {'USD': 0.26, 'EUR': 0.24, 'GBP': 0.20, 'PEN': 1.0},
        'GBP': {'USD': 1.27, 'EUR': 1.17, 'PEN': 4.84, 'GBP': 1.0}
    }

    def __init__(self):
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta, self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        try:
            inicial = float(self.leImporte.text())

            moneda_de = self.get_selected_currency(self.gbDe)
            moneda_a = self.get_selected_currency(self.gbA)

            tasa_cambio = self.exchange_rates[moneda_de][moneda_a]
            convertido = inicial * tasa_cambio

            self.lblCambio.setText(f"{convertido:.2f}")
        except ValueError:
            self.lblCambio.setText("Error")

    def get_selected_currency(self, groupbox):
        for rb in groupbox.findChildren(QRadioButton):
            if rb.isChecked():
                return rb.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec_()
