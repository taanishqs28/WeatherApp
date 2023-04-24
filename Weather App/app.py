import tkinter as tk
from tkinter import messagebox
import requests
import urllib.parse

def get_weather(city):
    """enter api key in quotes"""
    #api_key = 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": urllib.parse.quote(city),
        "appid": api_key,
        "units": "metric",
        "exclude": "minutely",  # Exclude minutely weather data
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def show_weather():
    city = city_entry.get()  # Get city name from input field
    weather_data = get_weather(city)  # Get weather data from API

    if "cod" in weather_data and weather_data["cod"] == "404":
        # Display error message if city not found
        messagebox.showerror("Error", "City not found. Please try again.")
    else:
        # Extract weather information
        temperature = weather_data.get("main", {}).get("temp", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        pressure = weather_data.get("main", {}).get("pressure", "N/A")
        lightning = weather_data.get("lightning", "N/A")
        rain = weather_data.get("rain", {}).get("1h", "N/A")
        wind_speed = weather_data.get("wind", {}).get("speed", "N/A")
        snow = weather_data.get("snow", {}).get("1h", "N/A")
        air_quality = weather_data.get("aqi", {}).get("value", "N/A")

        # Update labels with weather information
        temperature_label.config(text=f"Temperature: {temperature} °C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        lightning_label.config(text=f"Lightning: {lightning}")
        rain_label.config(text=f"Rain (1h): {rain} mm")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        snow_label.config(text=f"Snow (1h): {snow} mm")
        air_quality_label.config(text=f"Air Quality Index: {air_quality}")

# Create GUI window
root = tk.Tk()
root.title("Weather App")

# Create labels and entry field for city input
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=10)

# Create button to get weather information
get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

# Create labels to display weather information
temperature_label = tk.Label(root, text="")
temperature_label.pack()
humidity_label = tk.Label(root, text="")
humidity_label.pack()
pressure_label = tk.Label(root, text="")
pressure_label.pack()
lightning_label = tk.Label(root, text="")
lightning_label.pack()
rain_label = tk.Label(root, text="")
rain_label.pack()
wind_speed_label = tk.Label(root, text="")
wind_speed_label.pack()
snow_label = tk.Label(root, text="")
snow_label.pack()
air_quality_label = tk.Label(root, text="")
air_quality_label.pack()

def update_weather_labels(temperature, humidity, pressure, lightning, rain, wind_speed, snow, air_quality):
    temperature_label.config(text=f"Temperature: {temperature} °C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    lightning_label.config(text=f"Lightning: {lightning}")
    rain_label.config(text=f"Rain (1h): {rain} mm")
    wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
    snow_label.config(text=f"Snow (1h): {snow} mm")
    air_quality_label.config(text=f"Air Quality Index: {air_quality}")

# Run the GUI loop
root.mainloop()
