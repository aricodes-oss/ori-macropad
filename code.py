import usb_hid

from adafruit_hid.keyboard import Keyboard
from mappings import PINS, KEYCODES

kbd = Keyboard(usb_hid.devices)
kbd.release_all()


while True:
    to_press = []
    to_release = []

    # See mappings file for why this isn't a dictionary
    for idx, pin in enumerate(PINS):
        code = KEYCODES[idx]

        # Needed for debouncer to update the state
        pin.update()

        if pin.fell:
            to_press.append(code)

        if pin.rose:
            to_release.append(code)

    kbd.release(*to_release)
    kbd.press(*to_press)
