import sys
from PySide6.QtWidgets import (QApplication, 
               QMainWindow, QPushButton, 
               QVBoxLayout, QMessageBox)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog.warning Example')
        button = QPushButton('Press me for a dialog!', self)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        self.show()

    def button_clicked(self, s):
        # built-in dialog 테스트를 위한 method.
        print("click", s)
            # 정보 대화 상자 표시
        result = QMessageBox.warning(
                   self, 
                   'Warning', 
                   'This is a warning message.',
                   QMessageBox.Ok | QMessageBox.Cancel, 
                   QMessageBox.Ok)

        # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    app.exec()