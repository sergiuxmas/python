import sys

if __name__ == "__main__":
    # string
    a, path = "Hello", "c/user/World"
    b = path.split('/')
    c = path[2:-6]
    d = a[::-1]
    print(f" string: {d}")

    # list
    l = [0, 2, 'c']
    l += [3,4]
    l.append('d')
    print(f" list: {l}")
    print(f" last element from list: {l.pop()}")
    print(f" list: {l}")

    # tuple
    t = (4, 10, 'text')
    print(f" tuple: {t}")

    # bytes
    b = list(b"text123".decode('ascii'))
    print(f" bytes: {b}")
