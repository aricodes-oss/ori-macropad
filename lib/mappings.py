import json

import board
import digitalio
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer


def _init_pin(gp):
    pin = digitalio.DigitalInOut(getattr(board, gp))
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

    return Debouncer(pin)


with open("mappings.json") as f:
    config_data = list(json.load(f).items())

# CircuitPython doesn't allow us to use complex objects as dictionary keys
# so we're going with a series of lists here. dict.keys() and dict.values()
# do not guarantee a consistent return order so we use dict.items() once
# and base everything off of that ordering
PINS = [_init_pin(gp) for gp, _ in config_data]
KEYCODES = [getattr(Keycode, kc) for _, kc in config_data]
