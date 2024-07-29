# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout


class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # App Settings
        self.setWindowTitle("Caculator App")
        self.resize(250, 300)

        # Create all Widgets
        self.text_box = QLineEdit()  # Create thanh nhập
        self.grid = QGridLayout()

        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]
         # Loop for creating buttons
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")

        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)     
        self.setLayout(master_layout)
        
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)


    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                result = eval(symbol)
                self.text_box.setText(str(result))

            except Exception as e:
                print("Error:", e)

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


if __name__ in "__main__":
    # Show/Run
    app = QApplication([])      
    main_window = CalcApp()
    main_window.show()
    app.exec_()

print("Trần Thành Dương")
