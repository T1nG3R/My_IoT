from dataclasses import dataclass
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.ground_clearance import GroundClearance


@dataclass
class AggregatedData:
    accelerometer: Accelerometer
    gps: Gps
    ground_clearance: GroundClearance
    timestamp: datetime