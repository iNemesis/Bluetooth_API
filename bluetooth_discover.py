from flask import jsonify
import bluetooth, requests

URL = 'http://...'

def get_all_devices():
    devices = bluetooth.discover_devices()
    return jsonify({'devices' : devices})

def send_all_devices():
    request_content = get_all_devices()
    requests.post(URL, request_content)






