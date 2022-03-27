import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from rgbkeypad import RGBKeypad

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
plum = (221,160,221)
yellow = (255,255,0)
cyan = (0,255,255)
orange = (255,128,0)
white = (255,255,255)
black = (0,0,0)
indigo = (75,0,130)
teal = (65,159,191)
turq = (0,255,190)

KEYBOARD_MAP = {
    (0,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.V,),      # Start/Stop Video
    (1,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.Z,),      # Mute/Unmute Self
    (2,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.N,),      # Switch Camera
    (3,0): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.L,),      # Mute/Unmute All
    (0,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.Q,),      # Start/Stop Screenshare
    (1,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.P,),      # Show/Hide Floating Controls
    (2,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.C,),      # Chat Panel
    (3,1): (Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.B,),      # Participant Panel
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
keypad[1,0].color = blue
keypad[2,0].color = green
keypad[3,0].color = purple
keypad[0,1].color = cyan
keypad[1,1].color = yellow
keypad[2,1].color = turq
keypad[3,1].color = orange
keypad[0,2].color = black
keypad[1,2].color = black
keypad[2,2].color = black
keypad[3,2].color = black
keypad[0,3].color = black
keypad[1,3].color = black
keypad[2,3].color = black
keypad[3,3].color = white
keypad.brightness = 0.3

while True:
    for key in keypad.keys:
        if key.is_pressed():
            if (key.x, key.y) in KEYBOARD_MAP.keys():
                kbd.send(*KEYBOARD_MAP[(key.x, key.y)]) 
            while key.is_pressed():
                pass