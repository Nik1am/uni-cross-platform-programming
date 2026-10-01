#!/usr/bin/env python

d = {
    "john": "john@mail.net",
    "jane": "jane@mail.net",
    "mark": "mark@mail.net",
    "pete": "pete@mail.net",
}


def print_delim():
    print("-"*40+"\n")


print(f"dictionary `d`: {d}")
print_delim()

# 1:
k, v = "alex", "alex@mail.net"

d[k] = v

print(f"added `{k}` with value `{v}`\nnew dict: {d}")
print_delim()

# 2:
users = {
    "john": {
        "name": "John Smith",
        "mail":  "john@mail.net"
    },
    "jane": {
        "name": "Jane Smith",
        "mail":  "jane@mail.net"
    },
    "alex": {
        "name": "Alex Taylor",
        "mail":  "alex@mail.net"
    },
}

print(f"created a nested dict `users`, user `jane` is {users['jane']}")

print_delim()
# 3:
q = "john"
del d[q]

print(f"removed item `{q}` from original dict\nnew dict: {d}")
print_delim()

# 4:
k = d.keys()
print(f"keys of `d`: {k}")
print_delim()

# 5:
v = d.values()
print(f"values of `d`: {v}")
print_delim()

# 6:
i = d.items()
print(f"items of `d`: {i}")
print_delim()

# 7:
d.update({"pete": "cool_pete@mail.net"})
print(f"updated disct: {d}")
