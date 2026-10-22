#!/usr/bin/env python

class Car:
    def __init__(self, manufacturer, model_name):
        self.manufacturer = manufacturer
        self.model_name = model_name

    def status(self):
        print(f"Hi, i'm {self.manufacturer} {self.model_name}")


class Rental:
    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date


class RentalCar(Car, Rental):
    def __init__(self, manufacturer, model_name, expiry_date):
        super().__init__(manufacturer, model_name)
        super().set_expiry_date(expiry_date)

    def status(self):
        print(f"Hi, i'm rental {self.manufacturer} {
              self.model_name} and my expiry date is: {self.expiry_date}")


my_car = Car("Daewoo", "Lanos")
my_car.status()

my_rental_car = RentalCar("Ferrari", "F40", "21.10.2026")
my_rental_car.status()
