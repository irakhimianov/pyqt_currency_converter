# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 580)
        MainWindow.setMinimumSize(QtCore.QSize(350, 580))
        MainWindow.setMaximumSize(QtCore.QSize(350, 580))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 451, 211))
        self.frame.setStyleSheet("background-color: #00aaff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(55, 30, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(115, 80, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("currency.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"backgorund-color: #00aaff;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"color: #000;\n"
"}")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 500, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: #00aaff;\n"
"border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"border: 2px solid #fff;\n"
"border-radius: 15;\n"
"color: #000;\n"
"}\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(100, 220, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_amount.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input_amount.setToolTipDuration(1)
        self.input_amount.setStyleSheet("border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #ffffff;")
        self.input_amount.setText("")
        self.input_amount.setMaxLength(20)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(100, 290, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_currency.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input_currency.setToolTipDuration(1)
        self.input_currency.setStyleSheet("border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #ffffff;")
        self.input_currency.setText("")
        self.input_currency.setMaxLength(20)
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(100, 360, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.output_currency.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.output_currency.setToolTipDuration(1)
        self.output_currency.setStyleSheet("border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #ffffff;")
        self.output_currency.setText("")
        self.output_currency.setMaxLength(20)
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(100, 430, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.output_amount.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.output_amount.setToolTipDuration(1)
        self.output_amount.setStyleSheet("border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #ffffff;")
        self.output_amount.setText("")
        self.output_amount.setMaxLength(20)
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setReadOnly(True)
        self.output_amount.setObjectName("output_amount")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.pushButton_2.setText(_translate("MainWindow", "?"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРОВАТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
