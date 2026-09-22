#!/usr/bin/env python

cars = ["Honda", "Mazda", "Toyota", "Audi", "BMW", "Ford", "Dodge"]

# 1:
print("1:", [car for car in cars if "a" in car])

# 2:
print("1:", [car for car in cars if len(car) <= 4])
