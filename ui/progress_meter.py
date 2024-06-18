from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar

class ProgressMeter(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Progress")
        self.progress_bar = QProgressBar()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        self.label.setText(f"Cleared: {value:.2f} MB")
