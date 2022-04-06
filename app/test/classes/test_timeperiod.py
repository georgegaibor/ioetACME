from app.classes import TimePeriod
from datetime import datetime


def test_create():
    format = "%H:%M"
    start = datetime.strptime("20:00", format)
    end = datetime.strptime("21:00", format)
    test_period = TimePeriod(start, end)
    assert start == test_period.start
    assert end == test_period.end


def test_overlaps():
    format = "%H:%M"
    startA = datetime.strptime("20:00", format)
    endA = datetime.strptime("21:00", format)
    test_periodA = TimePeriod(startA, endA)
    startB = datetime.strptime("20:30", format)
    endB = datetime.strptime("22:00", format)
    test_periodB = TimePeriod(startB, endB)
    assert test_periodA.overlaps(test_periodB)
