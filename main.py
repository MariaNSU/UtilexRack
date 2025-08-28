import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QApplication)
from PyQt5.QtGui import QFont
from Coil.CoilTab import CoilTab
from Input.IntInputTab import IntInputTab
from Input.FloatInputTab import FloatInputTab


class UtilexMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Utilex Control Panel")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 14, QFont.Bold))
        self.main_layout.addWidget(self.tab_widget)

        self.coil_tab = CoilTab()
        self.tab_widget.addTab(self.coil_tab, "Coil Регистры")

        self.int_input_tab = IntInputTab()
        self.tab_widget.addTab(self.int_input_tab, "Int Input Регистры")

        self.float_input_tab = FloatInputTab()
        self.tab_widget.addTab(self.float_input_tab, "Float Input Регистры")

        self.holding_tab = QWidget()
        self.tab_widget.addTab(self.holding_tab, "Holding Регистры")

    def load_test_data(self):
        self.int_input_tab.update_register(1, 1)
        self.int_input_tab.update_register(6, 1500)
        self.int_input_tab.update_register(15, 30)

        self.float_input_tab.update_register(2, 22.5)
        self.float_input_tab.update_register(4, 18.3)
        self.float_input_tab.update_register(7, 75.8)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UtilexMainWindow()
    window.load_test_data()
    window.show()
    sys.exit(app.exec_())