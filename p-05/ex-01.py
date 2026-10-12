#!/usr/bin/env python

"""
Завдання на практику  09.10.2026:
1. напишіть клас із конструктором;
2. напишіть метод для класу з попереднього завдання;
3. додайте метод __str()__  до Вашого класу;
4. додайте статичних атрибутів до Вашого класу.
"""


class Account:
    acc_type = "user"  # 4

    def __init__(self, name):  # 1
        self.name = name

    def greet(self):  # 2
        print(f"Hi! I'm {self.name}.")

    def __str__(self):  # 3
        return f"{self.name} (type = {self.acc_type})"


user = Account("John")
user.greet()
print(user)
