import sys

from PyQt5.QtCore import Qt
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from ui import Ui_MainWindow
from dialog_ui import Ui_Dialog

#
# CURRENCIES = [['USD', 'BGN'],
#               ['CZK', 'DKK'],
#               ['GBP', 'HUF'],
#               ['RON', 'SEK'],
#               ['CHF', 'ISK'],
#               ['TRY', 'AUD'],
#               ['BRL', 'CAD'],
#               ['HKD', 'INR'],
#               ['MXN', 'MYR'],
#               ['NZD', 'PHP'],
#               ['SGD', 'THB']]

CURRENCIES = [
['USD', 'BGN', 'CZK', 'DKK'],
['GBP', 'HUF', 'RON', 'SEK'],
['CHF', 'ISK', 'TRY', 'AUD'],
['BRL', 'CAD', 'HKD', 'INR'],
['MXN', 'MYR', 'NZD', 'PHP']
]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('Конвертер валют')
        self.ui.input_currency.setPlaceholderText('Из валюты')
        self.ui.input_amount.setPlaceholderText('Количество денег')
        self.ui.output_currency.setPlaceholderText('В валюту')
        self.ui.output_amount.setPlaceholderText('Я получу')
        self.ui.pushButton.clicked.connect(self.btn_converter)
        self.ui.pushButton_2.clicked.connect(self.btn_help_dialog)
        self.setWindowIcon(QIcon('./icon.ico'))


    def btn_converter(self):
        input_currency = self.ui.input_currency.text()
        input_amount = self.ui.input_amount.text()
        output_currency = self.ui.output_currency.text()
        output_amount = self.convert_currency(
            base_cur=input_currency,
            dest_cur=output_currency,
            amount=input_amount
        )
        self.ui.output_amount.setText(output_amount)


    def btn_help_dialog(self):
        self.dialog = Dialog()
        self.dialog.show()


    @staticmethod
    def convert_currency(base_cur: str, dest_cur: str, amount: str | float) -> str:
        c = CurrencyRates()
        try:
            base_cur = str(base_cur).upper()
            dest_cur = str(dest_cur).upper()
            amount = float(amount)
            return str(round(c.convert(base_cur=base_cur, dest_cur=dest_cur, amount=amount), 3))
        except RatesNotAvailableError:
            return "Нет информации"
        except (ValueError, AttributeError, Exception):
            return "Ошибка данных"


class Dialog(QtWidgets.QWidget):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('Справка')
        self.setWindowIcon(QIcon('./icon.ico'))
        self.ui.pushButton.clicked.connect(self.btn_ok)
        self.ui.tableWidget.setRowCount(len(CURRENCIES))
        self.ui.tableWidget.setColumnCount(len(CURRENCIES[0]))
        row = 0
        for val in CURRENCIES:
            col = 0
            for item in val:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                cellinfo.setTextAlignment(Qt.AlignHCenter)
                col += 1
            row += 1


    def btn_ok(self):
        self.close()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec_())