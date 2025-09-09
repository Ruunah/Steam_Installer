from PySide6 import QtWidgets, QtCore, QtGui
import sys

class RoundedWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Install Options")
        self.resize(200, 100)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self._drag_pos = None

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(25)

        self.checkbox0 = QtWidgets.QCheckBox("Install VPN")
        self.checkbox0.setStyleSheet("""
            QCheckBox {
                color: #bdc1c6;
                font-size: 16px;
            }
            QCheckBox::indicator {
                width: 10px;
                height: 10px;
                border-radius: 7px;
                border: 2px solid #bdc1c6;
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background-color: #bdc1c6;
            }
        """)
        layout.addWidget(self.checkbox0, alignment=QtCore.Qt.AlignCenter)

        self.checkbox1 = QtWidgets.QCheckBox("Change Steam Name")
        self.checkbox1.setStyleSheet("""
            QCheckBox {
                color: #bdc1c6;
                font-size: 16px;
            }
            QCheckBox::indicator {
                width: 10px;
                height: 10px;
                border-radius: 7px;
                border: 2px solid #bdc1c6;
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background-color: #bdc1c6;
            }
        """)
        layout.addWidget(self.checkbox1, alignment=QtCore.Qt.AlignCenter)

        self.button = QtWidgets.QPushButton("Continue")
        self.button.setFixedSize(100, 40)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #bdc1c6;
                color: #011627;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #93a1a1;
            }
        """)
        layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        self.button.clicked.connect(self.on_continue)

    def on_continue(self):
        self.choice = [self.checkbox0.isChecked(), self.checkbox1.isChecked()]
        self.close()

    def paintEvent(self, event):
        radius = 20
        path = QtGui.QPainterPath()
        path.addRoundedRect(self.rect(), radius, radius)

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillPath(path, QtGui.QColor("#011627"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() & QtCore.Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None
        event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RoundedWindow()
    window.show()
    app.exec()
    return window.choice
