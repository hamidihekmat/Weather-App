#!/usr/local/bin/python3
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def format_response(city):
    weather_key = "15f1a9a8bfb41be537161d4d95453d68"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = "City: %s \nCondition: %s \nTemperature (C): %s" % (
            name, desc, temp)
    except:
        final_str = "There was a problem"
    return final_str


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        city = request.form['city']
        weather_data = format_response(city)
        return render_template('home.html', data=weather_data)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
