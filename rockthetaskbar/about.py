
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog

import rockthetaskbar


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()  # todo: fill in parameter?
        self.setWindowTitle(rockthetaskbar.__application_name__)
        layout = QGridLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel('RockTheTaskBar - "hello world" for a task bar MacOS/Windows app'))
        layout.addWidget(QLabel('Author: %s' % rockthetaskbar.__author__))
        layout.addWidget(QLabel('Source: %s' % rockthetaskbar.__url__))
        self.show()
