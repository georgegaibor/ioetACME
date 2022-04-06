from app.classes import Employee, TimePeriod
from app.common.util import days_dictionary


def test_create():
    test_dict = days_dictionary("FR20:00-23:00")
    test_emp = Employee("April", test_dict)
    assert test_emp == Employee("April", {"FR": [TimePeriod("20:00", "23:00")]})
