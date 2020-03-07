from math import floor


def getHour(minutes):
    return floor(minutes / 60) % 24


def getMinutes(minutes):
    return minutes % 60


class Clock(object):
    def __init__(self, hour, minute):
        self._total_minutes = hour*60 + minute


    def __repr__(self):
        return f"{getHour(self._total_minutes):02}:{getMinutes(self._total_minutes):02}"


    def __eq__(self, other):
        return getHour(self._total_minutes) == getHour(other._total_minutes) and getMinutes(self._total_minutes) == getMinutes(other._total_minutes)

    def __add__(self, minutes):
        total_minutes = self._total_minutes + minutes
        return Clock(getHour(total_minutes), getMinutes(total_minutes))

    def __sub__(self, minutes):
        total_minutes = self._total_minutes - minutes
        return Clock(getHour(total_minutes), getMinutes(total_minutes))
