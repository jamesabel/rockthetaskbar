
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QApplication, QDialog, QGridLayout, QLabel


class HelloWorldSystemTray(QSystemTrayIcon):
    def __init__(self):

        import icons
        icon = QIcon(QPixmap(':icon.png'))
        super().__init__(icon)

        menu = QMenu()
        menu.addAction("About").triggered.connect(self.about)
        menu.addAction("Exit").triggered.connect(self.exit)
        self.setContextMenu(menu)

    def about(self):
        about_box = QDialog()
        layout = QGridLayout(about_box)
        layout.addWidget(QLabel('hello world'))
        about_box.setLayout(layout)
        about_box.show()
        about_box.exec_()

    def exit(self):
        QApplication.exit()


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)  # so popup dialogs don't close the system tray icon
system_tray = HelloWorldSystemTray()
system_tray.show()
app.exec_()


