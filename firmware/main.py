import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,

        KC.MACRO("https://maps.google.com"),

        KC.MACRO(
            Press(KC.LCTL),
            Tap(KC.L),
            Release(KC.LCTL),
            "https://maps.google.com",
            Tap(KC.ENTER),
        ),
    ]
]

if __name__ == "__main__":
    keyboard.go()