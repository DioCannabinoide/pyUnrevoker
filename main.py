from backend.device_manager import DeviceManager
from backend.mainwindow import MainWindow
from pymobiledevice3 import usbmux
from PySide6.QtWidgets import QApplication
import sys
from tweak.authorization import UnrevokeTweak

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dev_manager = DeviceManager()

    tweak = UnrevokeTweak()

    window = MainWindow(dev_manager, tweak)
    window.show()

    sys.exit(app.exec())
