import yahooAPI_lib
import sys
city = sys.argv[1]
state = sys.argv[2]
print (city)
print (state)
Kiev = yahooAPI_lib.weather(city, state)
temp = Kiev.get_current_temp()
print (temp)
