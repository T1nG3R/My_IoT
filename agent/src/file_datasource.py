from csv import reader
from datetime import datetime

from domain.ground_clearance import GroundClearance
from domain.aggregated_data import AggregatedData
from domain.accelerometer import Accelerometer
from domain.gps import Gps

class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str, ground_clearance_filename: str) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.ground_clearance_filename = ground_clearance_filename
        self.cache_data = {}

    def read(self) -> AggregatedData:
        try:
            accelerometer_data = next(reader(self.cache_data["accelerometer"]))
            gps_data = next(reader(self.cache_data["gps"]))
            ground_clearance = next(reader(self.cache_data["ground_clearance"]))

            x, y, z = map(int, accelerometer_data)
            longitude, latitude = map(float, gps_data)
            length = int(ground_clearance[0])
            return AggregatedData(accelerometer=Accelerometer(x=x, y=y, z=z),
                                  gps=Gps(longitude=longitude, latitude=latitude),
                                  ground_clearance=GroundClearance(length, Gps(longitude=longitude, latitude=latitude)),
                                  timestamp=datetime.now())
        except StopIteration:
            self.stopReading()
            StopIteration("No data")
        except ValueError as error:
            ValueError(error)

    def startReading(self, *args, **kwargs):
        self.cache_data["accelerometer"] = open(self.accelerometer_filename, 'r')
        self.cache_data["gps"] = open(self.gps_filename, 'r')
        self.cache_data["ground_clearance"] = open(self.ground_clearance_filename, 'r')

    def stopReading(self, *args, **kwargs):
        self.cache_data["accelerometer"].close()
        self.cache_data["gps"].close()
        self.cache_data["ground_clearance"].close()