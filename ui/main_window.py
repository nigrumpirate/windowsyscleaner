
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import Qt
from core.cache_cleaner import CacheCleaner
from core.temp_cleaner import TempCleaner
from ui.progress_meter import ProgressMeter
from ui.toast import Toast

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Cleaner")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(open("assets/styles.qss", "r").read())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.progress_meter = ProgressMeter()
        self.layout.addWidget(self.progress_meter, alignment=Qt.AlignCenter)

        self.optimize_button = QPushButton("Optimize System")
        self.optimize_button.setFixedSize(150, 50)
        self.optimize_button.clicked.connect(self.optimize_system)
        self.layout.addWidget(self.optimize_button, alignment=Qt.AlignCenter)

    def show_toast(self, message):
        toast = Toast(message, self)
        toast.move(self.width() // 2 - toast.width() // 2, self.height() - 100)
        toast.show()

    def optimize_system(self):
        cache_cleaner = CacheCleaner()
        temp_cleaner = TempCleaner()

        cache_cleared = cache_cleaner.clear()
        temp_cleared = temp_cleaner.delete()

        total_cleared = cache_cleared + temp_cleared
        self.progress_meter.update_progress(total_cleared)
        self.show_toast(f"System optimized. Cleared {total_cleared:.2f} MB")
