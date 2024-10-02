import sys

# There is text containing an arbitrary number of curly braces {}. In addition to the brackets, it can contain any other characters. Write a check function that takes such text as an input parameter, and outputs True if the brackets in the text are correctly placed (the corresponding pairs of opening and closing brackets of any nesting), or False otherwise.
# a}b{c - False, {{abc}} - True. The task must be done in Python.

def validate_brackets_count(text):
    opened_bracket_count = 0
    closed_bracket_count = 0
    for char in text:
        if char == "{":
            opened_bracket_count = opened_bracket_count + 1
        if char == "}":
            if closed_bracket_count >= opened_bracket_count:
                return False
            closed_bracket_count = closed_bracket_count + 1
    return opened_bracket_count == closed_bracket_count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = sys.argv[1]
        if validate_brackets_count(text):
            print(f"The '{text}' is valid")
        else:
            print(f" The '{text}' is not valid")
    else:
        print("The function requires one argument")
