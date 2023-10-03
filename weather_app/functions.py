import requests
from credentials import *
from datetime import datetime

def getWeather(cityName):
        
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + cityName
    response = requests.get(complete_url)
    x = response.json()
    
    if x["cod"] != "404":
        weather = x["weather"]
        main = x["main"]
        wind = x["wind"]
        sun = x["sys"]

        weather_final = weather[0]["main"]
        
        main_final = {}
        main_final["Temprature"] = kelvinToCelcius(main["temp"])
        main_final["Feels Like"] = kelvinToCelcius(main["feels_like"])
        main_final["Minimum Temprature"] = kelvinToCelcius(main["temp_min"])
        main_final["Maximum Temprature"] = kelvinToCelcius(main["temp_max"])
        main_final["Pressure"] = main["pressure"]
        main_final["Humidity"] = main["humidity"]

        wind_final = {}
        wind_final["Speed"] = wind["speed"]
        wind_final["Degree"] = wind["deg"]

        sunrise = sun["sunrise"]
        sunset = sun["sunset"]
        sun_final = getSunriseSunset(sunrise, sunset)

        z = {"Weather": weather_final, "main": main_final, "wind": wind_final, "sun": sun_final}

        return z
    
    else:
        return(" City Not Found ")




def getSunriseSunset(sunrise, sunset):
    sunrise = datetime.fromtimestamp(sunrise)
    sunset = datetime.fromtimestamp(sunset)
    return {"Sunrise": sunrise.strftime("%d-%m-%Y %H:%M:%S %p"), "Sunset": sunset.strftime("%d-%m-%Y %H:%M:%S %p")}


def kelvinToCelcius(kelvin):
    return int(kelvin - 273.15)



