import sys
from PySide6 import QtWidgets, QtCore, QtGui
import main  # Import main.py to access the lookup_article function


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.is_light_mode = False

        # Create the greeting label
        self.greeting_label = QtWidgets.QLabel("Welcome to WeatherWiki")
        self.greeting_label.setAlignment(QtCore.Qt.AlignCenter)  # Center the text
        self.greeting_label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Increase font size

        # Create the search bar (QLineEdit)
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Enter search term")
        self.search_bar.setFixedWidth(300)

        # Create the search button
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setFixedWidth(100)

        # Create a label to display the search results
        self.result_label = QtWidgets.QLabel("Your result will appear here.")
        self.result_label.setWordWrap(True)  # Allow multi-line text
        self.result_label.setStyleSheet("padding-left: 20px;")  # Add padding to shift it slightly to the right

        # Create a horizontal layout to hold the search bar and button
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        # Create a main layout (vertical) and add the greeting, search layout, and result label
        main_content_layout = QtWidgets.QVBoxLayout()
        main_content_layout.addWidget(self.greeting_label)
        main_content_layout.addLayout(search_layout)
        main_content_layout.addWidget(self.result_label)
        main_content_layout.setAlignment(QtCore.Qt.AlignCenter)  # Keep everything centered

        # Now create the lightbulb button
        self.lightbulb_button = QtWidgets.QPushButton()
        self.lightbulb_button.setIcon(QtGui.QIcon("bulb.png"))  # Set the icon to a lightbulb image
        self.lightbulb_button.setFixedSize(40, 40)
        self.lightbulb_button.clicked.connect(self.toggle_light_mode)

        # Create a top layout for the lightbulb button, aligning it to the left
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.lightbulb_button)
        top_layout.addStretch()  # Push the button to the left, leaving space for the rest

        # Create a main vertical layout that first adds the top layout, then centers the rest of the content
        final_layout = QtWidgets.QVBoxLayout(self)
        final_layout.addLayout(top_layout)
        final_layout.addLayout(main_content_layout)

        # Connect the search button to the search function
        self.search_button.clicked.connect(self.perform_search)

        # Set an initial stylesheet (regular mode)
        self.set_regular_mode()

    def perform_search(self):
        # Get the search term from the search bar
        query = self.search_bar.text()

        # Call the lookup_article function from main.py to get the result
        result = main.lookup_article(query)

        # Update the result label with the search result
        self.result_label.setText(result)

    def toggle_light_mode(self):
        if self.is_light_mode:
            self.set_regular_mode()
        else:
            self.set_light_mode()

    def set_regular_mode(self):
        self.is_light_mode = False
        # Set background and text color for regular mode
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: white;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton {
                background-color: #4C566A;
                color: white;
                border: none;
                padding: 5px;
            }
            QLineEdit {
                background-color: #4C566A;
                color: white;
                border: 1px solid #4C566A;
            }
        """)
        self.greeting_label.setText("Welcome to WeatherWiki")

    def set_light_mode(self):
        self.is_light_mode = True
        # Set background and text color for light mode
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton {
                background-color: #D8DEE9;
                color: black;
                border: none;
                padding: 5px;
            }
            QLineEdit {
                background-color: #E5E9F0;
                color: black;
                border: 1px solid #D8DEE9;
            }
        """)
        self.greeting_label.setText("Welcome to WeatherWiki")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("Weather Wiktionary v.0.9")
    widget.show()

    sys.exit(app.exec())
