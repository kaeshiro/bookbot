def get_num_words(text):
    return len(text.split())


def get_num_char(text):
    chars = {}
    for c in text:
        lower_c = c.lower()
        if lower_c not in chars:
            chars[lower_c] = 1
        else:
            chars[lower_c] += 1
    return chars


def sort_on(d):
    return(d["num"])


def sort_dict(chars_dict):
    list_of_dicts = []
    for char in chars_dict:
        num = chars_dict[char]
        list_of_dicts.append({"char": char, "num": num})
        list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
