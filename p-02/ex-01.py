#!/usr/bin/env python

lst = ["One", "Two", "Three", "Four", "Five"]
lst2 = [1, 2, 3, 4, 5]


def replace_string_with_digit(s: str):
    match s:
        case "One":
            return 1
        case "Two":
            return 2
        case "Three":
            return 3
        case "Four":
            return 4
        case "Five":
            return 5


def replace_digit_with_string(d: int):
    match d:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"


def square(x: int):
    return x ** 2


# 1:
print("1:", lst, "->", list(map(replace_string_with_digit, lst)))

# 2:
print("2:", lst2, "->", list(map(replace_digit_with_string, lst2)))

# 3:
print("3:", lst2, "->", list(map(square, lst2)))


print("List comprehension approach:")

# 1:
print("1:", lst, "->", [replace_string_with_digit(i) for i in lst])

# 2:
print("2:", lst2, "->", [replace_digit_with_string(i) for i in lst2])

# 3:
print("3:", lst2, "->", [square(i) for i in lst2])
