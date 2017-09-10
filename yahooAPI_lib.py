import http.client
import json
from datetime import time
class weather(object):
	#please change APIkey veriable to your key. you can get it at https://openweathermap.org/api
	
	APIkey = "e8f57762a832617e695c9e11627bfd20"
	"""docstring for weather"""
	def __init__(self, cityName, stateName):
		self.cityName = cityName
		self.stateName = stateName
		self.fileName = cityName + 'json.txt'
		self.data = self.getCityData()

	#get current weather as an integer in celcius		
	def get_current_temp(self):
		ndata = json.loads(self.data)
		current_temp = ndata["query"]["results"]["channel"]["item"]["condition"]["temp"]
		return int((float(current_temp) - 32) / 1.8)

	#get actual weather data for the passed city
	def __getActualWeatherByCity(self):
		conn = http.client.HTTPConnection("query.yahooapis.com")
		city = "/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + self.cityName + "%2C%20" + self.stateName + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
		conn.request("GET", city)
		respond = conn.getresponse()
		data = respond.read()
		conn.close()
		return data.decode()

	def getCityData(self):
		data = self.__getActualWeatherByCity()
		return data

	#get weather data for the passed city if there are actual data
	#on the computer. if none, calls __getActualWeatherByCity()


			
