from app.classes import Employee
from app.common.util import employee_list, days_dictionary, match_visits


def test_emp_list():
    assert isinstance(employee_list("schedules.txt"), list)


def test_days_dict():
    assert isinstance(days_dictionary("FR20:00-23:00,SU06:00-07:00"), dict)


def test_match_visits():
    may = Employee("May", days_dictionary("FR20:00-23:00,SU06:00-07:00"))
    peter = Employee("Peter", days_dictionary("FR20:00-23:00,SA06:00-07:00"))
    assert match_visits(may, peter) == 1
