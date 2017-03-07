
import psutil
from PyQt5.QtWidgets import QGridLayout, QDialog

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