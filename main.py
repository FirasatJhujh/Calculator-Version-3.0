from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
import sys

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        
        # Load the Ui file
        loadUi("calc.ui", self)

        # Define our widgets and variables
        self.mode_Label = self.findChild(QLabel, "mode_Label")
        self.display = self.findChild(QLineEdit, "display_Label")
        self.result_Label = self.findChild(QLabel, "result_Label")
        self.clearmode_Button= self.findChild(QPushButton, "clearmode_Button")
        self.setmodepostive_Button = self.findChild(QPushButton, "setmodepostive_Button")
        self.setmodenegative_Button = self.findChild(QPushButton, "setmodenegative_Button")
        self.setmodetomr_Button = self.findChild(QPushButton, "setmodetomr_Button")
        self.clear_Button = self.findChild(QPushButton, "clear_Button")
        self.multiply_Button = self.findChild(QPushButton, "multiply_Button")
        self.divide_Button = self.findChild(QPushButton, "divide_Button")
        self.cancelone_Button = self.findChild(QPushButton, "cancelone_Button")
        self.seven_Button = self.findChild(QPushButton, "seven_Button")
        self.eight_Button = self.findChild(QPushButton, "eight_Button")
        self.nine_Button = self.findChild(QPushButton, "nine_Button")
        self.minus_Button = self.findChild(QPushButton, "minus_Button")
        self.four_Button = self.findChild(QPushButton, "four_Button")
        self.five_Button = self.findChild(QPushButton, "five_Button")
        self.six_Button = self.findChild(QPushButton, "six_Button")
        self.plus_Button = self.findChild(QPushButton, "plus_Button")
        self.one_Button = self.findChild(QPushButton, "one_Button")
        self.two_Button = self.findChild(QPushButton, "two_Button")
        self.three_Button = self.findChild(QPushButton, "three_Button")
        self.percent_Button = self.findChild(QPushButton, "percent_Button")
        self.zero_Button = self.findChild(QPushButton, "zero_Button")
        self.decimalpoint_Button = self.findChild(QPushButton, "decimalpoint_Button")
        self.equal_Button = self.findChild(QPushButton, "equal_Button")
        
        # Add function to all buttons
        self.clearmode_Button.clicked.connect(lambda: self.pressed(self.clearmode_Button))
        self.setmodepostive_Button.clicked.connect(lambda: self.pressed(self.setmodepostive_Button))
        self.setmodenegative_Button.clicked.connect(lambda: self.pressed(self.setmodenegative_Button))
        self.setmodetomr_Button.clicked.connect(lambda: self.pressed(self.setmodetomr_Button))
        self.clear_Button.clicked.connect(lambda: self.pressed(self.clear_Button))
        self.multiply_Button.clicked.connect(lambda: self.pressed(self.multiply_Button))
        self.divide_Button.clicked.connect(lambda: self.pressed(self.divide_Button))
        self.cancelone_Button.clicked.connect(lambda: self.pressed(self.cancelone_Button))
        self.seven_Button.clicked.connect(lambda: self.pressed(self.seven_Button))
        self.eight_Button.clicked.connect(lambda: self.pressed(self.eight_Button))
        self.nine_Button.clicked.connect(lambda: self.pressed(self.nine_Button))
        self.minus_Button.clicked.connect(lambda: self.pressed(self.minus_Button))
        self.four_Button.clicked.connect(lambda: self.pressed(self.four_Button))
        self.five_Button.clicked.connect(lambda: self.pressed(self.five_Button))
        self.six_Button.clicked.connect(lambda: self.pressed(self.six_Button))
        self.plus_Button.clicked.connect(lambda: self.pressed(self.plus_Button))
        self.one_Button.clicked.connect(lambda: self.pressed(self.one_Button))
        self.two_Button.clicked.connect(lambda: self.pressed(self.two_Button))
        self.three_Button.clicked.connect(lambda:self.pressed(self.three_Button))
        self.percent_Button.clicked.connect(lambda: self.pressed(self.percent_Button))
        self.zero_Button.clicked.connect(lambda: self.pressed(self.zero_Button))
        self.decimalpoint_Button.clicked.connect(lambda: self.pressed(self.decimalpoint_Button))
        self.equal_Button.clicked.connect(lambda: self.pressed(self.equal_Button))
        
        # Variable to keep track the new digit
        self.new_digitPermisson = True
        # Show the main window
        self.show()
    
    def pressed(self,btn):
    # Check which button is pressed

        # For Mode: (First Line) 
        if (btn.text() == "mc"):
            # if mc is pressed
            self.mode_Label.setText("")
        
        if (btn.text() == "m+"):
            # if m+ is pressed
            self.mode_Label.setText("M")
        
        if (btn.text() == "m-"):
            # if m- is pressed
            self.mode_Label.setText("M")
        
        if (btn.text() == "mr"):
            # if mr is pressed
            self.display.setText("0")

        # For:( Second Line )
        if (btn.text() == "C"):
            # Set the display's text to 0
            self.display.setText("0")
            # self.display.setText("0")
        
        if (btn.text() == "X"):
            # Replace if any operator is placed before
            self.replace_operator("x")
            # Call the operator_checked function for checking and putting X into display
            # self.operator_checked("x")
            # Remove the first 0(the initail zero)
            # self.deleteZero()
            
        
        if (btn.text() == "÷"):
            # Replace if any operator is placed before
            self.replace_operator("÷")
            # Call the operator_checked function for checking and putting ÷ into display
            # self.operator_checked("÷")
            # Remove the first 0(the initail zero)
            # self.deleteZero()

        if (btn.text() == ""):
            # Means Backspace
            
            # Grab the text from lineEdit
            text = self.display.text()
            # If there is not chracters in text
            try:
                # Remove last chraacter of it is not zero
                if not text[0] == "0":
                    self.display.setText(text[:-1])
                    # Update the value of text
                    text = self.display.text()
                    # Check that text is not ""
                    if text == "":
                        # Set the text of display to 0
                        self.display.setText("0")
            except:
                pass

        # For: ( Third Row )
        if (btn.text() == "7"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()
            
            # Put 7 in display
            self.addText("7")
        
        if (btn.text() == "8"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()

            # Put 8 in display
            self.addText("8")
        
        if (btn.text() == "9"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()
            # Put 9 in display
            self.addText("9")
        
        if (btn.text() == "-"):
            # Replace if any operator is placed before
            self.replace_operator("-")
            # # Call the operator_checked function for checking and putting - into display
            # self.operator_checked("-")
            # Remove the first 0(the initail zero)
            # self.deleteZero()

        # For: (Fourth Row)
        if (btn.text() == "4"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()
            # Put 4 in display
            self.addText("4")

        if (btn.text() == "5"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()
            # Put 5 in display
            self.addText("5")

        if (btn.text() == "6"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()

            # Put 6 in display
            self.addText("6")

        if (btn.text() == "+"):
            # Replace if any operator is placed before
            self.replace_operator("+")
            # Call the operator_checked function for checking and putting + into display
            # self.operator_checked("+")
            # # Remove the first 0(the initail zero)
            # self.deleteZero()

    
    # For: (Fifth Row)
        if (btn.text() == "1"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()

            # Put 1 in display
            self.addText("1")

        if (btn.text() == "2"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()

            # Put 2 in display
            self.addText("2")

        if (btn.text() == "3"):
            # Remove the first 0(the initail zero)
            self.deleteZero()
            # 
            self.deleteText()

            # Put 3 in display
            self.addText("3")
    
    # For: (Sixth Row)
        if (btn.text() == "%"):
            # Call the operator_checked function for checking and putting % into display
            self.replace_operator("%")

        if (btn.text() == "0"):
            # Remove the first 0(the initail zero)
            # self.deleteZero()
            
            # Put 0 in display
            self.addText("0")

        if (btn.text() == "."):
            # Put the .(period if it can be placed)
            self.decimalPiont()

        if (btn.text() == "="):

            self.top_Calculate()

    # For Presentation(Beauty)
        self.decrease_font()
        
    # For: (manual)
        if btn.text() != "=":
            self.bottom_Calculate()

    def decimalPiont(self):
        # Create a virual display and add . to diagonse error
        try:
            # Grab the text from display
            text = self.display.text()
            # Check that it is correct
            test_it = eval(text + '.')

            # Put the . in the deciamlPiont
            self.display.setText(text + ".")
        except:
            pass
    
    def bottom_Calculate(self):
        # Grab text from display
        text = self.display.text()
        
        # For: if the screen have no last digit(cover error)
        try:
            # Check the last didgit of screen is operator or not
            if not text[-1].isdigit():            
                text = text[:-1]
        except:
            pass

        # Replace the x with *
        text = text.replace("x", "*")
        # Replace the ÷ with \
        text = text.replace("÷", "/")

        # If the text is "-" than bottom calculation will be ""
        try:
            # Get the output of equation as float
            new:float = eval(text)
     
            # Check the are there more than 15 chracter on botton than convert in standard form   
            if len(str(new)) > 15:
                # Update the value of new (In standard form)
                new = self.convert_to_Standard(new)
            else:
                pass

        except:
            new = ""


        # Set the dispalys
        self.result_Label.setText(str(new))
 
    def top_Calculate(self):
        # Set the result's(bottom label) value to ""
        self.result_Label.setText("0")

        # Grab text from display
        text = self.display.text()
        
        # Remove the last chracter if operator
        if text.endswith("+") or text.endswith("-") or text.endswith("x") or text.endswith("÷"):
            text = text[:-1]
        
        # Replace the x with *
        text = text.replace("x", "*")
        # Replace the ÷ with \
        text = text.replace("÷", "/")
        
        # Round offing the expression's output by 4 digits
        new = round(eval(text),4)


        # Set the dispalys
        self.display.setText(str(new))

        # Set the result's(bottom label) value to ""
        self.result_Label.setText("0")
    
        # Change the value of Permission
        self.new_digitPermisson= False
        
    def addText(self, digit):
        # Grab the text from display.
        text = self.display.text()
        
        # If self.new_digitPermisson is True(when after topCAlculator called, if 1st key is -) than put digit 
        if self.new_digitPermisson:
            # Append text and digit to display
            self.display.setText(f"{text}{digit}")
        else:
            # OtherWise delete all text than put digit
            self.display.setText(digit)
            # Cahange the value of permission
            self.new_digitPermisson = True
            
        
    # For: (font stuff)
    def decrease_font(self):
        # Get the number of character
        t_chracter = len(self.display.text())
        #It change as time when the total chracters increase 
        font_size = 0

        if t_chracter <= 13:
            font_size = 33
        
        elif t_chracter <= 15:
            font_size = 30
             
        elif t_chracter <= 17 or t_chracter >= 17:
            font_size = 25
        
        # Choose the font
        font = QFont("Yu Gothic UI Semibold", font_size)
        # Set the font
        self.display.setFont(font)

    def deleteText(self):
        print("I am cutest!!!!")

    # For: (additionsl feature)
    def deleteZero(self):
        # Grab the text from the dispplay
        text = self.display.text() # * it value is 0

        # For list out of range error
        if len(text) > 1:
            # Check the first chracter of display
            li = ["-"]
            if text[0] == "0" and text[1] not in li and text[1] != ".":
            # Remmove the 0(first)
                self.display.setText(text[1:-1])
        else:
            # Check the first chracter of display
            if text[0] == "0":
            # Remmove the 0(first)
                self.display.setText(text[1:-1])

    def replace_operator(self, operator):
        # Change the value of permisson
        self.new_digitPermisson = True

        # Grab the text from from display
        text = self.display.text()
        # List of operators
        list_operator = ["+","-","÷","x"]
        print(text)
        if text == '0':
            if operator == "-":
                self.display.setText(f"{text[1:]}-")
        elif text[-1] in list_operator:
            # Check the the minus is first digit
            if text[0] != "-":
                self.display.setText(f"{text[:-1]}{operator}")
        else:
            # Simply add operator
            self.display.setText(f"{text}{operator}")
                  
    def convert_to_Standard(self, number):

        # Convert to standard form using scientific notation
        standard_form = "{:.5e}".format(number)

        # Replace small e(mean 10) with capital
        standard_form = standard_form.replace("e","E")
        
        # Returning the standard form
        return standard_form

if __name__ == "__main__":
    # Create the Application
    app = QApplication(sys.argv)
    # Create the UI
    ui = Ui_MainWindow()
    # Execute the application
    app.exec_()