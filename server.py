import random
import  datetime
from flask import Flask, jsonify

app = Flask(__name__)
NUM = 20

@app.route('/price')
def prices():
    return jsonify({f"product_{i}": random.uniform(1.0,10.0)  for i in range(NUM) })

@app.route('/sales')
def sales():
    return jsonify({f"product_{i}": random.randint(0,10) for i in range(NUM) })

@app.route('/daily/<date>')
def daily(date):
    try:
        dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        return f"{date} is not a valid date", 500
    epoch = datetime.datetime.utcfromtimestamp(0)
    result = {
        "year": dt.year,
        "day": dt.day,
        "month": dt.month,
        "seconds": (dt-epoch).total_seconds()
    }
    return jsonify(result)

