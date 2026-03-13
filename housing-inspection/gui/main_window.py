from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from app.inspection_controller import InspectionController

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Housing Inspection")

        self.controller = InspectionController()

        self.button = QPushButton("검사 시작")
        self.result = QLabel("결과: 대기중")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.button.clicked.connect(self.inspect)

    def inspect(self):
        result = self.controller.run_inspection()

        if result:
            self.result.setText("결과: 정상")
        else:
            self.result.setText("결과: 불량")
