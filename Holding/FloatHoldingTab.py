
class FloatHoldingTab(BaseHoldingTab):
    """Вкладка для float Holding регистров"""

    def __init__(self, parent=None):
        super().__init__("FLOAT Holding Регистры", parent)
        self.create_float_registers()

    def create_float_registers(self):
        """Создаем float Holding регистры"""
        float_registers = [
            ("Уставка температуры", 301),
            ("Аварийный порог влажности", 305),
            ("Аварийный порог температуры", 307),
            ("Предупредит порог температуры", 309),
            ("Предупредит порог влажности", 311),
            ("P", 314),
            ("I", 316),
            ("D", 318),
            ("Аварийный порог температуры воды", 320),
            ("Предупредит порог Т воды", 322)
        ]

        for name, address in float_registers:
            self.add_register(name, address)

    def add_register(self, name, address):
        """Добавить float регистр"""
        register_widget = FloatHoldingWidget(name, address)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)