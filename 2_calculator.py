# Import all Modules
import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QVBoxLayout, QHBoxLayout , QGridLayout , QLineEdit 




 
# Main App Objects and settings
app = QApplication(sys.argv) # initializes the application
app.setStyleSheet("""
    QPushButton {
        background-color: #4169E1;
        border-radius: 5px;
        padding: 6px;
    }
""")

main_window = QWidget() # initializes the main window
main_window.setWindowTitle("Calculator")
main_window.setFixedSize(250, 300) # sets the size of the window to 400x200 pixels

# Create all Objects/widgets here
text_box = QLineEdit() # creates a text box for user input
grid = QGridLayout() # creates a grid layout for the buttons
buttons = ["7", "8", "9", "/", 
        "4", "5", "6", "*", 
        "1", "2", "3", "-", 
        "0", ".", "=", "+"]

clear = QPushButton("C") # creates a button for clearing the text box
delete = QPushButton("Del") # creates a button for deleting the last character in the text box

def button_clicked():

        button = app.sender()
        text = button.text()
        if text == "=":
                symbol = text_box.text()
                try:
                        result = eval(symbol)
                        text_box.setText(str(result))
                except Exception as e:
                        print("Error:", e)
                        text_box.setText("Error")

        elif text == "C":
                text_box.clear()

        elif text == "Del":
                current_value = text_box.text()
                text_box.setText(current_value[:-1])
                
        else:
                current_value = text_box.text()
                text_box.setText(current_value + text)
                


row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_clicked)
    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Design you Layout, add your widgets to the screen
button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)
master_layout.addLayout(button_row)


# Function



# Set the final Layout to the Main window
main_window.setLayout(master_layout) #sets the layout of the main window to the master layout

# Events
clear.clicked.connect(button_clicked)
delete.clicked.connect(button_clicked)

# Show and execute the app
main_window.show()
app.exec_()







