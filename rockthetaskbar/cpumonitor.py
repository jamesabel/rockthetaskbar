import threading
import collections
import matplotlib.pyplot as plt

import psutil

from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog


class CPUMonitorDialog(QDialog):
    def __init__(self, cpu_monitor):
        super().__init__()  # todo: fill in parameter?
        self.setWindowTitle('CPU Monitor')
        layout = QGridLayout(self)
        self.setLayout(layout)
        xs = range(0, 101)
        plt.plot(xs, [cpu_monitor.performance_histogram[x] for x in xs])
        plt.title('CPU Usage Histogram')
        plt.ylabel('Count')
        plt.xlabel('CPU %')
        plt.show()


class CPUMonitor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.exit_event = threading.Event()
        self.performance_histogram = collections.defaultdict(int)

    def run(self):
        while not self.exit_event.is_set():
            self.exit_event.wait(1)
            self.performance_histogram[int(psutil.cpu_percent() + 0.5)] += 1

    def request_exit(self):
        self.exit_event.set()