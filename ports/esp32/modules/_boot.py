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

import boot

if button.value():
    print('button press detected, skipping main.py')
elif test_path('main.py'):
    import main