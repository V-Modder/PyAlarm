import sys

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from pyalarm.settingswidget import SettingsWidget

class ContextMenu(QWidget) :
    def __init__(self, parent):
        super().__init__(parent)
        self.__initUI(parent)        
        
    def __initUI(self, parent):
        self.setGeometry(0, 0, 150, 480)
        pallet = QPalette()
        pallet.setColor(QPalette.Background, QtCore.Qt.darkGray)
        self.setPalette(pallet)
        self.setAutoFillBackground(True)
        self.setVisible(False)

        self.__alarmButton = QLabel(self)
        self.__alarmButton.setGeometry(0, 0, self.width(), 50)
        self.__alarmButton.setText("Alarms")
        font = QFont("SansSerif", pointSize=25)
        self.__alarmButton.setFont(font)
        self.__alarmButton.mousePressEvent = self.__alarmClicked

        self.__exitButton = QLabel(self)
        self.__exitButton.setGeometry(0, 60, self.width(), 50)
        self.__exitButton.setText("Exit")
        self.__exitButton.setFont(font)
        self.__exitButton.mousePressEvent = self.__exitClicked   

        self.__settingsWidget = SettingsWidget(parent)
        self.__settingsWidget.show()
        self.__settingsWidget.setVisible(False)

    def __alarmClicked(self, event):
        self.__settingsWidget.activate(self.__config)
        self.setVisible(False)
    
    def __exitClicked(self, event):
        sys.exit()
    
    def activate(self, config):
        self.setVisible(True)
        self.raise_()
        self.__config = config
        