# Write a program that replaces all non-letters with spaces
s = 'this =- is , bad ! text #$%^123%^#&'


def is_letter(letter=str):
    if letter.lower() == letter.upper():
        return False
    return True


def replace_letter_if_symbol(text=str):
    s_builder = []
    for element in text:
        if is_letter(element):
            s_builder.append(element)
        else:
            s_builder.append(' ')
    return ''.join(s_builder)


print(replace_letter_if_symbol(s))
