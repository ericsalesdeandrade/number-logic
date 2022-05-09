# Number Logic and Unit Testing with PyTest
by Eric Sales De Andrade (9 May 2022)

This is an exercise to find 3 numbers in a list whose sum totals a pre-defined value.

The solution is written in Python 3.8.5 and tested using the `pytest` module. Below are instructions how to setup your environment in the `How To Run` section. 

## Repo 
The Repo contains
1. Python Module `number_logic` containing a script `number_logic.py` with the core logic with clear explanation of each function.
2. Input files containing data in the `number-logic/number_logic/src/input` folder. 
3. Unit tests (functionality and exception/error handling checks) under the `tests` folder.

## How To Run
###---------------------------------------------
### Step 1 - Prepare your local environment

#### Install Python and Virtual Environment
As a first step you'll need to prepare a Python environment. 

Mac OS X comes pre installed with Python 2.7, but you'll need to upgrade to `Python 3.8.5`

You can do this with Anaconda (useful for creating a virtual environment) or just install it directly from the web. This link may be useful - https://python.land/installing-python

Follow these instructions for creating a Virtual Environment with Anaconda - https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/

#### Install Requirements
The code uses the `pytest` module so you'll need to install it via pip. To install pip kindly follow the instructions here - https://www.makeuseof.com/tag/install-pip-for-python/

Once you've installed python and pip please navigate to the Root Directory `Wayflyer_ESDA` and run the below command
```
pip install -r requirements.txt
```

###---------------------------------------------

### Step 2 - Run Module `number_logic`
From the Root Directory run
```
python number_logic
```

You should get a similar response as below
```
Number Class Initialised!
Reading Input File from /Users/ericsda/PycharmProjects/Wayflyer_ESDA/num_logic/src/input/input1_short_version.txt
Valid File found
The 3 numbers that sum up to 2020 are [979, 366, 675]
The multiplication of the 3 numbers is 241861950
241861950
```

Now lets run the Unit Test
###---------------------------------------------

### Step 3 - Run Unit Tests
```
pytest ./tests/unit/test_number_logic.py -v -s
```

If the tests pass, you should get a response
```
============================================================================================ test session starts ============================================================================================
platform darwin -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /usr/local/anaconda3/envs/eric_dev/bin/python
cachedir: .pytest_cache
rootdir: /Users/ericsda/PycharmProjects/Wayflyer_ESDA
collected 7 items                                                                                                                                                                                           

tests/test_number_logic.py::test_read_input_file PASSED                                                                                                                                               [ 14%]
tests/test_number_logic.py::test_read_input_file_exception PASSED                                                                                                                                     [ 28%]
tests/test_number_logic.py::test_convert_str_int PASSED                                                                                                                                               [ 42%]
tests/test_number_logic.py::test_convert_str_int_exception PASSED                                                                                                                                     [ 57%]
tests/test_number_logic.py::test_check_sum PASSED                                                                                                                                                     [ 71%]
tests/test_number_logic.py::test_multiply_values PASSED                                                                                                                                               [ 85%]
tests/test_number_logic.py::test_multiply_values_exception PASSED                                                                                                                                     [100%]

============================================================================================= 7 passed in 0.02s =============================================================================================
```
###-----------------------------------------------------------------------------------------

### Congratulations you've run and tested the code successfully
###-----------------------------------------------------------------------------------------
