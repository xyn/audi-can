from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class ButtonDefinition:
    name: str
    press_frame: str
    release_frame: str
    short_event: Enum
    long_threshold: int
    very_long_threshold: int
    long_event: Enum | None = None
    very_long_event: Enum | None = None