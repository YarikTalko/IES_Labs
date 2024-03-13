from csv import reader
from datetime import datetime

from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking
from domain.aggregated_data import AggregatedData


class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str, parking_filename: str) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename
        self.data = {}

    def read(self) -> AggregatedData:
        try:
            accelerometer_data = next(reader(self.data["accelerometer_data"]))
            gps_data = next(reader(self.data["gps_data"]))
            parking_data = next(reader(self.data["parking_data"]))
            x = int(accelerometer_data[0])
            y = int(accelerometer_data[1])
            z = int(accelerometer_data[2])
            longitude = float(gps_data[0])
            latitude = float(gps_data[1])
            empty_count = int(parking_data[0])
            return AggregatedData(accelerometer=Accelerometer(x=x, y=y, z=z),
                                  gps=Gps(longitude=longitude, latitude=latitude),
                                  parking=Parking(empty_count, Gps(longitude=longitude, latitude=latitude)),
                                  time=datetime.now())

        except StopIteration:
            self.stopReading()

    def startReading(self, *args, **kwargs):
        self.data["accelerometer_data"] = open(self.accelerometer_filename, "r")
        self.data["gps_data"] = open(self.gps_filename, "r")
        self.data["parking_data"] = open(self.parking_filename, "r")

    def stopReading(self, *args, **kwargs):
        self.data["accelerometer_data"].close()
        self.data["gps_data"].close()
        self.data["parking_data"].close()
