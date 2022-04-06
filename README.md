<h1 align="center"> ACME Excercise Solution </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is a potential solution for the ACME coding exercise that is part of __ioet, Inc.'s__ recruitment process

## Overview
The company ACME needs to know what employees have been at the office within the same time frame.
The goal of this exercise is to output a table containing pairs of employees and how often they have 
coincided in the office. 

REQUIREMENTS:
* Can not use any external library to solve the exercise
* Input: the name of an employee and the schedule they worked, indicating the time and hours. 
This should be a .txt file with at least five sets of data.
* Output: a table containing pairs of employees and how often they have coincided in the office.


__EXAMPLE__

INPUT:

RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

RENE-ASTRID: 3


## Approach
From the sample input and output provided three main values can be identified:
* Name: the name of an employee
* Day: the day the employee visited the office
* Hours: the range of time the employee was at the office

To reach a solution the following issues needed to be addressed:
1. Extract the data from the input file and separate it into the identified values
2. Transform the values corresponding to the hours into an easily comparable data type to find if a visit took place during
the same time frame
3. Associate employees with their visits 


Considering the format of the example input provided, the first step of the process was completed by using built-in string
methods to separate each line of the .txt file into an employee's name and a string of the visits they had made, this was encapsulated
in the __employee_list()__ function. Inside this function the string of visits is processed using the __days_dictionary()__ function to transform it 
into a dictionary with days as keys and a list of objects of the __TimePeriod__ class as values to account for the possibility of multiple visits in a single day. 


The __TimePeriod__ class consists of a start and end attribute, both of datetime type, and represents the timeframe during
which a visit took place. It has an __overlaps__ method to check if a pair of visits took place at the same time and is tagged 
with the __dataclass__ decorator to implement __eq__ and other comparison methods automatically.


While the possibility of creating a __Visit__ class was considered to store the day and time frame of a visit in a single object,
dictionaries were selected as a better way to do this due to the capability to iterate through its keys by default and the fact that readily available 
in the itertools standard library, like __product__ and __combinations__, could be used without the need for additional definitions. 


The created dictionaries were then associated to their corresponding employee using objects of the __Employee__ class. This class
consists of a name and visits attribute, the name is the string obtained after the initial data extraction while visits is the dictionary
created through __days_dictionary()__ as previously described. It has a __match_visits_of()__ method that compares the list of visits
between two employees and returns how many times they have coincided at the office. Additionaly a __eq__ and a __lt__ method were defined to 
compare objects of this class during testing and sort the employees alphabetically by their names.

The data extraction process described above is repeated for every line of the input .txt file in order to build a list of objects
of the __Employee__ class which __employee_list()__ returns. This list is then sent as an argument to the __match_and_format()__ function which employs 
the __match_visits_of()__ method to find and print the employees that have matched at the office from all the possible combinations of employees using 
__f strings__.

## Architecture
The solution is structured as shown in the following figure:

![architecture](https://github.com/georgegaibor/ioetACME/blob/main/architecture.png)

It consists of a top-level file, run.py, which accesses the following modules:
* classes
* common
* test

The custom modules access the following standard library modules
* itertools 
* datetime
* dataclasses 
* sys
* os

The test module accesses the __pytest__ external module for unit testing. The remaining external modules are used to make sure
the code style is PEP8 compliant.

## Instructions

- Clone the repo

```bash
https://github.com/georgegaibor/ioetACME.git
```

- Create a virtual environment in the root folder of the project

```bash
python3 -m venv venv
```

- Activate the virtual environment 

_Linux/MacOS:_

```bash
source venv/bin/activate 
```

_Windows:_

```cmd
\path\to\env\Scripts\activate
```

- Install dependencies:

```bash
pip3 install -r requirements.txt
```

- Run the project while including the path to the desired input file:

```bash
python3 run.py <input_path>
```

For example using the included sample file:
```bash
python3 run.py schedules.txt
```

### Testing 

Run the test command

```bash
python3 run.py test
```

__Note:__ if you are on windows you may need to use __py__ instead of __python3__ to run the scripts.
