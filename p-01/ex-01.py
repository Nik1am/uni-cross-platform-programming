#!/usr/bin/python

def greet(*cars):
    print(f"Avaible cars: {' '.join(cars)}")


greet("Daewoo", "BMW", "Toyota")
