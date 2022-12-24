
import requests
from datetime import datetime as dt

apikey = "---your api goes heere---"
baseurl = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city: ")

url = f"{baseurl}?appid={apikey}&q={city}"
#print("URL= {}".format(url))  #To print the URL

response = requests.get(url)  
if response.status_code!=200:         #if reponse status is not 200 it exits the program
    print("\033[1;31;40mERROR {}{}".format(response.status_code,"\033[0;37;0m "))
    exit()

data = response.json()  #storing the data in json format
# print(data)

current_time = data["dt"]
current_time = dt.fromtimestamp(current_time).time()
print("\n{}--------------{}-{}----{}-------------{}".format("\033[1;32;40m ",city.upper(),data["sys"]["country"],current_time,"\033[0;37;0m "))

#----------------------------------DATA RETRIVING----------------------------------#
weather = data["weather"][0]["description"]             #extracting the weather data
temperature = round(data["main"]["temp"] - 273.15, 2)   #extracting the temperature data

sunrise = data["sys"]["sunrise"]                        #IST based timezone are returned in the api call
sunrise = dt.fromtimestamp(sunrise).time()              #extracting the time from the timestamp

sunset = data["sys"]["sunset"]
sunset = dt.fromtimestamp(sunset).time()  

lat_lon=data["coord"]["lat"],data["coord"]["lon"]       #extracting the longitude and latitude data


#----------------------------------PRINTNG DATA----------------------------------#
print("LATITUDE: {}  \tLONGITUDE: {}".format(float(lat_lon[0]),float(lat_lon[1])))
print("TEMPERATURE: {}°C\tWEATHER: {}".format(temperature,weather))
print("SUNRISE: {}\tSUNSET: {}".format(sunrise,sunset))

#-----------------------------------MISC. DATA-----------------------------------#
try:
    rain= data["rain"]["1h"]                            #extracting the rain data
    print("RAIN: ",rain)
except KeyError:
    print("NO RAIN TODAY")
