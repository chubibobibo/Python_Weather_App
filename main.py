import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow  

# Subclass QMainWindow to customize your application's main window
# When you subclass a Qt class you must always call the superclass __init__ function to allow Qt to set up the object.
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # access parent(QMainWindow) attributes
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)

        # self.setWindowTitle('My APP') # refers to the instance of MainWindow class
        # button = QPushButton('Push me') # creates a button
        # # Set the central widget of the Window.
        # self.setCentralWidget(button)


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