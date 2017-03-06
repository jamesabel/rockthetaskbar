
import sys
import copy

import psutil
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel, QSystemTrayIcon, QMenu, QDialog, QApplication

import rockthetaskbar
import rockthetaskbar.cpumonitor

# don't use matplotlib.pyplot (you'll end up with a windowing problem)
# see: http://stackoverflow.com/questions/29992771/combining-pyqt-and-matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator


class CPUDialog(QDialog):
    def __init__(self, cpu_histogram):
        super().__init__()

        # set up the graphical elements
        layout = QGridLayout(self)
        self.setLayout(layout)
        fig = Figure()
        layout.addWidget(FigureCanvas(fig))

        # do the plotting
        ax = fig.add_subplot(1, 1, 1)  # 1x1 grid, first subplot
        ax.set_title('CPU Usage Histogram (%s Cores/%s Threads)' % (psutil.cpu_count(False), psutil.cpu_count(True)))
        ax.set_ylabel('Count')
        ax.set_xlabel('CPU %')
        ax.grid(True)
        xs = range(0, 101)
        ax.plot(xs, [cpu_histogram[x] for x in xs])
        ax.xaxis.set_major_locator(MultipleLocator(10.))

        self.show()


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
        cpu_dialog = CPUDialog(copy.deepcopy(self.cpu_monitor.get_performance_histogram()))
        cpu_dialog.exec_()

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