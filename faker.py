from bluetooth_api import *

for detection in Detection.query.all():
    print(detection)