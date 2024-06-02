import sys
from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QLineEdit, QInputDialog)

class MW(QMainWindow):
    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QVBoxLayout()  # 레이아웃을 여기에서 정의해야 합니다.

        l_buttons = ['getText', 'getMultilineText', 'getInt'] 
        for idx, c_str in enumerate(l_buttons): 
            button = QPushButton(c_str)
            button.clicked.connect(self.slot00)
            layout.addWidget(button)

        self.ret_label = QLabel()
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        sender = self.sender()
        tmp_str = sender.text()
        ret_val = ""
        is_ok = False  # 변수 초기화 위치 수정

        if tmp_str == 'getText':  # 조건문 수정
            ret_val, is_ok = QInputDialog.getText(
                self,
                "Input Text",
                "Enter Your Text!",
                QLineEdit.PasswordEchoOnEdit,
                "default text!",
            )
        elif tmp_str == 'getMultilineText':  # 조건문 수정
            ret_val, is_ok = QInputDialog.getMultiLineText(
                self,
                "Input Multi-Line Text",
                "Enter Your Multi-Line Text!",
            )
            
        elif tmp_str == 'getInt':
            ret_val, is_ok = QInputDialog.getInt(
                self,
                "Input Integer",
                    "Enter Your Int Value!",
                    0,
                    0, 100,
                    3,
            )

        if is_ok:
            self.ret_label.setText(f'{ret_val}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())