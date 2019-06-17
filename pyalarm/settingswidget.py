import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from pyalarm.alarm import Alarm
from pyalarm.config import Config
from pyalarm.editwidget import EditWidget

class SettingsWidget(QWidget) :
    def __init__(self, parent):
        super().__init__(parent)
        self.__initUI()        
        
    def __initUI(self):
        self.setGeometry(10, 10, 780, 460)
        pallet = QPalette()
        pallet.setColor(QPalette.Background, QtCore.Qt.darkGray)
        self.setPalette(pallet)
        self.setAutoFillBackground(True)
        self.setVisible(False)       
       
        self.__list = QListWidget(self)
        self.__list.setGeometry(10, 10, 760, 400)

        self.__exitButton = QPushButton(self)
        self.__exitButton.setGeometry(600, 410, 150, 50)
        self.__exitButton.setText("Save & Exit")
        font = QFont("SansSerif", pointSize=25)
        self.__exitButton.setFont(font)
        self.__exitButton.mousePressEvent = self.__exitClicked

        self.__addButton = QPushButton(self)
        self.__addButton.setGeometry(10, 410, 150, 50)
        self.__addButton.setText("Add")
        self.__addButton.setFont(font)
        self.__addButton.mousePressEvent = self.__addClicked

        self.__editButton = QPushButton(self)
        self.__editButton.setGeometry(170, 410, 150, 50)
        self.__editButton.setText("Edit")
        self.__editButton.setFont(font)
        self.__editButton.mousePressEvent = self.__editClicked

        self.__deleteButton = QPushButton(self)
        self.__deleteButton.setGeometry(330, 410, 150, 50)
        self.__deleteButton.setText("Remove")
        self.__deleteButton.setFont(font)
        self.__deleteButton.mousePressEvent = self.__deleteClicked
    
    def __exitClicked(self, event):
        self.__save()
        self.setVisible(False)
    
    def __addClicked(self, event):
        alarm = Alarm()
        item = QListWidgetItem(alarm.presentationString(), self.__list)
        item.setData(1, alarm)
        self.__list.addItem(item)

    def __editClicked(self, event):
        items = self.__list.selectedItems() 
        if len(items) > 0:
            item = items[0]
            editWidget = EditWidget(self, item.data(1))
            editWidget.show()
            editWidget.closeEvent = self.__editClosed

    def __editClosed(self, event):
        sender = self.sender()
        editWidget = sender.parent()
        alarm = editWidget.alarm
        item = self.__list.selectedItems()[0]
        item.setText(alarm.presentationString())
        item.setData(1, alarm)

    def __deleteClicked(self, event):
        items = self.__list.selectedItems()
        for item in items:
            self.__list.takeItem(self.__list.row(item))
    
    def __save(self):
        self.__config.getAlarms().clear()
        for i in range(0, self.__list.count()):
            item = self.__list.item(i)
            alarm = item.data(1)
            self.__config.getAlarms().append(alarm)
        self.__config.save()

    def __generateData(self, config):
        for alarm in config.getAlarms():
            item = QListWidgetItem(alarm.presentationString(), self.__list)
            item.setData(1, alarm)
            self.__list.addItem(item)

    def activate(self, config):
        self.__config = config
        self.setVisible(True)
        self.raise_()
        self.__list.clear()
        self.__generateData(config)
