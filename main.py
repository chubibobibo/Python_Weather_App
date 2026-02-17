import sys
import requests
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import( QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QVBoxLayout)  

# Subclass QWidget to customize your application's main window
# When you subclass a Qt class you must always call the superclass __init__ function to allow Qt to set up the object.
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__() # access parent(QMainWindow) attributes
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
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
                font-family: calibri;
            }

            QLabel#city_label {
                font-size: 50px;
                font-style: italic;
            }

            QLineEdit#city_input {
                font-size: 40px;
            }

            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold
            }

            QLabel#temperature_label {
                font-size: 75px;
            }

            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }

            QLabel#description_label {
                font-size: 50px
            }

        """)
        
        # signal listener
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self, get_weather_icon):
        print('Getting weather from api...')
        api_key = "661f40b7510beeb48bf0c439faf87066"
        city = self.city_input.text() # obtains text in the text field
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status() # manually type this because try catch block does not normally catch http errors
            data = response.json()
            # print(data['weather'][0]['description'])
            if data['cod'] == 200: 
                self.get_weather_icon(data)
                self.display_weather(data, city)
        # Exception raised by the request module
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error('Bad Request:\nCheck your input')
                case 401:
                    self.display_error('Unauthorized')
                case 403:
                    self.display_error('Forbidden')
                case 404:
                    self.display_error('City Not Found')
                case _: #no cases match
                    self.display_error('HTTP error occurred')
        except requests.exceptions.ConnectionError:
            # print('Connection Error:\nCheck your internet connection')
            self.display_error('Connection Error:\nCheck your internet connection')
            
        except requests.exceptions.Timeout:
            # print('Time Out error:\nThe request timed out')
            self.display_error('Time Out error:\nThe request timed out')
            
            
        except requests.exceptions.TooManyRedirects:
            # print('Too many redirects:\nCheck url')
             self.display_error('Too many redirects:\nCheck url')
            

        except requests.RequestException as req_err:
            print(f'Request Error {req_err}')

        except Exception: # catch other exceptions
            # print('Something went  wrong')
            self.display_error('Something went  wrong')

      

    def display_error(self, err_message):
        self.temperature_label.setStyleSheet('font-size: 30px')# styling the error appearing in the temperature label
        self.temperature_label.setText(f'An exception occurred: \n{err_message}')
        self.emoji_label.clear()
        self.description_label.clear()

    #if no errors are returned
    def display_weather(self, data, city_data):
        print(f'Here are the results: {data['weather']}')
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        print(f'Here is the temperature in celsius: {temperature_c:.0f}C')
        
        # displaying result
        # Temperature
        self.temperature_label.setStyleSheet('font-size: 50px')
        self.temperature_label.setText(f'Here is the temperature for {city_data.capitalize()}:\n{temperature_c:.0f}C')
        # Weather description
        self.description_label.setStyleSheet('font-size: 40px')
        self.description_label.setText(data['weather'][0]['description'])
       
        # Weather icon
        #icon = data['weather'][0]['icon']
        # Obtain icons based on weather
        #icon_url = f'https://openweathermap.org/payload/api/media/file/{icon}.png'
        #icon_response = requests.get(icon_url)
        # print(icon_response.content)
        #pixmap = QPixmap() # display images
        #pixmap.loadFromData(icon_response.content) # convert binary data from icon_response to image data that QT can use
        #self.emoji_label.setPixmap(pixmap) # set the pixmap from converted image raw data
        #self.emoji_label.show()

    # @staticmethod #belongs to a class but does not require instance specific data
    def get_weather_icon(self, data):
        icon = data['weather'][0]['icon']
        icon_url =  f'https://openweathermap.org/payload/api/media/file/{icon}.png'
        icon_response = requests.get(icon_url)
        pixmap = QPixmap()
        pixmap.loadFromData(icon_response.content)
        self.emoji_label.setPixmap(pixmap)
        self.emoji_label.show()
        self.emoji_label.setStyleSheet('background-color: lightgray; border-radius: 25px')





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