from bluetooth_api import *

for i in range(10, 100):
    detection = Detection('{0}:{0}:{0}:{0}:{0}:{0}'.format(i))
    db.session.add(detection)

db.session.commit()