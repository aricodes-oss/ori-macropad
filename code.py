import usb_hid

from adafruit_hid.keyboard import Keyboard
from mappings import PINS, KEYCODES

kbd = Keyboard(usb_hid.devices)
kbd.release_all()


while True:
    # See mappings file for why this isn't a dictionary
    for idx, pin in enumerate(PINS):
        code = KEYCODES[idx]

        # Needed for debouncer to update the state
        pin.update()

        if pin.fell:
            kbd.press(code)

        if pin.rose:
            kbd.release(code)
