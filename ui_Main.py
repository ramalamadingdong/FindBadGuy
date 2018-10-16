from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 480)

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

        """
        #PushButton2
        self.PushButton2 = QtWidgets.QPushButton(self.stack1)
        self.PushButton2.setText("BUTTON 2")
        self.PushButton2.setGeometry(QtCore.QRect(150, 150, 100, 100))
        """

    def Window2UI(self):
        self.FontColor = "color: #839496"
        self.BackColor = "background-color: #fdf6e3;"

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

        userT = QtWidgets.QLabel("User:")
        usernameT = QtWidgets.QLabel("Username:")
        homeTownT = QtWidgets.QLabel("Home Town:")
        bioT = QtWidgets.QLabel("Bio:")
        dateT = QtWidgets.QLabel("Date:")
        textT = QtWidgets.QLabel("Tweet:")

        self.labelSheets = "font-family: Times New Roman, Times, sans-serif;" \
                      "color: #cb4b16;"

        userT.setStyleSheet(self.labelSheets)
        usernameT.setStyleSheet(self.labelSheets)
        homeTownT.setStyleSheet(self.labelSheets)
        bioT.setStyleSheet(self.labelSheets)
        dateT.setStyleSheet(self.labelSheets)
        textT.setStyleSheet(self.labelSheets)

        layout.addWidget(userT, 0, 0)
        layout.addWidget(usernameT, 1, 0)
        layout.addWidget(homeTownT, 2, 0)
        layout.addWidget(bioT, 3, 0)
        layout.addWidget(dateT, 4, 0)
        layout.addWidget(textT, 0, 2)

        self.userL = QtWidgets.QLabel()
        self.usernameL = QtWidgets.QLabel()
        self.homeTownL = QtWidgets.QLabel()
        self.bioL = QtWidgets.QLabel()
        self.dateL = QtWidgets.QLabel()
        self.textL = QtWidgets.QLabel()

        self.userL.setWordWrap(True)
        self.usernameL.setWordWrap(True)
        self.homeTownL.setWordWrap(True)
        self.bioL.setWordWrap(True)
        self.dateL.setWordWrap(True)
        self.textL.setWordWrap(True)

        self.userL.setFixedWidth(145)
        self.userL.setFixedHeight(40)
        self.usernameL.setFixedWidth(145)
        self.homeTownL.setFixedWidth(145)
        self.bioL.setFixedWidth(145)
        self.dateL.setFixedWidth(145)
        self.textL.setFixedWidth(400)

        self.textL.setStyleSheet(self.FontColor)

        layout.addWidget(self.userL, 0, 1)
        layout.addWidget(self.usernameL, 1, 1)
        layout.addWidget(self.homeTownL, 2, 1)
        layout.addWidget(self.bioL, 3, 1)
        layout.addWidget(self.dateL, 4, 1)
        layout.addWidget(self.textL, 0, 3)

        layout.addWidget(self.linkBtn, 5, 2)
        layout.addWidget(self.nextBtn, 5, 3)
        layout.addWidget(self.darkBtn, 0, 5)
        self.stack2.setLayout(layout)

        #self.stack2.setStyleSheet("background: red")
