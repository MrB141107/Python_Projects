import tkinter as tk
import requests

# Function to fetch weather data from the OpenWeatherMap API
def get_weather():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_label.config(text=f"Weather: {weather_info}")
        temp_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        result_label.config(text="")
    else:
        weather_label.config(text="")
        temp_label.config(text="")
        humidity_label.config(text="")
        result_label.config(text="City not found!")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create labels, entry, and button widgets
city_label = tk.Label(window, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(window)
city_entry.pack()
search_button = tk.Button(window, text="Search", command=get_weather)
search_button.pack()
weather_label = tk.Label(window, text="", font=("Helvetica", 16))
weather_label.pack(pady=10)
temp_label = tk.Label(window, text="")
temp_label.pack()
humidity_label = tk.Label(window, text="")
humidity_label.pack()
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

window.mainloop()
