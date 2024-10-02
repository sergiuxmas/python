from turtledemo.paint import switchupdown

# Write a program that goes through the list and displays whether the value is an int, float, or not a numeric type.

lst = [0, 1, 245.0, 3.17, "2.50", "eight", False, "", True]


def show_type_of_each_element(expected_types=()):
    checked = False
    for element in lst:
        for t in expected_types:
            if isinstance(element, t):
                print(f"{element} is {t}")
                checked = True
                break
        if not checked:
            print(f"{element} is not a numeric type")
        checked = False


show_type_of_each_element((int, float))
