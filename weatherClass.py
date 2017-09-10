import http.client
import json
from datetime import time
class weather(object):
	#please change APIkey veriable to your key. you can get it at https://openweathermap.org/api
	
	APIkey = "e8f57762a832617e695c9e11627bfd20"
	"""docstring for weather"""
	def __init__(self, cityName):
		self.cityName = cityName
		self.fileName = cityName + 'json.txt'
		self.data = self.getCityData()

	#get current weather as an integer in celcius		
	def get_current_temp(self):
		current_temp = int(float(self.data['main']['temp']) - 273.15)
		return current_temp

	#get actual weather data for the passed city
	def __getActualWeatherByCity(self):
		conn = http.client.HTTPConnection("api.openweathermap.org")
		city = "/data/2.5/weather?id=524901&APPID=&q=" + self.APIkey + self.cityName
		conn.request("GET", city)
		respond = conn.getresponse()
		data = respond.read()
		conn.close()
		return data.decode()

	def getCityData(self):
		try:
			fo = open(self.fileName, "r+")
			data = json.load(fo)
			fo.close()
		except FileNotFoundError:
			data = self.__getActualWeatherByCity()
			fo = open(self.fileName, "w+")
			fo.write(json.loads(data))
			fo.close()
		return data

	#get weather data for the passed city if there are actual data
	#on the computer. if none, calls __getActualWeatherByCity()


			
