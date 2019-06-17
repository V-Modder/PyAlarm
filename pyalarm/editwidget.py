from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from pyalarm.alarm import Alarm
from pyalarm.config import Config

class EditWidget(QWidget) :
    def __init__(self, parent, alarm):
        super().__init__(parent)
        self.alarm = alarm
        self.__initUI()        
        
    def __initUI(self):
        self.setGeometry(10, 10, 780, 460)
        pallet = QPalette()
        pallet.setColor(QPalette.Background, QtCore.Qt.darkGray)
        self.setPalette(pallet)
        self.setAutoFillBackground(True)
        self.setVisible(False)

        self.__hourUpButton = QPushButton(self)
        self.__hourUpButton.setGeometry(50, 50, 50, 50)
        self.__hourUpButton.setText("Up")
        font = QFont("SansSerif", pointSize=25)
        self.__hourUpButton.setFont(font)
        self.__hourUpButton.clicked.connect(self.__hourUpClicked)

        self.__hourDownButton = QPushButton(self)
        self.__hourDownButton.setGeometry(50, 100, 50, 50)
        self.__hourDownButton.setText("Down")
        self.__hourDownButton.setFont(font)
        self.__hourDownButton.clicked.connect(self.__hourDownClicked)

        self.__hourText = QLabel(self)
        self.__hourText.setGeometry(100, 50, 100, 50)
        self.__hourText.setText(str(self.alarm.getHour()))
        font2 = QFont("SansSerif", pointSize=45)
        self.__hourText.setFont(font2)

        self.__minuteUpButton = QPushButton(self)
        self.__minuteUpButton.setGeometry(305, 50, 50, 50)
        self.__minuteUpButton.setText("Up")
        self.__minuteUpButton.setFont(font)
        self.__minuteUpButton.clicked.connect(self.__minuteUpClicked)

        self.__minuteDownButton = QPushButton(self)
        self.__minuteDownButton.setGeometry(305, 100, 50, 50)
        self.__minuteDownButton.setText("Down")
        self.__minuteDownButton.setFont(font)
        self.__minuteDownButton.clicked.connect(self.__minuteDownClicked)

        self.__minuteText = QLabel(self)
        self.__minuteText.setGeometry(205, 50, 100, 50)
        self.__minuteText.setText(str(self.alarm.getMinute()))
        self.__minuteText.setFont(font2)

        self.__mondayCheckbox = QCheckBox(self)
        self.__mondayCheckbox.setGeometry(10, 200, 100, 50)
        self.__mondayCheckbox.setText("Monday")
        self.__mondayCheckbox.setChecked(Alarm.MONDAY in self.alarm.getWeekdays())

        self.__tuesdayCheckbox = QCheckBox(self)
        self.__tuesdayCheckbox.setGeometry(110, 200, 100, 50)
        self.__tuesdayCheckbox.setText("Tuesday")
        self.__tuesdayCheckbox.setChecked(Alarm.TUESDAY in self.alarm.getWeekdays())

        self.__wednesdayCheckbox = QCheckBox(self)
        self.__wednesdayCheckbox.setGeometry(220, 200, 100, 50)
        self.__wednesdayCheckbox.setText("Wednesday")
        self.__wednesdayCheckbox.setChecked(Alarm.WEDNESDAY in self.alarm.getWeekdays())

        self.__thursdayCheckbox = QCheckBox(self)
        self.__thursdayCheckbox.setGeometry(330, 200, 100, 50)
        self.__thursdayCheckbox.setText("Thursday")
        self.__thursdayCheckbox.setChecked(Alarm.THURSDAY in self.alarm.getWeekdays())

        self.__fridayCheckbox = QCheckBox(self)
        self.__fridayCheckbox.setGeometry(440, 200, 100, 50)
        self.__fridayCheckbox.setText("Friday")
        self.__fridayCheckbox.setChecked(Alarm.FRIDAY in self.alarm.getWeekdays())

        self.__saturdayCheckbox = QCheckBox(self)
        self.__saturdayCheckbox.setGeometry(550, 200, 100, 50)
        self.__saturdayCheckbox.setText("Saturday")
        self.__saturdayCheckbox.setChecked(Alarm.SATURDAY in self.alarm.getWeekdays())

        self.__sundayCheckbox = QCheckBox(self)
        self.__sundayCheckbox.setGeometry(660, 200, 100, 50)
        self.__sundayCheckbox.setText("Sunday")
        self.__sundayCheckbox.setChecked(Alarm.SUNDAY in self.alarm.getWeekdays())

        self.__exitButton = QPushButton(self)
        self.__exitButton.setGeometry(50, 300, 100, 50)
        self.__exitButton.setText("Done")
        self.__exitButton.setFont(font)
        self.__exitButton.clicked.connect(self.__exitClicked)

    def __hourUpClicked(self):
        hour = int(self.__hourText.text())
        if hour == 23:
            hour = 0
        else:
            hour += 1
        self.__hourText.setText(str(hour))
    
    def __hourDownClicked(self):
        hour = int(self.__hourText.text())
        if hour == 0:
            hour = 23
        else:
            hour -= 1
        self.__hourText.setText(str(hour))
    
    def __minuteUpClicked(self):
        minute = int(self.__minuteText.text())
        if minute == 59:
            minute = 0
        else:
            minute += 1
        self.__minuteText.setText(str(minute))
    
    def __minuteDownClicked(self):
        minute = int(self.__minuteText.text())
        if minute == 0:
            minute = 59
        else:
            minute -= 1
        self.__minuteText.setText(str(minute))

    def __exitClicked(self):
        hour = int(self.__hourText.text())
        minute = int(self.__minuteText.text())
        self.alarm.setHour(hour)
        self.alarm.setMinute(minute)
        self.alarm.getWeekdays().clear()

        if self.__mondayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.MONDAY)
        if self.__tuesdayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.TUESDAY)
        if self.__wednesdayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.WEDNESDAY)
        if self.__thursdayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.THURSDAY)
        if self.__fridayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.FRIDAY)
        if self.__saturdayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.SATURDAY)
        if self.__sundayCheckbox.isChecked():
            self.alarm.getWeekdays().append(Alarm.SUNDAY)
        self.close()