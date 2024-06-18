from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
class Toast(QWidget):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: #333; color: #fff; border-radius: 10px; padding: 10px;")

        self.layout = QVBoxLayout()
        self.message_label = QLabel(message)
        self.layout.addWidget(self.message_label)
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide)
        self.timer.start(5000)  # Toast duration is 5 seconds
