import sys
import qrcode

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class Qual8eWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qual8e")
        self.setMinimumSize(900, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Qual8e")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Scan to connect")
        subtitle.setAlignment(Qt.AlignCenter)

        # Temporary connection data
        connection_data = "QUAL8E_SESSION_TEST"

        # Generate QR code
        qr = qrcode.make(connection_data)

        # Save QR temporarily
        qr_path = "qual8e_qr.png"
        qr.save(qr_path)

        # Display QR
        qr_label = QLabel()
        pixmap = QPixmap(qr_path)
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter)

        status = QLabel("Waiting for device...")
        status.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(qr_label)
        layout.addSpacing(20)
        layout.addWidget(status)

        central_widget.setLayout(layout)


app = QApplication(sys.argv)

window = Qual8eWindow()
window.show()

sys.exit(app.exec())