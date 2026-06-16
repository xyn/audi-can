from __future__ import annotations

import time

from audi_can.bus import CANBus
from audi_can.rnse import constants


class RNSE:
    def __init__(self, bus: CANBus):
        self.bus = bus
        self._tv_task = None
        self._press_counts = {
            name: 0 for name in constants.BUTTONS
        }
        self._last_scroll_time = 0.0
        self._last_unknown_time: dict[str, float] = {}

    def enable_tv_mode(self, video_format: str = "PAL", period: float = 0.50):
        if video_format.upper() == "NTSC":
            payload = constants.NTSC_TV_PAYLOAD
        else:
            payload = constants.PAL_TV_PAYLOAD

        self._tv_task = self.bus.send_periodic(can_id=constants.TV_CAN_ID, data=payload, period=period)
        return self._tv_task

    def disable_tv_mode(self) -> None:
        if self._tv_task is not None:
            self._tv_task.stop()
            self._tv_task = None

    def listen_buttons(self, timeout: float = 0.25, debounce_seconds: float = 0.70, show_unknown: bool = False) -> constants.RNSEButtonEvent | str | None:
        msg = self.bus.recv(timeout=timeout)

        if msg is None:
            return None

        if msg.arbitration_id != constants.BUTTON_CAN_ID:
            return None

        hex_data = bytes(msg.data).hex()
        now = time.monotonic()

        if hex_data in constants.ROTARY_ENCODER:
            event = constants.ROTARY_ENCODER[hex_data]

            if now - self._last_scroll_time >= debounce_seconds:
                self._last_scroll_time = now
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
                return f"RNSE_UNKNOWN_{hex_data}"

        return None