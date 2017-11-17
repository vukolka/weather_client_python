import yahooAPI_lib
import geocoder
import http.client
#gettin ip adress
conn = http.client.HTTPConnection("ip.42.pl")
conn.request("GET", "/raw")
respond = conn.getresponse()
data = respond.read()
conn.close()

g = geocoder.freegeoip(data.decode())
Kiev = yahooAPI_lib.weather(g.json['city'], g.json["raw"]['country_code'])
temp = Kiev.get_current_temp()
print (temp)