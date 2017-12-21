from flask import jsonify
import bluetooth, requests, json

URL = 'http://127.0.0.1:5000/'

def get_all_devices():
    devices = bluetooth.discover_devices()
    return json.dumps({'devices' : devices})

def send_all_devices():
    request_content = get_all_devices()
    requests.post(URL + 'visite', request_content)

if __name__ == '__main__':
    send_all_devices()
