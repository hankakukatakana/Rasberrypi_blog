import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

message = "Hello"
while True:
    layout.write(message)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

    time.sleep(1000)