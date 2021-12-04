import os
import sys
from pathlib import Path
from functools import reduce


class NumberLogic:
    """
    Class to Calculate Number Logic
    """

    def __init__(self):
        print("Number Class Initialised!")

    @staticmethod
    def read_input_file(file_path: str, file_name: str) -> list:
        """
        Function to read input file and save each line as a list of values
        :param file_path: Filepath within  the parent folder/repo e.g. 'src/input' in string format
        :param file_name: Filename in string format
        :return: Returns a list where each element is a new line from the file read
        """
        try:
            file_path_updated = Path.cwd() / file_path / file_name
            print(f"Reading Input File from {file_path_updated}")
            with open(file_path_updated, 'r') as f:
                try:
                    if os.stat(file_path_updated).st_size > 0:
                        print("Valid File found")
                    else:
                        print("Empty file")
                        sys.exit(0)
                except OSError:
                    print("No file")
                data_read = [line.strip() for line in f]
                f.close()
                return data_read
        except FileNotFoundError:
            print(f'ERROR - File {file_name} does not exist')
            raise FileNotFoundError
        except Exception as error:
            print("Error Reading Input File")
            raise error

    @staticmethod
    def convert_str_int(input_list_str: list) -> list:
        """
        Function to convert all elements in a list to int
        :param input_list_str: List containing values in string format
        :return: list containing values in int format
        """
        try:
            input_list_int = list(map(int, input_list_str))
            return input_list_int
        except ValueError as error:
            print("String Value in Input File. Please ensure input only contains numbers. Skipping for NOW")
            raise error
            pass
        except Exception as error:
            print("Error Converting List to int")
            raise error

    @staticmethod
    def check_sum(input_data: list, check_value: int) -> list:
        """
        Function to check the sum of 3 values in the list and compare against a pre defined value
        :param input_data: Input list with elements in int format
        :param check_value: Value to be compared with in int format
        :return: Returns list of 3 numbers who's sum totals the check_value, list
        """
        try:
            result_list = []
            if isinstance(check_value, int):
                for i in range(len(input_data)):
                    for j in range(i + 1, len(input_data)):
                        for k in range(j + 1, len(input_data)):
                            if input_data[i] + input_data[j] + input_data[k] == check_value:
                                result_list.extend([input_data[i], input_data[j], input_data[k]])
                                print(f"The 3 numbers that sum up to 2020 are {result_list}")
                                return result_list
            else:
                raise ValueError("Check Value is NOT Integer. Exiting...")
        except Exception as error:
            print("Error In Check Sum Functionality")
            raise error

    @staticmethod
    def multiply_values(list_of_val: list) -> int:
        """
        Function to multiply values of a list
        :param list_of_val: List of values in int format
        :return: Returns result of multiplying values in the list
        """
        try:
            if isinstance(list_of_val, list):
                if all(isinstance(element, int) for element in list_of_val):
                    result = reduce(lambda x, y: x * y, list_of_val)
                    print(f"The multiplication of the 3 numbers is {result}")
                    return result
                else:
                    raise ValueError("All elements in the list are not integers")
        except TypeError as error:
            print("Check Value should be integer")
            raise error
        except Exception as error:
            print("Error In Multiply Functionality")
            raise error