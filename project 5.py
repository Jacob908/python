import imp
from turtle import down
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

#Main class
class Window(QMainWindow):
    # Constructor method
    def __init__(self):
        # inheriting methods and properties from superclass QMainWindow
        super().__init__()
        # Setting the title
        self.setWindowTitle("Mortgage Payment Calculator")
        self.width = 700
        self.height = 900
        self.setGeometry(100, 100, self.width, self.height)
        self.UiComponents()
        self.show()
    # Function to add widgets
    def UiComponents(self):
        head = QLabel("Morgage Payment Calculator", self)
        head.setGeometry(0,10,400,60)
        font = QFont('Times', 15)
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkBlue)
        head.setGraphicsEffect(color)
    #-------------- Interest label---------------
        i_label = QLabel("Annual Interest", self)
        #properties
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20,100,170,40)
        i_label.setStyleSheet("QLabel" " {"
                                               "border : 2px solid black;"
                                               "background: rgba(70,70,70,35);"
                                               "}")
        i_label.setFont(QFont('Times', 9))
        #input field for interest rate
        self.rate = QLineEdit(self)
        # setting properties
        self.rate.setGeometry(200,100,180,40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont('Times', 9))

    #------------Price of the house-------------
        p_label = QLabel("Price of House", self)
        #properties
        p_label.setAlignment(Qt.AlignCenter)
        p_label.setGeometry(20,150,170,40)
        p_label.setStyleSheet("QLabel" " {"
                                               "border : 2px solid black;"
                                               "background: rgba(70,70,70,35);"
                                               "}")
        p_label.setFont(QFont('Times', 9))
        #input field for price of the house 
        self.price = QLineEdit(self)
        #Only integers validation
        onlyInt = QIntValidator()
        self.price.setValidator(onlyInt)
        # setting properties
        self.price.setGeometry(200,150,180,40)
        self.price.setAlignment(Qt.AlignCenter)
        self.price.setFont(QFont('Times', 9))
     #------------Downpayment of the house-------------
        d_label = QLabel("Downpayment", self)
        #properties
        d_label.setAlignment(Qt.AlignCenter)
        d_label.setGeometry(20,200,170,40)
        d_label.setStyleSheet("QLabel" " {"
                                               "border : 2px solid black;"
                                               "background: rgba(70,70,70,35);"
                                               "}")
        d_label.setFont(QFont('Times', 9))
        #input field for price of the house 
        self.down = QLineEdit(self)
        #Only integers validation
        onlyInt = QIntValidator()
        self.down.setValidator(onlyInt)
        # setting properties
        self.down.setGeometry(200,200,180,40)
        self.down.setAlignment(Qt.AlignCenter)
        self.down.setFont(QFont('Times', 9))

        
    #----------number of years------------
        n_label = QLabel("Years", self)
        #properties
        n_label.setAlignment(Qt.AlignCenter)
        n_label.setGeometry(20,250,170,40)
        n_label.setStyleSheet("QLabel" " {"
                                               "border : 2px solid black;"
                                               "background: rgba(70,70,70,35);"
                                               "}")
        n_label.setFont(QFont('Times', 9))
        #input field for years 
        self.years = QLineEdit(self)
        #Only integers validation
        onlyInt = QIntValidator()
        self.years.setValidator(onlyInt)
        # setting properties
        self.years.setGeometry(200,250,180,40)
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFont(QFont('Times', 9))


        # ///////////Compute payment
        #Creating the compute button
        calculate = QPushButton("Calculate", self)
        #Set geometry
        calculate.setGeometry(140,340,150,40)
        # Add action the calculate button
        calculate.clicked.connect(self.calculate_action)

        #output Widgets
    # ----------Loan Amount --------------
        self.amount = QLabel(self)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setGeometry(50,410,300,60)
        self.amount.setStyleSheet("QLabel" " {"
                                               "border : 3px solid black;"
                                               "background: white"
                                               "}")
        self.amount.setFont(QFont('Times', 11))


    # --------- MOntlhy payment --------
        self.m_payment = QLabel(self)
        #properties monthly payment
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setGeometry(50,480,300,60)
        self.m_payment.setStyleSheet("QLabel" " {"
                                               "border : 3px solid black;"
                                               "background: white"
                                               "}")
        self.m_payment.setFont(QFont('Times', 11))
        
        self.t_payment = QLabel(self)
        #properties total payment
        self.t_payment.setAlignment(Qt.AlignCenter)
        self.t_payment.setGeometry(50,550,300,60)
        self.t_payment.setStyleSheet("QLabel" " {"
                                               "border : 3px solid black;"
                                               "background: white"
                                               "}")
        self.t_payment.setFont(QFont('Times', 11))

    def calculate_action(self):
        # Getting annual interest rate
        annualInterestRate = self.rate.text()
        # To check if fields are empty
        if len(annualInterestRate) == 0 or annualInterestRate == '0':
            QMessageBox.critical(self, "Alert!", "Fill the blanks!")
        # Getting number of years
        numberOfYears = self.years.text()
        # To check if fields are empty
        if len(numberOfYears) == 0 or numberOfYears == '0':
            QMessageBox.critical(self, "Alert!", "Fill the blanks!")
        # Getting the loan amount
        downPayment = self.down.text()
        # To check if fields are empty
        if len(downPayment) == 0 or downPayment == '0':
            QMessageBox.critical(self, "Alert!", "Fill the blanks!")
        housePrice = self.price.text()
        # To check if fields are empty
        if len(housePrice) == 0 or housePrice == '0':
            QMessageBox.critical(self, "Alert!", "Fill the blanks!")
        
        
        #Get calculations
        #Convert text into integer
        annualInterestRate = float(annualInterestRate)
        numberOfYears = int(numberOfYears)
        downPayment = int(downPayment)
        housePrice = int(housePrice)
        
        #Monthly interest rate calculation [12x100%]
        monthlyInterestRate = annualInterestRate / 1200
        #Calculate loan amount
        loanAmount = housePrice - downPayment
        #Calculate monthly payments
        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1+monthlyInterestRate) ** (numberOfYears*12))

        
        #Outputting loan amount
        loanAmount = "{:.2f}".format(loanAmount)
        self.amount.setText("Loan Amount: " + str(loanAmount))
        #Set the format for monthly payment for 2 decimal points float
        monthlyPayment = "{:.2f}".format(monthlyPayment)
        # Add text to monthly payment calculation
        self.m_payment.setText("Monthly Payment: " + str(monthlyPayment))
        #Getting total payment
        totalPayment = float(monthlyPayment) * 12 * numberOfYears
        totalPayment = "{:.2f}".format(totalPayment)
        # Add text to total payment calculation
        self.t_payment.setText("Total Payment: " + str(totalPayment))


# Create app object
App = QApplication(sys.argv)

# Instantiate Window Class
window = Window()

#Start the application
sys.exit(App.exec())