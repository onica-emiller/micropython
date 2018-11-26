import gc
import uos
from flashbdev import bdev
from machine import Pin
import os
import iotanium

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
    print('button press detected. skipping boot.py and main.py')
    import webrepl
    iotanium.setup() #running setup with button pressed will enable AP
    webrepl.start()
else:
    import boot
    if test_path('main.py'):
        import main