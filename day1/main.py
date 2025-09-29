from functools import partial

def char_startswith(input_str: str, char: str):
    if len(input_str) > 0 and input_str.startswith(char):
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
    check_function = partial(char_startswith, char = start_char)
    print(extract_strings_from_list(check_function, input_list))