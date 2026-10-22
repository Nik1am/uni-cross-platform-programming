#!/usr/bin/env python

class Entity:
    def __init__(self, name):
        self.health_points = 100
        self.name = name


class Animal(Entity):
    def go_to(self, x, y):
        print(f"(Walking to [{x},{y}])")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"[{self.name}]: meow.")


my_cat = Cat("Barsik")
my_cat.go_to(100, 200)
my_cat.speak()
