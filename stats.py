def get_num_words(text_string):
    return len(text_string.split())

def get_letter_count(text_string):
    counts = {}
    for chars in text_string[::]:
        for char in chars:
            char = char.lower()
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
    return counts

def sort_on(items):
    return items["num"]

def get_char_list_as_dict(text_string):
    counts = get_letter_count(text_string)
    dicts = []
    for key, value in counts.items():
        dicts.append(
            {
                "char": key,
                "num": value,
            }
        )
    dicts.sort(reverse=True, key=sort_on)
    return dicts