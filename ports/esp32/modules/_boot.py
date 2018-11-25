import gc
import uos
from flashbdev import bdev
from machine import Pin
import os

button = Pin(2, Pin.IN)

def test_path(fname):
    try:
        os.stat(fname)
        return True
    except OSError:
        return False

try:
    if bdev:
        uos.mount(bdev, '/')
except OSError:
    import inisetup
    vfs = inisetup.setup()

gc.collect()


if button.value():
    print('button press detected. skipping boot.py, main.py and enabling AP')
    import iotanium
    iotanium.setup() #running setup with button pressed will enable AP
else:
    import boot
    
if test_path('main.py'):
    import main