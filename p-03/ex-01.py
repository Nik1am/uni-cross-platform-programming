#!/usr/bin/env python

l = [1, 2, 4, 8, 3, 7, 5, 18]


def print_delim():
    print("-"*40+"\n")


print(f"list `l`: {l}")
print_delim()

# 1:
x = 4
if x in l:
    print(f"`x` ({x}) is in the list `l`")
else:
    print(f"`x` ({x}) is not in the list `l`")

print_delim()

# 2:
sl = l[2:5]
print(f"slice [2:5] of `l` is {sl}")

print_delim()

# 3:
x = 42
l.append(x)
print(f"added {x} to the end of the list\nnew list: {l}")

x = 27
l.insert(0, x)
print(f"added {x} to the beginning of the list\nnew list: {l}")

print_delim()

# 4:
x = l.pop()
print(f"removing (popping) an item ({x}) from the list\nnew list: {l}")

x = 8
l.remove(x)
print(f"removing a specific item ({x}) from the list\nnew list: {l}")

print_delim()

# 5:
l = [
    [1, 2, 3],
    [4, 8, 12],
    [7, 14, 21]
]

i = 1
j = 2
print(f"created a nested list `l`: {l}\nl[{i}][{j}] = {l[i][j]}")

print_delim()

# 6:
for i in range(len(l)):
    print(f"l[{i}]: {l[i]}")

print_delim()

# 7:
l = [
    "lorem",
    "ipsum",
    "dolor",
    "sit",
    "amet"
]

print(f"created a list of strings: {l}")
l.sort()
print(f"sorted list: {l}")

print_delim()

# 8:
q = "lorem"
x = l.count(q)
print(f"`{q}` appears in {l} {x} times")

print_delim()

# 9:
i = l.index(q)
print(f"index of `{q}` is {i}")
