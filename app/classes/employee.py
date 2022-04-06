class Employee:
    def __init__(self, name: str, visits: dict):
        """
        Class used to represent an employee

        Attributes
        ----------
        :param name: str
            The name of the employee

        :param visits:
            Dictionary of the visits the employee has made to the office.
                Keys: Day of visit.
                Values: List with TimePeriods of all the visits in a given day.
        """
        self.name = name
        self.visits = visits

    def __eq__(self, other: "Employee") -> bool:
        return (self.name == other.name) and (self.visits == other.visits)

    def __lt__(self, other):
        return self.name < other.name
