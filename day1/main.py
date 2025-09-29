from functools import partial

def char_exists_at_position(input_str: str, char: str, position: int):
    if len(input_str) > position and input_str[position] == char:
        return True
    return False

def extract_strings_from_list(check_function, input_list: list):
    res = []
    for word in input_list:
        if check_function(word):
            res.append(word)         
    return res


if __name__ == "__main__":
    input_list = ["Exxon","Mobil","Bangalore","Bdd","Encapsulation"]
    start_char = "E"
    position = 0
    check_function = partial(char_exists_at_position, position = position, char = start_char)
    print(extract_strings_from_list(check_function, input_list))