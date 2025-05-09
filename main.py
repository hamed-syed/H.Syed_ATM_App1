
from PyQt6.QtWidgets import QApplication
from gui import ATMApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ATMApp()
    window.show()
    sys.exit(app.exec())
