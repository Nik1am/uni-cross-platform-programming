#!/usr/bin/env python

def log(func_name):
    def decorator(func):
        def inner():
            print(f"Before {func_name} call")
            func()
            print(f"After {func_name} call")
        return inner
    return decorator


@log(func_name="hello")
def hello():
    print("Hello, World!")


hello()
