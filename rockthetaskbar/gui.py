
import sys
import copy

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QApplication

from rockthetaskbar.cpumonitor import CPUMonitor
from rockthetaskbar.cpudialog import CPUDialog
from rockthetaskbar.about import AboutDialog


class RockTheTaskBarSystemTray(QSystemTrayIcon):
    def __init__(self):

        from rockthetaskbar import icons
        icon = QIcon(QPixmap(':icon.png'))
        super().__init__(icon)

        menu = QMenu()
        menu.addAction("CPU").triggered.connect(self.cpu)
        menu.addAction("About").triggered.connect(self.about)
        menu.addAction("Exit").triggered.connect(self.exit)
        self.setContextMenu(menu)

        self.cpu_monitor = CPUMonitor()
        self.cpu_monitor.start()

    def cpu(self):
        cpu_dialog = CPUDialog(copy.deepcopy(self.cpu_monitor.get_performance_histogram()))
        cpu_dialog.exec_()

    def about(self):
        about_box = AboutDialog()
        about_box.exec_()

    def exit(self):
        self.cpu_monitor.request_exit()
        self.cpu_monitor.join()
        QApplication.exit()


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # so popup dialogs don't close the system tray icon
    system_tray = RockTheTaskBarSystemTray()
    system_tray.show()
    app.exec_()