import pytest


def test_read_input_file(number_logic) -> None:
    """
    Test to Check whether the code reads a file correctly and completely from a specified path
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    input_list_example_unit_test = ["10", "20", "30", "cat"]
    input_list_example_code = number_logic.read_input_file("tests/unit", "input1_test.txt")
    assert input_list_example_code == input_list_example_unit_test, "Failed"


def test_read_input_file_exception(number_logic) -> None:
    """
    Tests to check whether code throws a FileNotFoundError if a file is not found
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    with pytest.raises(FileNotFoundError):
        input_list_example = number_logic.read_input_file("src/input", "file_does_not_exist.txt")


def test_convert_str_int(number_logic) -> None:
    """
    Test to check whether code correctly converts string to int
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    int_list = [10, 20, 30]
    str_result = number_logic.convert_str_int(["10", "20", "30"])
    assert int_list == str_result, "Failed"


def test_convert_str_int_exception(number_logic) -> None:
    """
    Test to check if Input File contains valid values (integers not string) and raises ValueError if input file
    contains a string
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    with pytest.raises(ValueError):
        str_result = number_logic.convert_str_int(["10", "20", "30", "cat"])


def test_check_sum(number_logic) -> None:
    """
    Tests to check if code correctly checks the list of integers for sum matching pre defined val
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    test_result_list = [979, 366, 675]
    result_list = number_logic.check_sum([1721, 979, 366, 299, 675, 1456], 2020)
    assert test_result_list == result_list, "Failed"


def test_multiply_values(number_logic) -> None:
    """
    Test to check whether code correctly multiplies the values in list
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    test_multiplied_value = 241861950
    multiplied_result = number_logic.multiply_values([979, 366, 675])
    assert multiplied_result == test_multiplied_value, "Failed"


def test_multiply_values_exception(number_logic) -> None:
    """
    Test to check code correctly throws exception when check value is values in list are not int
    :param number_logic: Pytest Fixture as specified in the ConfTest File
    :return: None
    """
    with pytest.raises(ValueError):
        multiplied_result = number_logic.multiply_values([979, 366, "cat"])
