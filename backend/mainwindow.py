from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import webbrowser

class MainWindow(QMainWindow):
    def __init__(self, deviceManager, tweak):
        super().__init__()

        self.dev_manager = deviceManager
        self.tweak = tweak
        self.setWindowTitle("EUEnabler")
        self.setFixedSize(960, 540)
        self.setWindowIcon(QIcon("icon.png"))
        screen_geometry = QApplication.primaryScreen().availableGeometry()

        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        self.move(x, y)
        self.setupUI()

    def setupUI(self):
        self.main = QWidget(self)

        self.logoBtn = QToolButton(self.main)
        self.logoBtn.setObjectName(u"logoBtn")
        self.logoBtn.setFixedSize(200, 200)
        self.logoBtn.move((self.width() - self.logoBtn.width()) // 2, 50)
        self.logoBtn.setStyleSheet(u"QToolButton {\n"
        "	background-color: transparent;\n"
        "	padding: 0px;\n"
        "   border: none;\n"
        "}")

        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoBtn.setIcon(icon)
        self.logoBtn.setIconSize(QSize(400, 400))
        self.logoBtn.clicked.connect(self.logoBtn_callback)

        self.EUText = QLabel("EUEnabler", self)
        font = QFont()
        font.setBold(True)
        font.setPointSize(24)
        self.EUText.setFont(font)
        self.EUText.setFixedSize(self.width(), 50)
        self.EUText.move(0, 245)
        self.EUText.setAlignment(Qt.AlignCenter)

        self.deviceText = QLabel("", self)
        font.setBold(False)
        font.setPointSize(16)
        self.deviceText.setFont(font)
        self.deviceText.setFixedSize(self.width(), 50)
        self.deviceText.move(0, 275)
        self.deviceText.setAlignment(Qt.AlignCenter)
        self.deviceText.setText(self.dev_manager.device.get("name") if len(self.dev_manager.devices) != 0 else "No device connected!")

        icon = QIcon()
        icon.addFile(u"icon/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.applyBtn = QToolButton(self)
        self.applyBtn.setObjectName(u"applyBtn")
        self.applyBtn.setFixedSize(36, 36)
        self.applyBtn.setStyleSheet(u"QToolButton {\n"
        "	background-color: transparent;\n"
        "	padding: 0px;\n"
        "   border: none;\n"
        "}\n"
        "QToolButton:pressed {\n"
        "    opacity: 0.5;\n"
        "}")
        self.applyBtn.setIcon(icon)
        self.applyBtn.setIconSize(QSize(36, 36))
        self.applyBtn.clicked.connect(self.applyBtn_callback)
        self.applyBtn.move((self.width() - self.applyBtn.width()) // 2, 478)

        self.setCentralWidget(self.main)

    def logoBtn_callback(self):
        webbrowser.open("https://github.com/nightfallenxyz/EUEnabler-ASH")

    def applyBtn_callback(self):
        self.tweak.apply()