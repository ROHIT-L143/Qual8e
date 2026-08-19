import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Qual8eWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qual8e")
        self.setMinimumSize(900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Qual8e")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Transfer files instantly")
        subtitle.setAlignment(Qt.AlignCenter)

        qr_placeholder = QLabel("QR CODE")
        qr_placeholder.setAlignment(Qt.AlignCenter)
        qr_placeholder.setMinimumSize(250, 250)

        status = QLabel("Waiting for device...")
        status.setAlignment(Qt.AlignCenter)

        connected = QLabel("Connected device: None")
        connected.setAlignment(Qt.AlignCenter)

        select_button = QPushButton("Select Files")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(qr_placeholder, alignment=Qt.AlignCenter)
        layout.addSpacing(20)
        layout.addWidget(status)
        layout.addWidget(connected)
        layout.addSpacing(20)
        layout.addWidget(select_button)

        central_widget.setLayout(layout)


app = QApplication(sys.argv)

window = Qual8eWindow()
window.show()

sys.exit(app.exec())