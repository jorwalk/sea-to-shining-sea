import json
from flask import Flask
from flask import render_template
from flask import request

from src.constraint_solver import main
from src.data import Data

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def root():

    depot = 33

    cities, route = main(depot)

    if request.method == 'POST':
        data = Data()
        flight = {"flights": data.flight_path(route)}
        return json.dumps(flight)

    if request.method == 'GET':
        cap = {'capitals': cities}
        return render_template('home.html', data=cap)



app.run(debug=True)
