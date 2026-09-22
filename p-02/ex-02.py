#!/usr/bin/env python

number_list = range(-5, 5)
lst2 = ["Barber", "Taxi Driver", "Python Developer",
        "Data Scientist", "Game Developer"]
lst1 = [1, 3, 4, 6, 10, 11, 15, 12, 14]

IT_jobs = ["Python Developer",
           "Data Scientist", "Game Developer"]


def less_than_zero(x: int):
    return x < 0


def is_IT_job(job: str):
    return job in IT_jobs


def is_even(x: int):
    return x % 2 == 0


# 1:
print("1:", list(number_list), "->", list(filter(less_than_zero, number_list)))

# 2:
print("2:", lst2, "->", list(filter(is_IT_job, lst2)))


# 3:
print("1:", list(lst1), "->", list(filter(is_even, lst1)))

print("List comprehension approach:")

# 1:
print("1:", list(number_list), "->", [i for i in number_list if i < 0])

# 2:
print("2:", lst2, "->", [i for i in lst2 if i in ["Python Developer",
                                                  "Data Scientist",
                                                  "Game Developer"]])

# 3:
print("1:", list(lst1), "->", [i for i in lst1 if i % 2 == 0])
