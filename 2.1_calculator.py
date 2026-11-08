# Import all Modules
import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QVBoxLayout, QHBoxLayout , QGridLayout , QLineEdit 



class CalcApp(QWidget):

        def __init__(self):

            super().__init__()

            # Main App Objects and settings

            self.setWindowTitle("Calculator")
            self.setFixedSize(250, 300) # sets the size of the window to 400x200 pixels

            # Create all Objects/widgets here
            self.text_box = QLineEdit() # creates a text box for user input
            self.grid = QGridLayout() # creates a grid layout for the buttons
            self.buttons = ["7", "8", "9", "/", 
                    "4", "5", "6", "*", 
                    "1", "2", "3", "-", 
                    "0", ".", "=", "+"]
            row = 0
            col = 0
            for text in self.buttons:
                button = QPushButton(text)
                button.clicked.connect(self.button_clicked)
                self.grid.addWidget(button, row, col)
                col += 1
                if col > 3:
                        col = 0
                        row += 1
                
            self.clear = QPushButton("C") # creates a button for clearing the text box
            self.delete = QPushButton("Del") # creates a button for deleting the last character in the text box
                        # Design you Layout, add your widgets to the screen
            button_row = QHBoxLayout()
            button_row.addWidget(self.clear)
            button_row.addWidget(self.delete)

            master_layout = QVBoxLayout()
            master_layout.addWidget(self.text_box)
            master_layout.addLayout(self.grid)
            master_layout.addLayout(button_row)

            # Set the final Layout to the Main window
            self.setLayout(master_layout) #sets the layout of the main window to the master layout
            self.clear.clicked.connect(self.button_clicked)
            self.delete.clicked.connect(self.button_clicked)


        def button_clicked(self):

                button = app.sender()
                text = button.text()
                if text == "=":
                        symbol = self.text_box.text()
                        try:
                                result = eval(symbol)
                                self.text_box.setText(str(result))
                        except Exception as e:
                                print("Error:", e)
                                self.text_box.setText("Error")

                elif text == "C":
                        self.text_box.clear()

                elif text == "Del":
                        current_value = self.text_box.text()
                        self.text_box.setText(current_value[:-1])
                        
                else:
                        current_value = self.text_box.text()
                        self.text_box.setText(current_value + text)
                        


        


            # Function



            # Events






# Show and execute the app

if __name__ == "__main__":
        app = QApplication([]) # initializes the application
        main_window = CalcApp() # initializes the main window
        main_window.show()
        app.exec_()







