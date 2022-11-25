"""Homework Lesson #7"""
LIST_OF_WORDS = []
LONG_TEXT = """asdlknfasldkmfasdfasdf"""


def add_word(word):
    """Adds a new word to list of words"""
    LIST_OF_WORDS.append(word)


def get_words(chars):
    """Accepts chars and finds all the words which start with the chars.
    Returns a list of those words in ascending order (length must be up to 5)"""
    filtered_list = list(filter(lambda el: el.startswith(chars), LIST_OF_WORDS))
    filtered_list.sort()
    if len(filtered_list) > 5:
        filtered_list = [filtered_list[i] for i in range(5)]
    return filtered_list


def crop_text(length):
    """Generator yields a text piece of specified length or less"""
    result = ''
    for char in LONG_TEXT:
        result += char
        if len(result) % length == 0:
            yield result
            result = ''
    yield result


if __name__ == '__main__':
    assert get_words('') == []

    add_word('bat')
    add_word('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []

    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')

    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
