# Write a program that accepts a string separated by spaces.
# For example: one 2 3 zero. Print the first and the last element and the total number of unique elements.
# -> one 2 3 zero
# one zero 4
# -> ten 5 ten 100
# ten 100 3
# -> ten ten ten ten
# ten ten 1

from sortedcontainers import sortedset
from collections import OrderedDict


def print_border_el_and_unique_count(s=str):
    s.replace(' ', '')
    origin_list = list(s.split(' '))
    sorted_set = list(OrderedDict.fromkeys(s.split(' ')))
    first_element = origin_list[0]
    last_element = '' if len(origin_list) <= 1 else origin_list[len(origin_list) - 1]
    print(f"{first_element} {last_element} {len(sorted_set)}")


print_border_el_and_unique_count("one 2 3 zero")
print_border_el_and_unique_count("ten 5 ten 100")
print_border_el_and_unique_count("ten ten ten ten")
