def char_exists_at_position(input_str: str, char: str, position: int):
    if len(input_str) > position and input_str[position] == char:
        return True
    return False

def extract_strings_from_list(input_list: list, char: str, position: int):
    res = []
    for word in input_list:
        if char_exists_at_position(word, char, position):
            res.append(word)
            
    return res


if __name__ == "__main__":
    input_list = ["Exxon","Mobil","Bangalore","Bdd","Encapsulation"]
    start_char = "E"
    position = 0
    print(extract_strings_from_list(input_list, start_char, position))