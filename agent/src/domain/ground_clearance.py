from dataclasses import dataclass

from domain.gps import Gps
@dataclass
class GroundClearance:
    length: int
    gps: Gps