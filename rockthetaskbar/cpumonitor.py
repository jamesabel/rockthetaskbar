
import threading
import collections
import matplotlib.pyplot as plt

import psutil


def cpu_graph(histogram):
    xs = range(0, 101)
    plt.plot(xs, [histogram[x] for x in xs])
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
            self.performance_histogram[int(psutil.cpu_percent() + 0.5)] += 1
            self.exit_event.wait(1)  # periodically poll

    def request_exit(self):
        self.exit_event.set()
