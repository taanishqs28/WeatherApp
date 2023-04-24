import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "2a2f3f5f7828274647633dc6d6b77617"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def show_weather():
    city = entry.get()
    if city:
        try:
            data = get_weather(city)
            if data["cod"] == 200:
                weather = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                messagebox.showinfo("Weather Information", f"City: {city}\nWeather: {weather}\nTemperature: {temperature}°C")
            else:
                messagebox.showerror("Error", f"Unable to fetch weather information for {city}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", "Please enter a city name")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  

label = tk.Label(root, text="Enter City:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)
button = tk.Button(root, text="Search", command=show_weather)
button.pack()

root.mainloop()
