from __future__ import annotations
from typing import Iterable, Optional

import can

class CANBus:
    def __init__(self, channel: str = "can0", interface: str = "socketcan"):
        self.channel = channel
        self.interface = interface
        self.bus = can.interface.Bus(channel=channel, interface=interface)
    
    def send(self, can_id: int, data: bytes | bytearray | list[int]) -> None:
        msg = can.Message(arbitration_id=can_id, data=bytearray(data), is_extended_id=False)
        self.bus.send(msg)

    def send_periodic(self, can_id: int, data: bytes | bytearray | list[int], period: float) -> None:
        msg = can.Message(arbitration_id=can_id, data=bytearray(data), is_extended_id=False)
        return self.bus.send_periodic(msg, period)
    
    def recv(self, timeout: Optional[float] = None):
        return self.bus.recv(timeout)
    
    def set_filters(self, can_ids: Iterable[int]) -> None:
        self.bus.set_filters([
            {"can_id": can_id, "can_mask": 0x7FF, "extended": False}
            for can_id in can_ids
        ])
    
    def shutdown(self) -> None:
        self.bus.shutdown()

    def __enter__(self) -> "CANBus":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.shutdown()  