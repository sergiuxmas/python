# Write a program that accepts a string in the format:
# “php = Rasmus Lerdorf; perl = Larry Wall; python = Guido van Rossum”
# Build a dictionary where the keys are the values to the left of "=" and the values are to the right of "=".
# Delimiter is ";".
# Invert the dictionary so that values become keys and keys become values.
# Print the resulting dictionaries in sorted by key form, separated by fiftysymbols “#”.
# It is guaranteed that all values and keys are unique.

from collections import OrderedDict


def strToDictionary(text=str):
    rows = text.strip(' \t\n\r').split(';')
    dictionary = {}
    for row in rows:
        seq = str(row).split('=')
        dictionary.setdefault(seq[0].strip(), seq[1].strip())
    return dictionary


def revert_dictionary(d=dict):
    return {v: k for k, v in d.items()}


def sort_dictionary_by_key(d=dict):
    return OrderedDict(sorted(d.items()))


def print_by_fifty_symbols(d=OrderedDict):
    for elem in d:
        print('#' * 50)
        print(f" key:{elem}, value:{d.get(elem)}")


def main(text=str):
    dictionary = strToDictionary(text)
    dictionary_reverted = revert_dictionary(dictionary)
    dictionary_sorted = sort_dictionary_by_key(dictionary_reverted)
    print_by_fifty_symbols(dictionary_sorted)


main("php = Rasmus Lerdorf; perl = Larry Wall; python = Guido van Rossum")
