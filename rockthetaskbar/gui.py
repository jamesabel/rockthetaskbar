
import sys
import copy


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel, QSystemTrayIcon, QMenu, QDialog, QApplication

import rockthetaskbar
import rockthetaskbar.cpumonitor


class About(QDialog):
    def __init__(self):
        super().__init__()  # todo: fill in parameter?
        self.setWindowTitle(rockthetaskbar.__application_name__)
        layout = QGridLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel('RockTheTaskBar - "hello world" for a task bar MacOS/Windows app'))
        layout.addWidget(QLabel('Author: %s' % rockthetaskbar.__author__))
        layout.addWidget(QLabel('Source: %s' % rockthetaskbar.__url__))
        self.show()


class PropMTimeSystemTray(QSystemTrayIcon):
    def __init__(self):

        from rockthetaskbar import icons
        icon = QIcon(QPixmap(':icon.png'))
        super().__init__(icon)

        menu = QMenu()
        menu.addAction("CPU").triggered.connect(self.cpu)
        menu.addAction("About").triggered.connect(self.about)
        menu.addAction("Exit").triggered.connect(self.exit)
        self.setContextMenu(menu)

        self.cpu_monitor = rockthetaskbar.cpumonitor.CPUMonitor()
        self.cpu_monitor.start()

    def cpu(self):
        rockthetaskbar.cpumonitor.cpu_graph(copy.deepcopy(self.cpu_monitor.performance_histogram))

    def about(self):
        about_box = About()
        about_box.exec_()

    def exit(self):
        self.cpu_monitor.request_exit()
        self.cpu_monitor.join()
        QApplication.exit()  # todo: what should this parameter be?


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # so popup dialogs don't close the system tray icon
    system_tray = PropMTimeSystemTray()
    system_tray.show()
    app.exec_()