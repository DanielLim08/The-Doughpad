# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys




# This is the main instance of your keyboard
keyboard = KMKKeyboard()
Encoder_handler = EncoderHandler()
# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(Encoder_handler)
keyboard.modules.append(MediaKeys)
keyboard.modules.append(MouseKeys)



# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6,
        board.D7, board.D8, board.D9, board.D10, board.D11]
Encoder_handler.pins = ((board.D6, board.D7, board.D8,None),)  # Encoder pins
# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.ESC, KC.LTCL(KC.C) KC.LTCL(KC.V),]
]
Encoder_handler.map = [
    (KC.VOLUME_DOWN, KC.VOLUME_UP),  # Encoder rotation
    (KC.MUTE, KC.PLAY_PAUSE),  # Encoder push
]
# Start kmk!
if __name__ == '__main__':
    keyboard.go()