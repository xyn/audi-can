from enum import Enum

from audi_can.constants import ButtonDefinition

MFSW_CAN_ID = 0x5C3

class MFSWButtonEvent(Enum):
    WHEEL_LEFT_UP = 'wheel_left_up'
    WHEEL_LEFT_DOWN = 'wheel_left_down'
    WHEEL_LEFT_CLICK = 'wheel_left_click'
    WHEEL_LEFT_CLICK_LONG = 'wheel_left_click_long'
    WHEEL_LEFT_CLICK_VERY_LONG = 'wheel_left_click_very_long'

SCROLL_WHEEL: dict[str, MFSWButtonEvent] = {
    "3a03": MFSWButtonEvent.WHEEL_LEFT_UP,
    "3a02": MFSWButtonEvent.WHEEL_LEFT_DOWN,
}

BUTTONS: dict[str, ButtonDefinition] = {
    "left_wheel_click": ButtonDefinition(
        name="left_wheel_click",
        press_frame="3a1a",
        release_frame="3a00",
        short_event=MFSWButtonEvent.WHEEL_LEFT_CLICK,
        long_event=MFSWButtonEvent.WHEEL_LEFT_CLICK_LONG,
        very_long_event=MFSWButtonEvent.WHEEL_LEFT_CLICK_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
}

BUTTON_PRESS: dict[str, str] = {
    button.press_frame: name
    for name, button in BUTTONS.items()
}

BUTTON_RELEASE: dict[str, str] = {
    button.release_frame: name
    for name, button in BUTTONS.items()
    if button.release_frame is not None
}