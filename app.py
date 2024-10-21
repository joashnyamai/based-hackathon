# app.py (Flask backend)
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for passenger dashboard data
@app.route('/passenger-data')
def passenger_data():
    routes = [
        {"id": 1, "route": "Route 101", "fare": "0.01 ETH"},
        {"id": 2, "route": "Route 202", "fare": "0.02 ETH"},
    ]
    return jsonify(routes)

# Route for driver dashboard data
@app.route('/driver-data')
def driver_data():
    routes = [
        {"id": 1, "route": "Route 101", "earnings": "0.10 ETH"},
        {"id": 2, "route": "Route 202", "earnings": "0.15 ETH"},
    ]
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True)
