from functools import partial

def char_startswith(char: str):
    def word_startswith(word: str):
        if len(word) > 0 and word.startswith(char):
            return True
        return False
    return word_startswith

def extract_strings_from_list(check_function, input_list: list):
    res = []
    for word in input_list:
        if check_function(word):
            res.append(word)         
    return res


if __name__ == "__main__":
    input_list = ["Exxon","Mobil","Bangalore","Bdd","Encapsulation"]
    start_char = "E"
    check_function = char_startswith(start_char)
    print(extract_strings_from_list(check_function, input_list))