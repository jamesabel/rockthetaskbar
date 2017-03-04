
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel, QSystemTrayIcon, QMenu, QDialog, QApplication

import rockthetaskbar


class About(QDialog):
    def __init__(self):
        super().__init__()  # todo: fill in parameter?
        self.setWindowTitle(rockthetaskbar.__application_name__)
        layout = QGridLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel('Source: %s' % rockthetaskbar.__url__))


class PropMTimeSystemTray(QSystemTrayIcon):
    def __init__(self):

        from rockthetaskbar import icons
        icon = QIcon(QPixmap(':icon.png'))
        super().__init__(icon)

        menu = QMenu()
        menu.addAction("Info").triggered.connect(self.paths)
        menu.addAction("About").triggered.connect(self.about)
        menu.addAction("Exit").triggered.connect(self.exit)
        self.setContextMenu(menu)

    def paths(self):
        pass

    def about(self):
        about_box = About()
        about_box.exec()

    def exit(self):
        QApplication.exit()  # todo: what should this parameter be?


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # so popup dialogs don't close the system tray icon
    system_tray = PropMTimeSystemTray()
    system_tray.show()
    app.exec_()