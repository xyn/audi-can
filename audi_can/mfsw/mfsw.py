from __future__ import annotations
import time

from audi_can.bus import CANBus
from audi_can.mfsw import constants

class MFSW:
    def __init__(self, bus: CANBus):
        self.bus = bus

        self._press_counts = {
            name: 0 for name in constants.BUTTONS
        }

        self._last_wheel_time = 0.0
        self._last_select_time = 0.0
        self._last_unknown_time: dict[str, float] = {}

    def listen_buttons(self, timeout: float = 0.25, debounce_seconds: float = 0.70, show_unknown: bool = False) -> constants.MFSWButtonEvent | str | None:
        msg = self.bus.recv(timeout=timeout)

        if msg is None:
            return None
        
        if msg.arbitration_id != constants.MFSW_CAN_ID:
            return None
        
        hex_data = bytes(msg.data).hex()
        now = time.monotonic()

        if hex_data in constants.SCROLL_WHEEL:
            event = constants.SCROLL_WHEEL[hex_data]

            if now - self._last_wheel_time >= debounce_seconds:
                self._last_wheel_time = now
                return event
            
            return None
        
        if hex_data in constants.BUTTON_PRESS:
            button_name = constants.BUTTON_PRESS[hex_data]
            self._press_counts[button_name] += 1
            return None

        if hex_data in constants.BUTTON_RELEASE:
            button_name = constants.BUTTON_RELEASE[hex_data]
            count = self._press_counts[button_name]
            self._press_counts[button_name] = 0

            if count > 0:
                button = constants.BUTTONS[button_name]
                if count > button.very_long_threshold:
                    return button.very_long_event
                if count > button.long_threshold:
                    return button.long_event

                return button.short_event

            return None
        
        if show_unknown:
            previous = self._last_unknown_time.get(hex_data, 0.0)

            if now - previous >= debounce_seconds:
                self._last_unknown_time[hex_data] = now
                return f"MFSW_UNKNOWN_{hex_data}"

        return None