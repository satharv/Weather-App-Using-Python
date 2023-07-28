from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox
from tkinter import PhotoImage
import difflib


INDIAN_CITIES = ['Ahmedabad','Bengaluru','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Amritsar','Bhopal','Chandigarh','Coimbatore','Cuttack','Dehradun','Indore','Jalandhar','Jammu','Kanpur','Kochi','Kozhikode','Lucknow','Ludhiana','Madurai','Meerut','Mysore','Nagpur','Nashik','Patna','Raipur','Rajkot','Ranchi','Shimla','Srinagar','Surat','Thiruvananthapuram','Udaipur','Varanasi','Vijayawada','Visakhapatnam']

def data_get():
    city = city_name.get()
    try:
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a2d98052c87079aa6f0fad62bb8e72e7").json()
        
        # Get icon code
        icon_code = data['weather'][0]['icon']  

        # Create and display icon 
        icon_img = get_weather_icon(icon_code) # Call function to get PhotoImage
        if icon_img is not None:
            weather_icon_label = Label(image=icon_img)
            weather_icon_label.image = icon_img
            weather_icon_label.place(x=220, y=220)

        w_label0_0.config(text=data['weather'][0]["main"])
        w_label1_1.config(text=data["weather"][0]["description"])
        w_label2_2.config(text=str(int(data["main"]["temp"]-273.15)))
        w_label3_3.config(text=data["main"]["pressure"])
    except Exception as e :
        messagebox.showerror("Error", "Could not get weather data. Please check city name and internet connection.")

def get_weather_icon(code):
  if code == "01d":
    return PhotoImage(file="images/sunny.png")
  elif code == "02d": 
     return PhotoImage(file="images/partly_cloudy.png")
  elif code == "03d": 
     return PhotoImage(file="images/scattered_clouds.png")
  elif code == "04d": 
     return PhotoImage(file="images/broken_clouds.png")
  elif code == "09d": 
     return PhotoImage(file="images/shower_rain.png")
  elif code == "10d": 
     return PhotoImage(file="images/rain.png")
  elif code == "11d": 
     return PhotoImage(file="images/thunderstorm.png")
  elif code == "13d": 
     return PhotoImage(file="images/snow.png")
  elif code == "50d": 
     return PhotoImage(file="images/mist.png")
  elif code == "01n": 
     return PhotoImage(file="images/clear_night.png")
  elif code == "02n": 
     return PhotoImage(file="images/partly_cloudy_night.png")
  else:
     return None

win = Tk()
win.title("Weather App")
win.config(bg = "white")
win.geometry("500x600")


# heading label
name_label = Label(win, text="Weather App Using Python", font=("Times New Roman", 27, "bold"),bg="white")
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


# combo box
com = ttk.Combobox(win, text="Weather App using Pytho", values=list_name, font=("Times New Roman", 13),textvariable=city_name)
com.place(x=75, y=130, height=30, width=350 )


# weather climate label
w_label0 = Label(win, text="Weather Climate: ", font=("Times New Roman", 17), bg="white")
w_label0.place(x=33, y=270, height=40, width=230)
# get data
w_label0_0 = Label(win, text="", font=("Times New Roman", 17), bg="white", anchor="w", justify="left")
w_label0_0.place(x=230, y=270, height=40, width=100)


# weather description label
w_label1 = Label(win, text="Weather Description: ", font=("Times New Roman", 17), bg="white", anchor="w", justify="left")
w_label1.place(x=60, y=300, height=40, width=210)
# get data
w_label1_1 = Label(win, text="", font=("Times New Roman", 17), bg="white", anchor="w", justify="left")
w_label1_1.place(x=260, y=300, height=45, width=200)


# temperature label
w_label2 = Label(win, text="Temperature: ", font=("Times New Roman", 17), bg="white")
w_label2.place(x=25, y=330, height=40, width=210)
# get data
w_label2_2 = Label(win, text="", font=("Times New Roman", 17), bg="white", anchor="w", justify="left")
w_label2_2.place(x=193, y=330, height=40, width=100)


# pressure label
w_label3 = Label(win, text="Pressure: ", font=("Times New Roman", 17), bg="white")
w_label3.place(x=5, y=360, height=40, width=210)
# get data 
w_label3_3 = Label(win, text="", font=("Times New Roman", 17), bg="white", anchor="w", justify="left")
w_label3_3.place(x=150, y=360, height=40, width=100)


# submit button
done_button = Button(win, text = "Get Info", font=("Times New Roman", 15, "bold"),command=data_get)
done_button.place(y=180, height=30, width=100, x=200)


win.mainloop()
