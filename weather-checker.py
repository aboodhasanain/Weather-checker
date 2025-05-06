import tkinter as tk
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define the function to fetch weather data
def get_weather_data(city):
    api_key = "6c034accdf55dec2d31221ef5610f5d4"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6c034accdf55dec2d31221ef5610f5d4&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]
        wind_data = data['wind']

        # Extracting relevant data
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_description = weather_data['description']
        wind_speed = wind_data['speed']

        return temperature, humidity, weather_description, wind_speed
    else:
        return None


# Define function to display weather info and graph
def display_weather():
    city = city_entry.get()
    weather = get_weather_data(city)

    if weather:
        temperature, humidity, weather_description, wind_speed = weather
        weather_info.set(
            f"Weather in {city}:\nTemp: {temperature}°C\nHumidity: {humidity}%\nCondition: {weather_description.capitalize()}\nWind Speed: {wind_speed} m/s")

        # Plot the weather conditions graph
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.barh(['Temperature', 'Humidity', 'Wind Speed'], [temperature, humidity, wind_speed], color='skyblue')
        ax.set_title(f"Weather in {city}")
        ax.set_xlabel("Values")
        ax.set_ylabel("Weather Conditions")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)
        canvas.draw()
    else:
        weather_info.set("City not found. Please try again.")


# Create the main window
window = tk.Tk()
window.title("Interactive Weather App")
window.geometry("400x400")

# Create and place the widgets
city_label = tk.Label(window, text="Enter City Name:")
city_label.grid(row=0, column=0)

city_entry = tk.Entry(window)
city_entry.grid(row=0, column=1)

search_button = tk.Button(window, text="Get Weather", command=display_weather)
search_button.grid(row=1, column=0, columnspan=2)

weather_info = tk.StringVar()
weather_label = tk.Label(window, textvariable=weather_info, font=("Arial", 12))
weather_label.grid(row=2, column=0, columnspan=2)

# Start the application
window.mainloop()
