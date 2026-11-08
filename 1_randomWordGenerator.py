# Import all Modules
from PyQt5.QtCore import Qt # type: ignore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout # type: ignore

from random import choice



# Main App Objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random words Maker")
main_window.setFixedSize(400, 200) # sets the size of the window to 400x200 pixels

# Create all Objects/widgets here
title = QLabel("Random Keywords")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")
button = QPushButton("Tester")

my_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# All Designs here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)
row3.addWidget(button)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout) #sets the layout of the main window to the master layout

#Create all Functions here
def random_word1():

    word = choice(my_words)
    text1.setText(word)
def random_word2():

    word = choice(my_words)
    text2.setText(word)
def random_word3():
    word = choice(my_words)
    text3.setText(word)
    

#Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)
button.clicked.connect(lambda: print("Tester Button Clicked!")) # Example of a lambda function to print a message when the button is clicked

# Show/Run the App 
main_window.show()
app.exec_()





#QtCore -tools for aligning widgets
# #QtWidgets - tools for creating GUI elements


#PyQt Methods
#addWidget() - adds a widget to the layout
#setText() - sets the text of a widget
#addLayout() - adds a layout to a widget
#setLayout() - sets the layout of a widget
#show() - displays the widget on the screen


