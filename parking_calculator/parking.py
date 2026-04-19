from datetime import datetime
from math import ceil


class Parking:
    def __init__(self, line):
        parts = line.split("\t\t")
        self.registration_number = parts[0]
        self.start: datetime = datetime.strptime(parts[1], '%Y-%m-%d %H:%M:%S')
        self.end: datetime = datetime.strptime(parts[2], '%Y-%m-%d %H:%M:%S')

        if self.start > self.end:
            raise Exception("Exit time cannot be earlier than entry time!")

    def get_duration(self):
        return ceil((self.end - self.start).total_seconds() / 60)
