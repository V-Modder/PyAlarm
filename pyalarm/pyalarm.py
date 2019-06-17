import sys
import time
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCalendarWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QTimer, QUrl, QDate
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5 import QtGui
from PyQt5 import QtCore


from pyalarm.alarm import Alarm
from pyalarm.alarmmanager import AlarmManager
from pyalarm.alarmwidget import AlarmWidget
from pyalarm.contextmenu import ContextMenu
from pyalarm.stripedbutton import StripedButton
from pyalarm.config import Config
from pyalarm.holidaycalender import HolidayCalendar

def main():
    app = QApplication(sys.argv)
    alarm = PyAlarm()
    sys.exit(app.exec_())

class PyAlarm(QMainWindow):
    LIBREELEC_URL="http://libreelec"

    def __init__(self):
        super().__init__()
        self.__config = Config()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle("PyAlarm")
        self.setWindowIcon(QIcon("pyalarm.png"))
        self.mousePressEvent = self.__windowClicked
        
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 800, 480)
        self.background.setPixmap(QPixmap("C:\\Users\\V-Modder\\projects\\pyalarm\\pyalarm\\pyalarm.png"))

        self.time = QLabel(self)
        self.time.setGeometry(122, 50, 250, 50)
        self.time.setText("00:00")
        font = QFont("SansSerif", pointSize=45)
        font.setBold(True)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.time.setStyleSheet("QLabel#time {color: white}")

        self.calender = QCalendarWidget(self)
        self.calender.setGeometry(50, 130, 320, 250)
        self.calender.setEnabled(False)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.__timerTick)
        self.timer.start(1000)

        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.ShowScrollBars, False)
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, False)

        self.browser = QWebEngineView(self)
        self.browser.load(QUrl(self.LIBREELEC_URL))
        self.browser.setGeometry(410, 10, 380, 460)
        self.browser.loadFinished.connect(self.__browserLoadFinished)
        
        self.contextButton = StripedButton(self)
        self.contextButton.setGeometry(3, 3, 50, 50)
        self.contextButton.clicked.connect(self.__contextClicked)

        self.__contextMenu = ContextMenu(self)
        self.__contextMenu.show()
        self.__contextMenu.setVisible(False)

        self.__alarmWidget = AlarmWidget(self)
        self.__alarmWidget.show()
        self.__alarmWidget.setVisible(False)

        self.show()

    def __timerTick(self):
        currentDate = datetime.now()
        self.time.setText(currentDate.strftime("%H:%M"))
        self.calender.setSelectedDate(QDate())

        alarmManager = AlarmManager(self.__config)
        holiday = HolidayCalendar(self.__config.getHolidayUser(), self.__config.getHolidayPassword)
        if alarmManager.alarmAvailable(currentDate) and  not holiday.isHolidayToday():
            self.__alarmWidget.activate()

    def __contextClicked(self):
        self.__contextMenu.activate(self.__config)     

    def __windowClicked(self, event):
        self.__contextMenu.setVisible(False)  

    def __browserLoadFinished(self, success):
        if success == False:
            time.sleep(1)
            self.browser.load(QUrl(self.LIBREELEC_URL))