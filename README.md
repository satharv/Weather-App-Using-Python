# Weather-App-Using-Python
This is a simple weather app built with Python and Tkinter that allows you to view the current weather conditions for a city.

## Features

- Enter a city name and get real-time weather data
- Displays weather metrics like temperature, weather condition, pressure etc
- Appropriate weather icon displayed based on conditions
- Dropdown to select from list of Indian cities
- Input validation with suggestions for invalid city name
- Error handling for network requests and invalid data

## Modules Used

- ``` Tkinter ``` : For building the GUI
- ``` Requests ``` : To fetch weather data from OpenWeatherMap API
- ``` JSON ``` : To parse API response
- ``` PIL ``` : To load weather icons

## Future Improvements
Some ways the app can be improved further:

- Allow searching for cities globally
- Add graphs and visualizations for weather metrics
- Enable configuration of temperature units
- Use asynchronous calls to improve performance
- Improve UI/UX for better user experience

## Installation
- First clone the repository:
  ```
  git clone https://github.com/username/weather-app.git
  ```
- Install the dependencies using pip:
  ```
  pip install -r requirements.txt
  ```
- Now the application can be executed using:
  ```
  python weather_app.py
  ```

## Requirements
The app requires the following packages:

- ``` tkinter ```
- ``` requests ```
- ``` Pillow ```
- ``` json ```
- ``` difflib ```
  
Overall, this project demonstrates how Python and its libraries can be used to build a simple yet useful weather application with a GUI.
