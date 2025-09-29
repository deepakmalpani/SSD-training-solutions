def extract_strings_from_list(arr: list, start_char: str):
    res = []
    for a in arr:
        if a[:1] == start_char:
            res.append(a)
            
    return res


if __name__ == "__main__":
    input_list = ["Exxon","Mobil","Bangalore","Bdd","Encapsulation"]
    start_char = "E"
    print(extract_strings_from_list(input_list, start_char))