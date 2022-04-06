import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from rgbkeypad import RGBKeypad

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)

KEYBOARD_MAP = {
    (0,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.1,),      # Start/Stop Video
    (1,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.2,),      # Switch Camera
    (2,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.3,),      # Mute/Unmute Self
    (3,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.4,),      # Mute/Unmute All
    (0,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.5,),      # Start/Stop Screenshare
    (1,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.6,),      # Show/Hide Floating Controls
    (2,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.7,),      # Chat Panel
    (3,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.8,),      # Participant Panel
    #(0,2): (Keycode.SHIFT, Keycode.E,),
    #(1,2): (Keycode.R,),
    #(2,2): (Keycode.E,),
    #(3,2): (Keycode.SHIFT, Keycode.ONE,),
    #(0,3): (Keycode.CONTROL,),
    #(1,3): (Keycode.ENTER,),
    #(2,3): (Keycode.ENTER,),
    (3,3): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.ESCAPE,) # Task Manager
}

keypad = RGBKeypad()
kbd = Keyboard(usb_hid.devices)
keypad[0,0].color = red
keypad[1,0].color = red
keypad[2,0].color = red
keypad[3,0].color = red
keypad[0,1].color = blue
keypad[1,1].color = blue
keypad[2,1].color = blue
keypad[3,1].color = blue
keypad[0,2].color = green
keypad[1,2].color = green
keypad[2,2].color = green
keypad[3,2].color = green
keypad[0,3].color = yellow
keypad[1,3].color = yellow
keypad[2,3].color = yellow
keypad[3,3].color = yellow
keypad.brightness = 0.2

while True:
    for key in keypad.keys:
        if key.is_pressed():
            if (key.x, key.y) in KEYBOARD_MAP.keys():
                kbd.send(*KEYBOARD_MAP[(key.x, key.y)]) 
            while key.is_pressed():
                pass
