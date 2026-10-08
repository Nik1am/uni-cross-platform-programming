#!/usr/bin/env python

def decorator(func):
    def inner():
        print("Before func call")
        func()
        print("After func call")
    return inner


@decorator
def hello():
    print("Hello, World!")


hello()
