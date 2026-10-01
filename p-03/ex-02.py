#!/usr/bin/env python

t = (1, 2, 4, 8, 3, 5, 7, 13)


def print_delim():
    print("-"*40+"\n")


print(f"tuple `t`: {t}")
print_delim()

# 1:
x = 4
if x in t:
    print(f"`x` ({x}) is in the tuple `t`")
else:
    print(f"`x` ({x}) is not in the tuple `t`")

print_delim()

# 2:
sl = t[2:5]
print(f"slice [2:5] of `t` is {sl}")

print_delim()


# 3:
minimum = min(t)
maximum = max(t)

print(f"min: {minimum}\nmax: {maximum}")

print_delim()

# 4:
print(f"before: {t}")

x = 10
l: list = list(t)
# my IDE was complaining about the line below, so i had to specify the type
l[0] = x
t = tuple(l)

print(f"after: {t}")

print_delim()

# 5:
a, b, c, d, e, f, g, h = t
print("unpacked the tuple into variables a..h")
print(f"`a`: {a}")
print(f"`b`: {b}")
print("...")
print(f"`h`: {h}")

print_delim()

# 6:

for i in range(len(t)):
    print(f"t[{i}] = {t[i]}")
