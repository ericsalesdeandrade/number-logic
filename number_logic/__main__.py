from src.number_logic import NumberLogic


def main():
    number_example_obj = NumberLogic()
    input_list_example = number_example_obj.read_input_file("number_logic/src/input", "input1_short_version.txt")
    input_list_num_example = number_example_obj.convert_str_int(input_list_example)
    result_list_example = number_example_obj.check_sum(input_list_num_example, 2020)
    multiplied_result_example = number_example_obj.multiply_values(result_list_example)
    print(multiplied_result_example)


if __name__ == '__main__':
    main()
