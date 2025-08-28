from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Input.UpdateButton import UpdateButton

class BaseHoldingTab(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.registers = {}
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("QScrollArea { border: none; }")

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setSpacing(8)

        self.scroll.setWidget(self.container)

        self.update_button = UpdateButton()
        self.update_button.clicked.connect(self.on_update_data)

        self.save_button = QPushButton("Сохранить все значения")
        self.save_button.setFixedHeight(50)
        self.save_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: 2px solid #219a52;
                border-radius: 8px;
                padding: 10px 20px;
                margin: 10px 15px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
                border: 2px solid #27ae60;
            }
            QPushButton:pressed {
                background-color: #219a52;
            }
        """)
        self.save_button.clicked.connect(self.on_save_data)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.save_button)

        main_layout.addWidget(title_label)
        main_layout.addWidget(scroll)
        main_layout.addLayout(button_layout)

    def on_update_data(self):
        """Обновить данные с устройства"""
        print(f"Обновление данных для {self.title}")

    def on_save_data(self):
        """Сохранить все значения на устройство"""
        print(f"Сохранение данных для {self.title}")
        values = self.get_all_values()
        print("Значения для сохранения:", values)

    def get_all_values(self):
        """Получить все значения регистров"""
        return {address: widget.get_value() for address, widget in self.registers.items()}

    def set_all_values(self, values_dict):
        """Установить все значения регистров"""
        for address, value in values_dict.items():
            if address in self.registers:
                self.registers[address].set_value(value)

