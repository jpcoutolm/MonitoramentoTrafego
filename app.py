from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = 'database/devices.db'

def connect_db():
    conn = sqlite3.connect(DB)
    return conn

@app.route('/devices', methods=['GET'])
def get_devices():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices")
    rows = cursor.fetchall()
    conn.close()
    devices = [{"id": r[0], "ip": r[1], "name": r[2], "traffic": r[3]} for r in rows]
    return jsonify(devices)

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO devices (ip, name, traffic) VALUES (?, ?, ?)", 
                   (data['ip'], data['name'], data['traffic']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Device added"}), 201

@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM devices WHERE id = ?", (device_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Device deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
