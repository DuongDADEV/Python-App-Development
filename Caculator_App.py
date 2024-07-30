# 1.Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

# 2. Tạo lớp CalcApp kế thừa từ QWidget
class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # App Settings
        self.setWindowTitle("Caculator App")
        self.resize(250, 300)

        # 3. Tạo ô nhập liệu và các nút bấm
        self.text_box = QLineEdit()  # Create ô nhập liệu
        self.text_box.setFont(QFont("Helvetica", 32)) # Đổi font chữ

        self.grid = QGridLayout() # Create lưới

        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ] # List buttons

        # 4. Tạo và sắp xếp các nút bấm vào lưới
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text) # Tạo nút bấm với ký tự tương ứng
            button.clicked.connect(self.button_click) # Kết nối sự kiện click của nút bấm với hàm xử lý button_click
            button.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }") # Tạo kiểu nút bấm
            self.grid.addWidget(button, row, col) # Thêm nút bấm vào lưới tại vị trí (row, col).
            col += 1

            if col > 3:
                col = 0
                row += 1

        # 5. Tạo các nút đặc biệt và đặt vào layout
        self.clear = QPushButton("Clear") 
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
        self.delete.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
         

        # 6. Sắp xếp tất cả vào layout chính
        master_layout = QVBoxLayout() # Tạo layout chính dạng dọc
        master_layout.addWidget(self.text_box) # Thêm ô nhập liệu vào layout chính 
        master_layout.addLayout(self.grid) # Thêm lưới các nút bấm vào layout chính

        button_row = QHBoxLayout() # Tạo layout chính dạng ngang cho các nút đặc biệt
        button_row.addWidget(self.clear) # Thêm nút clear vào layout
        button_row.addWidget(self.delete) # Thêm nút delete vào layout
        master_layout.addLayout(button_row) # Thêm layout ngang vào layout chính.
        master_layout.setContentsMargins(25, 25, 25, 25) # Set Margin Đặt lề cho layout chính

        self.setLayout(master_layout) # Đặt layout chính cho cửa sổ.

        # Kết nối sự kiện click của các nút đặc biệt với hàm xử lý button_click.
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)


    # 7. Xử lý sự kiện khi nút bấm được click
    def button_click(self):
        button = app.sender() # Lấy nút bấm đã phát sinh sự kiện.
        text = button.text() # Lấy văn bản trên nút bấm.

        if text == "=":
            symbol = self.text_box.text() # Lấy biểu thức từ ô nhập liệu.

            # Thử tính toán biểu thức và hiển thị kết quả. Nếu có lỗi, in ra lỗi.
            try:
                result = eval(symbol)
                self.text_box.setText(str(result))

            except Exception as e:
                print("Error:", e)

        # Nếu nút "Clear" được bấm, xóa ô nhập liệu.
        elif text == "Clear":
            self.text_box.clear() 

        # Nếu nút "<" được bấm, xóa ký tự cuối cùng của ô nhập liệu.
        elif text == "<": 
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else: # Thêm văn bản của nút bấm vào ô nhập liệu.
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


# 8. Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication([]) # Tạo ứng dụng PyQt5.      
    main_window = CalcApp() # Tạo cửa sổ chính.
    main_window.setStyleSheet("QWidget { background-color: #f0f0f8}") # Đặt màu nền cho cửa sổ chính.
    main_window.show() # Hiển thị cửa sổ chính.
    app.exec_() # Bắt đầu vòng lặp sự kiện của ứng dụng.

"""
    Khi chạy trực tiếp:
    Python đặt __name__ của script đó là "__main__".
    Điều kiện if __name__ == "__main__": sẽ đúng.
    Bất kỳ đoạn mã nào nằm trong khối if __name__ == "__main__": sẽ được thực thi.
    Khi import vào module khác:

    Python đặt __name__ của script đó là tên của module (tên file).
    Điều kiện if __name__ == "__main__": sẽ sai.
    Bất kỳ đoạn mã nào nằm trong khối if __name__ == "__main__": sẽ không được thực thi.
"""

