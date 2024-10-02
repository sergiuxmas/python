import sys

def count_letter(text, symbol):
    n = 0
    for char in text:
        if char == symbol:
            n = n + 1
    return n

if __name__ == "__main__":
    if len(sys.argv) > 2:
        text = sys.argv[1]
        symbol = sys.argv[2]
        symbol_count = count_letter(text,symbol)
        if symbol_count > 0:
            print(f"In {text} there are {symbol_count} of {symbol}")
        else:
            print(f"{symbol} wasn't find in {text}")
    else:
        print("The function requires 2 arguments")