import pytest
from num_logic.src.number_logic import NumberLogic

number_logic = NumberLogic()


# Functionality Test - Unit test to check whether Code reads Input File correctly
def test_read_input_file():
    input_list_example_unit_test = ["10", "20", "30", "cat"]
    input_list_example_code = number_logic.read_input_file("tests", "input1_test.txt")
    assert input_list_example_code == input_list_example_unit_test, "Failed"


# Exception Test - Unit test to check whether Input File Exists and Raise Exception
def test_read_input_file_exception():
    with pytest.raises(FileNotFoundError):
        input_list_example = number_logic.read_input_file("src/input", "file_does_not_exist.txt")


# Functionality Test - Unit test to check if code correctly converts string to int
def test_convert_str_int():
    int_list = [10, 20, 30]
    str_result = number_logic.convert_str_int(["10", "20", "30"])
    assert int_list == str_result, "Failed"


# Exception Test - Unit test to check if Input File contains valid values (integers not string)
def test_convert_str_int_exception():
    with pytest.raises(ValueError):
        str_result = number_logic.convert_str_int(["10", "20", "30", "cat"])


# Functionality Test - Unit test to check if code correctly checks the list of integers for sum matching pre defined val
def test_check_sum():
    test_result_list = [979, 366, 675]
    result_list = number_logic.check_sum([1721, 979, 366, 299, 675, 1456], 2020)
    assert test_result_list == result_list, "Failed"


# Functionality Test - Unit test to check code correctly multiplies the values in list
def test_multiply_values():
    test_multiplied_value = 241861950
    multiplied_result = number_logic.multiply_values([979, 366, 675])
    assert multiplied_result == test_multiplied_value, "Failed"


# Exception Test - Unit test to check code correctly throws exception when check value is values in list are not int
def test_multiply_values_exception():
    with pytest.raises(ValueError):
        multiplied_result = number_logic.multiply_values([979, 366, "cat"])
