
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QFormLayout, QLabel)
from PyQt5.QtGui import QPixmap

#QWidget to display the button layout for user input of parameter
class input_form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Labels for input boxes
        label1=QLabel()
        label1.setText("Sample Rate")
        label1.setAlignment(Qt.AlignLeft)
        label2=QLabel()
        label2.setText("Angular Resolution")
        label2.setAlignment(Qt.AlignLeft)
        label3=QLabel()
        label3.setText("Distance to Wait")
        label3.setAlignment(Qt.AlignLeft)


        logo=QLabel()
        logo.setPixmap(QPixmap("python.jpg"))

        #Integer inputs for scan settings
        in1=QLineEdit("Sample Rate")
        in2=QLineEdit("Angular Resolution")
        in3=QLineEdit("Distance to Wait")

        #adding buttons to grid layout
        form=QFormLayout()
        form.addRow(label1,in1)
        form.addRow(label2,in2)
        form.addRow(label3,in3)

        #Create start/stop scan Buttons with layout
        self.start=QPushButton("Start")
        self.stop=QPushButton("Stop")

        ctrl=QHBoxLayout()
        ctrl.addWidget(self.start)
        ctrl.addWidget(self.stop)

        b_h = QHBoxLayout ()
        b_h.addLayout(form)
        b_h.addStretch(1)
        b_h.addWidget(logo)

        vbox = QVBoxLayout()
        vbox.addLayout(ctrl)
        vbox.addStretch(1)
        vbox.addLayout(b_h)

        self.setLayout(vbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window=input_form()
    sys.exit(app.exec_())
