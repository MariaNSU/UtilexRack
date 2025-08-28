from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtGui import QFont
from Holding.HoldingRegisterWidget import HoldingRegisterWidget


class FloatHoldingWidget(HoldingRegisterWidget):
    def __init__(self, name, address, restr_ar=None, parent=None):
        super().__init__(name, address, "float", parent)
        if restr_ar is None:
            restr_ar = [-1000, 1000]
        self.create_double_spinbox(restr_ar)

    def create_double_spinbox(self, restr_ar):
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setDecimals(2)  # 2 знака после запятой
        self.spinbox.setRange(restr_ar[0], restr_ar[1])
        self.spinbox.setFont(QFont("Arial", 10))
        self.spinbox.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #e8f8f5;
                border: 2px solid #7dcea0;
                border-radius: 4px;
                padding: 5px;
                min-width: 100px;
            }
            QDoubleSpinBox:hover {
                border: 2px solid #52be80;
            }
        """)

        self.layout().addWidget(self.spinbox)

    def get_value(self):
        return self.spinbox.value() if self.spinbox else 0.0

    def set_value(self, value):
        if self.spinbox:
            self.spinbox.setValue(float(value))