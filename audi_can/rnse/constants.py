from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


TV_CAN_ID = 0x602
BUTTON_CAN_ID = 0x461

PAL_TV_PAYLOAD = bytes.fromhex("81123141562031")
NTSC_TV_PAYLOAD = bytes.fromhex("89123141562031")


class RNSEButtonEvent(Enum):
    SCROLL_LEFT = "scroll_left"
    SCROLL_RIGHT = "scroll_right"

    UP_SHORT = "up_short"
    UP_LONG = "up_long"
    UP_VERY_LONG = "up_very_long"

    DOWN_SHORT = "down_short"
    DOWN_LONG = "down_long"
    DOWN_VERY_LONG = "down_very_long"

    SELECT_SHORT = "select_short"
    SELECT_LONG = "select_long"
    SELECT_VERY_LONG = "select_very_long"

    RETURN_SHORT = "return_short"
    RETURN_LONG = "return_long"
    RETURN_VERY_LONG = "return_very_long"

    NEXT_SHORT = "next_short"
    NEXT_LONG = "next_long"
    NEXT_VERY_LONG = "next_very_long"

    PREVIOUS_SHORT = "previous_short"
    PREVIOUS_LONG = "previous_long"
    PREVIOUS_VERY_LONG = "previous_very_long"

    SETUP_SHORT = "setup_short"
    SETUP_LONG = "setup_long"
    SETUP_VERY_LONG = "setup_very_long"

@dataclass(frozen=True)
class ButtonDefinition:
    name: str
    press_frame: str
    release_frame: str
    short_event: RNSEButtonEvent
    long_event: RNSEButtonEvent
    very_long_event: RNSEButtonEvent
    long_threshold: int
    very_long_threshold: int


ROTARY_ENCODER: dict[str, RNSEButtonEvent] = {
    "373001004001": RNSEButtonEvent.SCROLL_LEFT,
    "373004004000": RNSEButtonEvent.SCROLL_LEFT,
    "377004004000": RNSEButtonEvent.SCROLL_LEFT,

    "373001002001": RNSEButtonEvent.SCROLL_RIGHT,
    "373004002000": RNSEButtonEvent.SCROLL_RIGHT,
    "377004002000": RNSEButtonEvent.SCROLL_RIGHT,
}


BUTTONS: dict[str, ButtonDefinition] = {
    "up": ButtonDefinition(
        name="up",
        press_frame="373001400000",
        release_frame="373004400000",
        short_event=RNSEButtonEvent.UP_SHORT,
        long_event=RNSEButtonEvent.UP_LONG,
        very_long_event=RNSEButtonEvent.UP_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "down": ButtonDefinition(
        name="down",
        press_frame="373001800000",
        release_frame="373004800000",
        short_event=RNSEButtonEvent.DOWN_SHORT,
        long_event=RNSEButtonEvent.DOWN_LONG,
        very_long_event=RNSEButtonEvent.DOWN_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "select": ButtonDefinition(
        name="select",
        press_frame="373001001000",
        release_frame="373004001000",
        short_event=RNSEButtonEvent.SELECT_SHORT,
        long_event=RNSEButtonEvent.SELECT_LONG,
        very_long_event=RNSEButtonEvent.SELECT_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "return": ButtonDefinition(
        name="return",
        press_frame="373001000200",
        release_frame="373004000200",
        short_event=RNSEButtonEvent.RETURN_SHORT,
        long_event=RNSEButtonEvent.RETURN_LONG,
        very_long_event=RNSEButtonEvent.RETURN_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "next": ButtonDefinition(
        name="next",
        press_frame="373001020000",
        release_frame="373004020000",
        short_event=RNSEButtonEvent.NEXT_SHORT,
        long_event=RNSEButtonEvent.NEXT_LONG,
        very_long_event=RNSEButtonEvent.NEXT_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "previous": ButtonDefinition(
        name="previous",
        press_frame="373001010000",
        release_frame="373004010000",
        short_event=RNSEButtonEvent.PREVIOUS_SHORT,
        long_event=RNSEButtonEvent.PREVIOUS_LONG,
        very_long_event=RNSEButtonEvent.PREVIOUS_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    ),
    "setup": ButtonDefinition(
        name="setup",
        press_frame="373001000100",
        release_frame="373004000100",
        short_event=RNSEButtonEvent.SETUP_SHORT,
        long_event=RNSEButtonEvent.SETUP_LONG,
        very_long_event=RNSEButtonEvent.SETUP_VERY_LONG,
        long_threshold=4,
        very_long_threshold=16,
    )
}

BUTTON_PRESS: dict[str, str] = {
    button.press_frame: name
    for name, button in BUTTONS.items()
}

BUTTON_RELEASE: dict[str, str] = {
    button.release_frame: name
    for name, button in BUTTONS.items()
}