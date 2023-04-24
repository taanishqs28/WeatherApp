import tkinter as tk
import requests

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x400")

# Create labels and entry for city input
city_label = tk.Label(root, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

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

# Function to update weather information labels
def update_weather_labels(temperature, humidity, pressure, lightning, rain, wind_speed, snow, air_quality):
    temperature_fahrenheit= round((temperature * 9/5) + 32, 2) 
    temperature_label.config(text=f"Temperature: {temperature_fahrenheit} °F")  

    humidity_label.config(text=f"Humidity: {humidity}%")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    lightning_label.config(text=f"Lightning: {lightning}")
    rain_label.config(text=f"Rain (1h): {rain} mm")
    wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
    snow_label.config(text=f"Snow (1h): {snow} mm")
    air_quality_label.config(text=f"Air Quality Index: {air_quality}")


# Function to get weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()
    city = city.replace(" ", "%20")  # Replace spaces with '%20'
    api_key = "2a2f3f5f7828274647633dc6d6b77617"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        if 'lightning' in data['weather'][0]['description'].lower():
            lightning = 'Yes'
        else:
            lightning = 'No'
        if 'rain' in data.keys():
            rain = data['rain']['1h']
        else:
            rain = 0
        if 'wind' in data.keys():
            wind_speed = data['wind']['speed']
        else:
            wind_speed = 0
        if 'snow' in data.keys():
            snow = data['snow']['1h']
        else:
            snow = 0
        if 'aqi' in data.keys() and 'us-epa' in data['aqi'].keys():
            air_quality = data['aqi']['us-epa']['aqi']
        else:
            air_quality = 'N/A'
        update_weather_labels(temperature, humidity, pressure, lightning, rain, wind_speed, snow, air_quality)
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        temperature_label.config(text="Error: Failed to fetch weather data")
        humidity_label.config(text="")
        pressure_label.config(text="")
        lightning_label.config(text="")
        rain_label.config(text="")
        wind_speed_label.config(text="")
        snow_label.config(text="")
        air_quality_label.config(text="")
    except Exception as e:
        # Handle other exceptions
        temperature_label.config(text="Error: An unexpected error occurred")
        humidity_label.config(text="")
        pressure_label.config(text="")
        lightning_label.config(text="")
        rain_label.config(text="")
        wind_speed_label.config(text="")
        snow_label.config(text="")
        air_quality_label.config(text="")

# Create button to get weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Run tkinter event loop
root.mainloop()
