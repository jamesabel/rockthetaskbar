
import threading
import collections

import psutil


class CPUMonitor(threading.Thread):
    def __init__(self):
        super().__init__()
        self._exit_event = threading.Event()
        self._performance_histogram = collections.defaultdict(int)

    def run(self):
        while not self._exit_event.is_set():
            self._performance_histogram[int(psutil.cpu_percent() + 0.5)] += 1
            self._exit_event.wait(1)  # periodically poll

    def get_performance_histogram(self):
        return self._performance_histogram

    def request_exit(self):
        self._exit_event.set()
