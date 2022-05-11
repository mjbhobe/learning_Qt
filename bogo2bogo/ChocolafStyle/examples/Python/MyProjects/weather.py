# -*- coding: utf-8 -*-
"""
* weather.py - get weather information
* TKinter app converted to PyQt5
* TKinter app @https://www.askpython.com/python/examples/gui-weather-app-in-python
*
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!

"""
import sys
import os
import pathlib
import requests
import urllib
# import json
from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from chocolaf.palettes import ChocolafPalette
from chocolaf.utils.chocolafapp import ChocolafApp

APP_PATH = os.path.dirname(__file__)
Window_Title = f"PyQt {PYQT_VERSION_STR} Weather application"
HOME_DIR = str(pathlib.Path.home())

API_KEY = '609e577f6c5eeac1a9a6c42875bbc0ec'
CITY = 'Mumbai'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def getWeather(city='Mumbai'):
    request_url = WEATHER_URL.format(city, API_KEY)
    response = requests.get(request_url)
    weather_info = response.json()
    print(weather_info)
    weather_data = {}  # response dict

    if weather_info['cod'] == 200:
        kelvin = 273.0
        # @see: https://openweathermap.org/current for documentation
        weather_data['city'] = weather_info['name'] + ', ' + weather_info['sys']['country']
        weather_data['weather_main'] = weather_info['weather'][0]['main']
        weather_data['weather_icon'] = weather_info['weather'][0]['icon']
        weather_data['temp'] = int(float(weather_info['main']['temp']) - kelvin)
        weather_data['feels_like_temp'] = int(float(weather_info['main']['feels_like']) - kelvin)
        weather_data['temp_min'] = int(float(weather_info['main']['temp_min']) - kelvin)
        weather_data['temp_max'] = int(float(weather_info['main']['temp_max']) - kelvin)
        weather_data['pressure'] = weather_info['main']['pressure']
        weather_data['humidity'] = weather_info['main']['humidity']
        weather_data['visibility'] = weather_info['visibility']
        weather_data['wind_speed'] = weather_info['wind']['speed'] # * 3.6
        weather_data['wind_direction'] = weather_info['wind']['deg']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        weather_data['timezone'] = timezone
        weather_data['cloudy'] = weather_info['clouds']['all']
        weather_data['description'] = weather_info['weather'][0]['description']

        weather_info['date'] = time_format_for_location(weather_info['dt'] + timezone)
        weather_data['sunrise_time'] = time_format_for_location(sunrise + timezone)
        weather_data['sunset_time'] = time_format_for_location(sunset + timezone)
    else:
        print(f"Weather info for city {city} not found!")
    return weather_data

class WeatherWidget(QWidget):
    def __init__(self, weather_data_dict, parent:QWidget=None):
        super(WeatherWidget, self).__init__(parent)
        self.weather_data = weather_data
        self.ui = None
        self.setupUi()

    def loadPixmap(self, weather_icon):
        pixmap_url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"
        data = urllib.request.urlopen(pixmap_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap

    def setupUi(self):
        self.city = QLabel(f"<html></h3>{self.weather_data['city']}</h3></html>")
        self.ui = uic.loadUi(os.path.join(APP_PATH, 'weather.ui'), self)
        self.ui.labelCity.setText(f"<html><h2>{self.weather_data['city']}</h2></html>")
        self.ui.labelWeatherMain.setText(self.weather_data['weather_main'])
        pixmap = self.loadPixmap(self.weather_data['weather_icon'])
        self.ui.iconLabel.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # get weather location of Mumbai as dict
    weather_data = getWeather('Los Angeles')
    print(weather_data)

    widget = WeatherWidget(weather_data)
    widget.ui.show()

    sys.exit(app.exec())