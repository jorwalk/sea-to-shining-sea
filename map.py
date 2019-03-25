from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('flight-animation.html')

@app.route('/flight-data')
def send():
    return send_from_directory('static', 'flights.json')

app.run(debug=True)