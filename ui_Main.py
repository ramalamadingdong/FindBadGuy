from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(600, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()

        self.Window1UI()
        self.Window2UI()

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

    def Window1UI(self):
        self.stack1.resize(400, 120)

        layout = QtWidgets.QGridLayout()

        self.query = QtWidgets.QLineEdit()
        self.geo = QtWidgets.QLineEdit()

        queryLabel = QtWidgets.QLabel("Query:")
        geoLabel = QtWidgets.QLabel("Geo:")

        self.submitBtn = QtWidgets.QPushButton(self.stack1)
        self.submitBtn.setText("Submit")
        self.submitBtn.setGeometry(QtCore.QRect(10, 10, 100, 100))

        layout.addWidget(queryLabel, 0, 0)
        layout.addWidget(self.query, 0, 1)

        layout.addWidget(geoLabel, 1, 0)
        layout.addWidget(self.geo, 1, 1)

        layout.addWidget(self.submitBtn, 1, 2)

        self.stack1.setLayout(layout)

    def Window2UI(self):

        self.FontColor = ""
        self.BackColor = ""

        self.stack2.setFixedSize(800, 480)

        self.stack2.setStyleSheet(self.BackColor)

        self.darkBtn = QtWidgets.QPushButton('Dark')
        self.darkBtn.setCheckable(True)

        layout = QtWidgets.QGridLayout()

        self.linkBtn = QtWidgets.QPushButton(self.stack2)
        self.linkBtn.setText("Link")
        self.linkBtn.setGeometry(QtCore.QRect(10, 10, 100, 100))

        self.nextBtn = QtWidgets.QPushButton(self.stack2)
        self.nextBtn.setText("Next")
        self.nextBtn.setGeometry(QtCore.QRect(10, 10, 100, 100))

        self.prevBtn = QtWidgets.QPushButton(self.stack2)
        self.prevBtn.setText("Previous")
        self.prevBtn.setGeometry(QtCore.QRect(10, 10, 100, 100))

        self.showPic = QtWidgets.QPushButton(self.stack2)
        self.showPic.setText("Show Pic")
        self.showPic.setCheckable(True)
        self.showPic.setGeometry(QtCore.QRect(10, 10, 100, 100))


        userT = QtWidgets.QLabel("User:")
        usernameT = QtWidgets.QLabel("Username:")
        bioT = QtWidgets.QLabel("Bio:")

        self.homeTownT = QtWidgets.QLabel("Home:")
        self.dateT = QtWidgets.QLabel("Date:")

        self.geoT = QtWidgets.QLabel("Geo:")

        self.labelSheets = "color: #dc322f;"

        userT.setStyleSheet(self.labelSheets)
        usernameT.setStyleSheet(self.labelSheets)
        bioT.setStyleSheet(self.labelSheets)

        self.geoT.setStyleSheet(self.labelSheets)

        self.homeTownT.setStyleSheet(self.labelSheets)
        self.dateT.setStyleSheet(self.labelSheets)

        layout.addWidget(userT, 0, 1, 0, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        layout.addWidget(usernameT, 1, 1, 1, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        layout.addWidget(bioT, 2, 1, 2, 1, QtCore.Qt.AlignTop| QtCore.Qt.AlignRight)

        layout.addWidget(self.dateT, 0, 2, 0, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        layout.addWidget(self.homeTownT, 1, 2, 1, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

        layout.addWidget(self.geoT, 2, 2, 2, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

        self.userL = QtWidgets.QLabel()
        self.usernameL = QtWidgets.QLabel()
        self.homeTownL = QtWidgets.QLabel()
        self.bioL = QtWidgets.QLabel()
        self.dateL = QtWidgets.QLabel()
        self.textL = QtWidgets.QLabel()

        self.geoL = QtWidgets.QLabel()

        self.textL.setFixedWidth(350)
        self.bioL.setFixedWidth(150)

        self.userL.setWordWrap(True)
        self.usernameL.setWordWrap(True)
        self.homeTownL.setWordWrap(True)
        self.bioL.setWordWrap(True)
        self.dateL.setWordWrap(True)
        self.textL.setWordWrap(True)
        self.textL.setFont(QtGui.QFont("Helvetica", 16))
        self.picL = QtWidgets.QLabel()

        self.picL.show()

        layout.addWidget(self.picL, 3, 0)

        layout.addWidget(self.textL, 0, 0, 0, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        layout.addWidget(self.usernameL, 1, 2, 1, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        layout.addWidget(self.userL, 0, 2, 0, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        layout.addWidget(self.bioL, 2, 2, 2, 2, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        layout.addWidget(self.homeTownL, 1, 4, 1, 4, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        layout.addWidget(self.dateL, 0, 4, 0, 4, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        layout.addWidget(self.geoL, 2, 4, 2, 4, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.linkBtn.setStyleSheet("QPushButton { background-color: blue }"
                                   "QPushButton:pressed { background-color: red }")

        self.nextBtn.setStyleSheet("QPushButton { background-color: blue }"
                                   "QPushButton:pressed { background-color: red }")

        self.prevBtn.setStyleSheet("QPushButton { background-color: blue }"
                                   "QPushButton:pressed { background-color: red }")

        layout.addWidget(self.linkBtn, 5, 0)
        layout.addWidget(self.nextBtn, 5, 2)
        layout.addWidget(self.prevBtn, 5, 1)

        layout.addWidget(self.showPic, 4, 0)

        layout.setColumnMinimumWidth(0, 450)
        layout.setColumnMinimumWidth(2, 150)
        layout.setColumnMinimumWidth(4, 100)
        layout.setColumnMinimumWidth(1, 50)
        layout.setColumnMinimumWidth(3, 50)

        self.stack2.setLayout(layout)
