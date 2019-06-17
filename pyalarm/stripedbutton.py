from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import Qt, pyqtSignal

class StripedButton(QAbstractButton):

    def __init__(self, parent, stripeCount=3, stripeThikness=3, color=16777215):
        QAbstractButton.__init__(self, parent)
        self.stripeCount = stripeCount
        self.stripeThikness = stripeThikness
        self.stripeColor = QColor.fromRgb(color)

    def paintEvent(self, event):
        neededSpaces = (self.height() - self.stripeThikness) / (self.stripeCount + 1)
        painter = QPainter()
        painter.begin(self)
        painter.drawLine(0, 10, 10, 10)
        for i in range(self.stripeCount):
            rectangle = QRectF(1.0, neededSpaces * (i + 1), self.width() - 2, self.stripeThikness)
            painter.drawRoundedRect(rectangle, 50.0, 50.0, mode=Qt.RelativeSize)
            painter.fillRect(rectangle, self.stripeColor)

        painter.end()
