from itertools import product, combinations
from datetime import datetime

from ..classes.employee import Employee
from ..classes.timeperiod import TimePeriod
import app.config as config


def employee_list(directory: str) -> list:
    """
    Returns a list of objects of the Employee class from the lines of
    the specified file
    :param directory: str path to the file with employee data
    """
    employees = []
    with open(directory, "r") as file:
        for line in file:
            name, days = line.strip().split("=")
            employees.append(Employee(name, days_dictionary(days)))
    return employees


def days_dictionary(days: str) -> dict:
    """
    Transforms a string with day and time data into a dictionary
    :param days: string containing the day and time period during which
    a visit took place
    :returns: Dictionary of the visits made to the office.
    """
    format = "%H:%M"
    days_dict = {}
    for day in days.split(","):

        hours = day[2:].split("-")
        start = datetime.strptime(hours[0], format)
        end = datetime.strptime(hours[1], format)

        if day[:2] in days_dict:
            days_dict[day[:2]].append(TimePeriod(start, end))
            days_dict[day[:2]] = sorted(days_dict[day[:2]])
        else:
            days_dict[day[:2]] = [TimePeriod(start, end)]

    return days_dict


def match_and_format(employee_list: list):
    """
    Finds and prints the amount of times a group of employees have visited
    the office at the same time
    :param employee_list: list of employees
    """
    print(f"{config.titl_a:<14}{config.titl_b:<14}{config.match:<14}")

    for employee_a, employee_b in combinations(sorted(employee_list), 2):
        matches = match_visits(employee_a, employee_b)
        if matches > 0:
            print(f"{employee_a.name:<14}{employee_b.name:<14}{matches:<14}")


def match_visits(employee_a: "Employee", employee_b: "Employee") -> int:
    """
    Returns the number of matches found after comparing the schedule of
    two employees
    :param self: First employee to compare
    :param other: Second employee to compare
    :returns: number of matches found for the input pair
    """
    matches = 0
    for day in employee_a.visits:
        try:
            matchlist = [
                period_a.overlaps(period_b)
                for (period_a, period_b) in product(
                    employee_a.visits[day], employee_b.visits[day]
                )
            ]
            matches += len([value for value in matchlist if value is True])
        except KeyError:
            pass
    return matches
