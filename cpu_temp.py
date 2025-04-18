#!/usr/bin/env python3

from flask import Flask, jsonify
import time

app = Flask(__name__)

def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = float(f.read().strip()) / 1000.0
            return temp
    except Exception as e:
        print(f"Error reading CPU temperature: {e}")
        return None

@app.route('/temperature', methods=['GET'])
def temperature():
    temp = get_cpu_temperature()
    if temp is not None:
        return jsonify({
            'temperature': temp,
            'unit': 'celsius',
            'timestamp': time.time()
        })
    else:
        return jsonify({
            'error': 'Could not read CPU temperature'
        }), 500

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'CPU Temperature API',
        'endpoints': {
            '/temperature': 'Get current CPU temperature'
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 