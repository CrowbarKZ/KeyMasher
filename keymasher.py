from time import sleep
from random import randint

import uinput


device = uinput.Device([
    uinput.KEY_LEFTALT,
    uinput.KEY_LEFTCTRL,
    uinput.KEY_1,
    uinput.KEY_2,
    uinput.KEY_3,
    uinput.KEY_4,
    uinput.KEY_UP,
    uinput.KEY_DOWN,
    uinput.KEY_PAGEUP,
    uinput.KEY_PAGEDOWN,
])

DESKTOP_CHANGE_COMBOS = (
    [uinput.KEY_LEFTALT, uinput.KEY_LEFTCTRL, uinput.KEY_1],
    [uinput.KEY_LEFTALT, uinput.KEY_LEFTCTRL, uinput.KEY_2],
    [uinput.KEY_LEFTALT, uinput.KEY_LEFTCTRL, uinput.KEY_3],
)

i = 0
while True:
    # change desktop
    sleep(30)
    device.emit_combo(DESKTOP_CHANGE_COMBOS[i])
    i = (i + 1) % 3

    # scroll stuff
    for j in range(randint(1, 3)):
        device.emit_click(uinput.KEY_PAGEUP)
        sleep(2)

    for j in range(randint(1, 3)):
        device.emit_click(uinput.KEY_PAGEDOWN)
        sleep(2)

    for j in range(randint(1, 9)):
        device.emit_click(uinput.KEY_UP)
        sleep(1)

    for j in range(randint(1, 9)):
        device.emit_click(uinput.KEY_DOWN)
        sleep(1)


