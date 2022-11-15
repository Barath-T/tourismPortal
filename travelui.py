
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket

import eventHand


class Ui_MainWindow(object):
    def __init__(self, client:socket.socket) -> None:
        self.client = client

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 551)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 525))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 577))
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 525))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 525))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 525))
        self.mainStackedWidget.setMinimumSize(QtCore.QSize(1200, 525))
        self.mainStackedWidget.setMaximumSize(QtCore.QSize(1200, 525))
        self.mainStackedWidget.setStyleSheet("\n"
"QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QStackedWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"    border-radius:10px;\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(142, 142, 213);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(170, 170, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(111, 111, 166);\n"
"    font-size: 12pt;\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid  rgb(111, 111, 166);\n"
"    border-radius: 10px;\n"
"}")
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.welcomePage = QtWidgets.QWidget()
        self.welcomePage.setMinimumSize(QtCore.QSize(1200, 525))
        self.welcomePage.setMaximumSize(QtCore.QSize(1200, 525))
        self.welcomePage.setStyleSheet("\n"
"\n"
"#welcomePage{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#welcomeLabel{\n"
"     color: rgb(142, 142, 213);\n"
"    font: italic 24pt \"Harlow Solid Italic\";\n"
"}\n"
"\n"
"#welcomeSignupButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background: none;\n"
"}\n"
"#welcomeSignupButton:hover {\n"
"    color: rgb(170, 170, 255);\n"
"    background: none;\n"
"}")
        self.welcomePage.setObjectName("welcomePage")
        self.welcomeLabel = QtWidgets.QLabel(self.welcomePage)
        self.welcomeLabel.setGeometry(QtCore.QRect(130, 200, 341, 61))
        self.welcomeLabel.setScaledContents(False)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLoginButton = QtWidgets.QPushButton(self.welcomePage)
        self.welcomeLoginButton.setGeometry(QtCore.QRect(650, 210, 231, 41))
        self.welcomeLoginButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.welcomeLoginButton.setFlat(True)
        self.welcomeLoginButton.setObjectName("welcomeLoginButton")

        self.welcomeLoginButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))

        self.welcomeSignupButton = QtWidgets.QPushButton(self.welcomePage)
        self.welcomeSignupButton.setGeometry(QtCore.QRect(650, 310, 231, 41))
        self.welcomeSignupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.welcomeSignupButton.setObjectName("welcomeSignupButton")
        
        self.welcomeSignupButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(2))

        self.mainStackedWidget.addWidget(self.welcomePage)
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setMinimumSize(QtCore.QSize(1200, 500))
        self.loginPage.setMaximumSize(QtCore.QSize(1200, 500))
        self.loginPage.setStyleSheet("QLabel{\n"
"    color: rgb(111, 111, 166);\n"
"    font-size: 12pt;\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid  rgb(111, 111, 166);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#loginButton{\n"
"    min-height: 30px;\n"
"    max-width: 110%;\n"
"    margin-top: 20%;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.loginPage.setObjectName("loginPage")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.loginPage)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(330, 160, 491, 241))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.loginForm = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.loginForm.setContentsMargins(0, 0, 0, 0)
        self.loginForm.setObjectName("loginForm")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.usernameLabel.setObjectName("usernameLabel")
        self.loginForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLabel)
        self.usernameInput = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.usernameInput.setObjectName("usernameInput")
        self.loginForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLabel)
        self.passwordInput = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.passwordInput.setStyleSheet("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.loginForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.loginButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.loginButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginButton.setObjectName("loginButton")

        self.loginButton.clicked.connect(lambda: eventHand.login(self.usernameInput.text(), self.passwordInput.text(), self.mainStackedWidget, self.client))

        self.loginForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.loginButton)
        self.loginLabel = QtWidgets.QLabel(self.loginPage)
        self.loginLabel.setGeometry(QtCore.QRect(510, 70, 95, 84))
        self.loginLabel.setStyleSheet("#loginLabel{\n"
"    font-size: 24pt;\n"
"}")
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.mainStackedWidget.addWidget(self.loginPage)
        self.registerPage = QtWidgets.QWidget()
        self.registerPage.setStyleSheet("QLabel{\n"
"    color: rgb(111, 111, 166);\n"
"    font-size: 12pt;\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid  rgb(111, 111, 166);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#registerButton{\n"
"    min-height: 30px;\n"
"    max-width: 110%;\n"
"    margin-top: 20%;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.registerPage.setObjectName("registerPage")
        self.registerLabel = QtWidgets.QLabel(self.registerPage)
        self.registerLabel.setGeometry(QtCore.QRect(450, 60, 221, 84))
        self.registerLabel.setStyleSheet("#registerLabel{\n"
"    font-size: 24pt;\n"
"}")
        self.registerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerLabel.setObjectName("registerLabel")
        self.formLayoutWidget = QtWidgets.QWidget(self.registerPage)
        self.formLayoutWidget.setGeometry(QtCore.QRect(430, 180, 271, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.registerForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.registerForm.setContentsMargins(0, 0, 0, 0)
        self.registerForm.setObjectName("registerForm")
        self.usernameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel_2)
        self.usernameInput_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameInput_2.setObjectName("usernameInput_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameInput_2)
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.phoneInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneInput.setObjectName("phoneInput")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.phoneInput)
        self.passwordLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel_2.setObjectName("passwordLabel_2")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel_2)
        self.passwordInput_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordInput_2.setStyleSheet("")
        self.passwordInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput_2.setObjectName("passwordInput_2")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordInput_2)
        self.registerButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.registerButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.registerButton.setObjectName("registerButton")

        self.registerButton.clicked.connect(lambda: eventHand.signup(self.usernameInput_2.text(), self.phoneInput.text(), self.passwordInput_2.text(), self.mainStackedWidget, self.client))

        self.registerForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.registerButton)
        self.mainStackedWidget.addWidget(self.registerPage)

        self.firstPage = QtWidgets.QWidget()
        self.firstPage.setStyleSheet("QLineEdit{\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox, QDateEdit, QSpinBox{\n"
"    border: 2px solid  rgb(111, 111, 166);\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    color: rgb(111, 111, 166);\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"#requestButton{\n"
"    min-height: 30px;\n"
"    max-width: 110%;\n"
"    margin-top: 20%;\n"
"}\n"
"")
        self.firstPage.setObjectName("firstPage")
        self.horizontalWidget = QtWidgets.QWidget(self.firstPage)
        self.horizontalWidget.setGeometry(QtCore.QRect(130, 60, 921, 171))
        self.horizontalWidget.setStyleSheet("#beforeButton, #afterButton{\n"
"    width: 50%;\n"
"    height: 50%;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 22pt \"MS PGothic\";\n"
"}\n"
"\n"
"#beforeButton:pressed, #afterButton:pressed{\n"
"    \n"
"    background-color: rgb(139, 139, 139);\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.beforeButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.beforeButton.setObjectName("beforeButton")

        self.beforeButton.clicked.connect(lambda: self.packageStackedWidget.setCurrentIndex(self.packageStackedWidget.currentIndex() - 1) if (self.packageStackedWidget.currentIndex() != 0) else print("end"))

        self.horizontalLayout.addWidget(self.beforeButton)
        self.packageStackedWidget = QtWidgets.QStackedWidget(self.horizontalWidget)
        self.packageStackedWidget.setObjectName("packageStackedWidget")
        self.packagePage_1 = QtWidgets.QWidget()
        self.packagePage_1.setStyleSheet("\n"
"#label_5, #label_6, #label_8, #label_10{\n"
"    \n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#bookNowButton{\n"
"    height: 75%;\n"
"}")
        self.packagePage_1.setObjectName("packagePage_1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.packagePage_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.bookNowButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bookNowButton.setObjectName("bookNowButton")

        self.bookNowButton.clicked.connect(lambda: eventHand.gotoBooking(0, self.mainStackedWidget))

        self.gridLayout.addWidget(self.bookNowButton, 2, 4, 1, 1)
        self.packageStackedWidget.addWidget(self.packagePage_1)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.packageStackedWidget.addWidget(self.page_2)
####################################################################################
        self.packagePage_2 = QtWidgets.QWidget()
        self.packagePage_2.setStyleSheet("\n"
"#label_2_5, #label_2_6, #label_2_8, #label_2_10{\n"
"    \n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#bookNowButton_2{\n"
"    height: 75%;\n"
"}")
        self.packagePage_2.setObjectName("packagePage_2")
        self.gridLayout_2Widget = QtWidgets.QWidget(self.packagePage_2)
        self.gridLayout_2Widget.setGeometry(QtCore.QRect(10, 10, 781, 141))
        self.gridLayout_2Widget.setObjectName("gridLayout_2Widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayout_2Widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2_4 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_4.setObjectName("label_2_4")
        self.gridLayout_2.addWidget(self.label_2_4, 1, 1, 1, 1)
        self.label_2_6 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_6.setObjectName("label_2_6")
        self.gridLayout_2.addWidget(self.label_2_6, 2, 1, 1, 1)
        self.label_2_3 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_3.setObjectName("label_2_3")
        self.gridLayout_2.addWidget(self.label_2_3, 1, 0, 1, 1)
        self.label_2_9 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_9.setObjectName("label_2_9")
        self.gridLayout_2.addWidget(self.label_2_9, 1, 3, 1, 1)
        self.label_2_7 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_7.setObjectName("label_2_7")
        self.gridLayout_2.addWidget(self.label_2_7, 1, 2, 1, 1)
        self.label_2_10 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_10.setObjectName("label_2_10")
        self.gridLayout_2.addWidget(self.label_2_10, 2, 3, 1, 1)
        self.label_2_8 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_8.setObjectName("label_2_8")
        self.gridLayout_2.addWidget(self.label_2_8, 2, 2, 1, 1)
        self.label_2_5 = QtWidgets.QLabel(self.gridLayout_2Widget)
        self.label_2_5.setObjectName("label_2_5")
        self.gridLayout_2.addWidget(self.label_2_5, 2, 0, 1, 1)
        self.bookNowButton_2 = QtWidgets.QPushButton(self.gridLayout_2Widget)
        self.bookNowButton_2.setObjectName("bookNowButton_2")

        self.bookNowButton_2.clicked.connect(lambda: eventHand.gotoBooking(1, self.mainStackedWidget))

        self.gridLayout_2.addWidget(self.bookNowButton_2, 2, 4, 1, 1)
        self.packageStackedWidget.addWidget(self.packagePage_2)
######################################################################
        self.horizontalLayout.addWidget(self.packageStackedWidget)
        self.afterButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.afterButton.setObjectName("afterButton")

        self.afterButton.clicked.connect(lambda: print('end') if (self.packageStackedWidget.currentIndex() == self.packageStackedWidget.count()-1) else self.packageStackedWidget.setCurrentIndex(self.packageStackedWidget.currentIndex() + 1))

        self.horizontalLayout.addWidget(self.afterButton)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.firstPage)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(630, 260, 341, 211))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sourceLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.sourceLabel.setObjectName("sourceLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sourceLabel)
        self.sourceComboBox = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.sourceComboBox.setObjectName("sourceComboBox")

        self.sourceComboBox.addItem("Default")
        self.sourceComboBox.addItem("Default_1")
        self.sourceComboBox.addItem("Default_2")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sourceComboBox)
        self.destinationLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.destinationLabel.setObjectName("destinationLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.destinationLabel)
        self.destinationComboBox = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.destinationComboBox.setObjectName("destinationComboBox")

        self.destinationComboBox.addItem("Default")
        self.destinationComboBox.addItem("Default_1")
        self.destinationComboBox.addItem("Default_2")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinationComboBox)
        self.startLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.startLabel.setObjectName("startLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.startLabel)
        self.startDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.startDateEdit.setObjectName("startDateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startDateEdit)
        self.endLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.endLabel.setObjectName("endLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.endLabel)
        self.endDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.endDateEdit.setObjectName("endDateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endDateEdit)
        self.countLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.countLabel.setObjectName("countLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.countLabel)
        self.countSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget_3)
        self.countSpinBox.setObjectName("countSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.countSpinBox)
        self.requestButton = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.requestButton.setObjectName("requestButton")

        self.requestButton.clicked.connect(lambda: eventHand.request(self.sourceComboBox.currentText(), self.destinationComboBox.currentText(), self.startDateEdit.text(), self.endDateEdit.text(), self.countSpinBox.text(), self.client))

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.requestButton)
        self.label = QtWidgets.QLabel(self.firstPage)
        self.label.setGeometry(QtCore.QRect(170, 300, 291, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.firstPage)
        self.label_2.setGeometry(QtCore.QRect(120, 340, 451, 51))
        self.label_2.setObjectName("label_2")
        self.mainStackedWidget.addWidget(self.firstPage)
        self.bookingPage = QtWidgets.QWidget()
        self.bookingPage.setStyleSheet("QSpinBox, QPlainTextEdit, QLineEdit{\n"
"    border: 2px solid  rgb(111, 111, 166);\n"
"    border-radius: 10px;\n"
"}\n"
"#addressInput{\n"
"    \n"
"    \n"
"}\n"
"\n"
"#confirmButton{\n"
"    height: 40%;\n"
"}")
        self.bookingPage.setObjectName("bookingPage")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.bookingPage)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(360, 110, 431, 351))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.nameInput.setObjectName("nameInput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.addressLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.noPersonLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.noPersonLabel.setObjectName("noPersonLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.noPersonLabel)
        self.noPersonInput = QtWidgets.QSpinBox(self.formLayoutWidget_4)
        self.noPersonInput.setObjectName("noPersonInput")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.noPersonInput)
        self.phoneLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.phoneLabel_2.setObjectName("phoneLabel_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phoneLabel_2)
        self.phoneInput_2 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.phoneInput_2.setObjectName("phoneInput_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.phoneInput_2)
        self.addressInput = QtWidgets.QPlainTextEdit(self.formLayoutWidget_4)
        self.addressInput.setObjectName("addressInput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addressInput)
        self.confirmButton = QtWidgets.QPushButton(self.formLayoutWidget_4)
        self.confirmButton.setObjectName("confirmButton")

        self.confirmButton.clicked.connect(lambda: eventHand.book(self.nameInput.text(), self.addressInput.toPlainText(), self.noPersonInput.text(), self.phoneInput_2.text(), self.mainStackedWidget, self.client))

        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.confirmButton)
        self.bookingHeadingLabel = QtWidgets.QLabel(self.bookingPage)
        self.bookingHeadingLabel.setGeometry(QtCore.QRect(490, 40, 181, 31))
        self.bookingHeadingLabel.setObjectName("bookingHeadingLabel")
        self.mainStackedWidget.addWidget(self.bookingPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.mainStackedWidget.setCurrentIndex(0)
        self.packageStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", "Hi, Login to travel!"))
        self.welcomeLoginButton.setText(_translate("MainWindow", "Login"))
        self.welcomeSignupButton.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.usernameLabel.setText(_translate("MainWindow", "Username: "))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.loginLabel.setText(_translate("MainWindow", "Login"))
        self.registerLabel.setText(_translate("MainWindow", "Register"))
        self.usernameLabel_2.setText(_translate("MainWindow", "Username: "))
        self.phoneLabel.setText(_translate("MainWindow", "Phone:"))
        self.passwordLabel_2.setText(_translate("MainWindow", "Password:"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.beforeButton.setText(_translate("MainWindow", "<"))
        self.label_4.setText(_translate("MainWindow", "Destination:"))
        self.label_6.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Source:"))
        self.label_9.setText(_translate("MainWindow", "End date:"))
        self.label_7.setText(_translate("MainWindow", "Start date:"))
        self.label_10.setText(_translate("MainWindow", "Default"))
        self.label_8.setText(_translate("MainWindow", "Default"))
        self.label_5.setText(_translate("MainWindow", "Default"))
        self.bookNowButton.setText(_translate("MainWindow", "Book Now"))
############################################################################################

        self.label_2_4.setText(_translate("MainWindow", "Destination:"))
        self.label_2_6.setText(_translate("MainWindow", "Default_2"))
        self.label_2_3.setText(_translate("MainWindow", "Source:"))
        self.label_2_9.setText(_translate("MainWindow", "End date:"))
        self.label_2_7.setText(_translate("MainWindow", "Start date:"))
        self.label_2_10.setText(_translate("MainWindow", "Default_2"))
        self.label_2_8.setText(_translate("MainWindow", "Default_2"))
        self.label_2_5.setText(_translate("MainWindow", "Default_2"))
        self.bookNowButton_2.setText(_translate("MainWindow", "Book Now"))
#############################################################################################
        self.afterButton.setText(_translate("MainWindow", ">"))
        self.sourceLabel.setText(_translate("MainWindow", "Source:"))
        self.destinationLabel.setText(_translate("MainWindow", "Destination:"))
        self.startLabel.setText(_translate("MainWindow", "Start Date: "))
        self.endLabel.setText(_translate("MainWindow", "End Date"))
        self.countLabel.setText(_translate("MainWindow", "No of persons:"))
        self.requestButton.setText(_translate("MainWindow", "Request a Trip"))
        self.label.setText(_translate("MainWindow", "Couldn\'t find the trip you want?"))
        self.label_2.setText(_translate("MainWindow", "No worries request for a trip that you want to go."))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.addressLabel.setText(_translate("MainWindow", "Address:"))
        self.noPersonLabel.setText(_translate("MainWindow", "No of persons:"))
        self.phoneLabel_2.setText(_translate("MainWindow", "Phone:"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm Booking"))
        self.bookingHeadingLabel.setText(_translate("MainWindow", "Just one more step!"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


def run(client:socket.socket):
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(client)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

