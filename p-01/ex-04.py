#!/usr/bin/python

import random

number_to_guess = random.randint(0, 1000)

print("Guess the number! Type 'exit' to exit.")
while True:
    inp = input("> ")

    if inp.lower() == "exit":
        break

    if not inp.isdigit():
        print("Not a number!")
        continue

    inp = int(inp)
    if inp > number_to_guess:
        print("Too big")
    elif inp < number_to_guess:
        print("Too small")
    else:
        print("Bingo!")
        break
