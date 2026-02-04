import sys
import requests
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import( QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QVBoxLayout)  

# Subclass QWidget to customize your application's main window
# When you subclass a Qt class you must always call the superclass __init__ function to allow Qt to set up the object.
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # access parent(QMainWindow) attributes
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel('35C', self)
        self.emoji_label = QLabel('☀️', self)
        self.description_label = QLabel('Sunny', self)
        self.initUI()

    # method to initialize the interface
    def initUI(self):
        self.setWindowTitle('Weather App')
        #layout manager 
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        # set the layout passing the vertical layout manager that we defined
        self.setLayout(vbox)

        # align elements center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # applying styles based on objects name
        # set object name for every element we have
        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        # applying style sheets
        # NOTE: QLabel#city_label  selects QLabel that has a  "city_label" object name
        self.setStyleSheet("""
            QLabel, QPushButton {
            font-family: calibri
            }
            QLabel#city_label {
            
            }
        """)







if __name__ == "__main__":
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    weather_app = WeatherApp()
    weather_app.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()