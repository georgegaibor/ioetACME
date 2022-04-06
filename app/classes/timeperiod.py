from dataclasses import dataclass
from datetime import datetime


@dataclass(order=True)
class TimePeriod:
    def __init__(self, start: datetime, end: datetime):
        """
        Class used to represent a period of time

        Attributes
        ----------
        :param start: datetime
            beginning of the period of time in HH:MM
        :param end: datetime
            end of the period of time in HH:MM
        """
        self.start = start
        self.end = end

    def overlaps(self, other: "TimePeriod") -> bool:
        """
        Returns whether or not two time periods overlap with each other

        :param self: First time period to compare
        :param other: Second time period to compare
        :returns: true or false
        """
        return (self.start <= other.start <= self.end) or (
            other.start <= self.start <= other.end
        )
