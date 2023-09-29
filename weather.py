import tkinter as tk
import requests
import time

# install the libraries
# pip install requests
# pip install tkinter

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=79ff6654118cd4a24c275fb6b03503cf"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp  = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
  # rain = json_data['rain']['1h']
    clouds = json_data['clouds']['all']

    final_info = condition + "\n" + str(temp) + "℃"
    final_data = "\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp:" + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) +"Wind Speed: " + str(wind)
  # final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
    
 

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg='black')

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t, fg='orange')
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

# label1 = tk.Label(canvas, font=t)
# label1.pack()
# label2 = tk.Label(canvas, font=f)
# label2.pack()

label1 = tk.Label(canvas, font=t, fg='orange', bd=5, relief='ridge')  # Set text color to blue and add border
label1.pack(pady=10)

label2 = tk.Label(canvas, font=f, fg='orange', bd=5, relief='ridge')  # Set text color to blue and add border
label2.pack(pady=10)

canvas.mainloop()