from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

from pyalarm.alarmplayer import AlarmPlayer

class AlarmWidget(QWidget) :
    def __init__(self, parent):
        super().__init__(parent)
        self.__initUI()        
        
    def __initUI(self):
        self.setGeometry(50, 50, 700, 380)
        self.setStyleSheet("background-color:grey;")
        self.setVisible(False)

        self.__messageLabel = QLabel(self)
        self.__messageLabel.setGeometry(20, 20, self.width() - 40, self.height() - 40)
        self.__messageLabel.setText("Alarm")
        font = QFont("SansSerif", pointSize=45)
        self.__messageLabel.setFont(font)
        self.__messageLabel.mousePressEvent = self.__clicked

        self.__player = AlarmPlayer()

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__timerTick)
        

    def __clicked(self, event):
        self.setVisible(False)
        self.__timer.stop()
        self.__player.stop()

    def __timerTick(self):
        self.__player.increaseVolume()
    
    def activate(self):
        self.setVisible(True)
        self.raise_()
        self.__player.play()
        self.__player.setVolume(5)
        self.__timer.start(310)

        