#!/usr/bin/env python

class Cpu:
    def __init__(self, freq):
        self.cpu_freq = freq


class Ram:
    def __init__(self, freq, capacity):
        self.ram_freq = freq
        self.ram_capacity = capacity


class Pc(Cpu, Ram):
    def __init__(self, cpu_freq, ram_freq, ram_capacity):
        Cpu.__init__(self, cpu_freq)
        Ram.__init__(self, ram_freq, ram_capacity)

    def info(self):
        print("PC Specs:")
        for k, v in self.__dict__.items():
            print(f"{k}:\t{v}")


my_pc = Pc("4200 MHz", "3200 MHz", "16 GB")
my_pc.info()
