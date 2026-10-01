#!/usr/bin/env python

s = {1, 2, 4, 8, 3, 5, 7, 11}


def print_delim():
    print("-"*40+"\n")


print(f"set `s`: {s}")
print_delim()

# 1:
x = 17
s.add(x)
print(f"added {x} to set `s`\nnew set: {s}")
print_delim()

# 2:
x = 7
s.remove(x)
print(f"removed {x} from set `s`\nnew set: {s}")
print_delim()

# 3:
s_even = {0, 2, 4, 6, 8, 10, 12, 14}

print(f"`s_even`: {s_even}")

print(f"union of sets `s` and `s_even`: {s.union(s_even)}")
print(f"difference of sets `s` and `s_even`: {s.difference(s_even)}")
print(f"intersection of sets `s` and `s_even`: {s.intersection(s_even)}")
print(f"issubset of sets `s` and `s_even`: {s.issubset(s_even)}")
print_delim()

# 4:
x = 4
if x in s:
    print(f"`x` ({x}) is in the set `s`")
else:
    print(f"`x` ({x}) is not in the set `s`")

print_delim()
