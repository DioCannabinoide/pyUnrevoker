from backend.device_manager import DeviceManager
from backend.mainwindow import MainWindow
from pymobiledevice3 import usbmux
from PySide6.QtWidgets import QApplication
import sys
from tweak.authorization import AuthorizationTweak

if __name__ == "__main__":
    app = QApplication(sys.argv)

    device_manager = DeviceManager()

    authorization_tweak = AuthorizationTweak()

    window = MainWindow(device_manager, authorization_tweak)
    window.show()

    sys.exit(app.exec())
