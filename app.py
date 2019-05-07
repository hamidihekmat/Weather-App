from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

@app.route('/')
def weather_app():

    return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
