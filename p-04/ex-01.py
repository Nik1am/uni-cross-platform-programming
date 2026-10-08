#!/usr/bin/env python

def operator(op_code):
    def print_number(num):
        print(f"My number is +380 {op_code} {num}")
    return print_number


my_number = operator(66)
my_number(4143135)
