from pyA20.gpio import gpio
from pyA20.gpio import port

import dht22
import time
import datetime

gpio.init()

instance = dht22.DHT22(pin=port.PA6)

result = instance.read()
if result.is_valid():
    print('{0:0.1f} | {1:0.1f}'.format(result.temperature, result.humidity))
else:
    print('-1 | -1')