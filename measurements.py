import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class Measurement:
    def __init__(self, ask=False):
        self.quantity = None
        self.value = None
        self.unit = None
        self.uncertainty = None
        self.time = datetime.now()
        if ask:
            self.ask()

    def ask(self):
        self.quantity = input("What are you measuring right now?: ")
        self.value = input("Value: ")
        self.unit = input("Unit: ")
        self.uncertainty = input("Uncertanty: ")

    def __repr__(self):
        unc = ""
        if self.uncertainty:
            unc = f"+-{self.uncertanty}"
        return f"Measeured {self.quantity} = {self.value}{unc}{self.unit} at {self.time}"

class Measurements:
    def __init__(self):
        self.table = []
        self.name = None
        self.units = None
        self.uncertainty = None
        self.np = np.array([])

    def ask(self):
        if not self.name:
            self.name = input("What are you measuring now?: ")
        if not self.units:
            units = input("Are all units going to be the same?: ")
            if units.lower() == "y" or units.lower() == "yes":
                self.units = input("What unit would that be?: ")
        if not self.uncertainty:
            unc = input("Is it going to be a constant uncertainty? (If so type it, else just press Enter): ")
            if unc:
                self.uncertainty = float(unc)
        keep_going = True
        while(keep_going):
            measurement = input("Type next value(or press enter to quit): ")
            if not measurement:
                keep_going = False
                break
            if not self.units:
                unit = input("Unit: ")
            else:
                unit = self.units

            if not self.uncertainty:
                unc = float(input(f"Uncertainty [{unit}]: "))
            else:
                unc = self.uncertainty
            m = Measurement()
            m.quantity = self.name
            m.value = float(measurement)
            m.unit = unit
            m.uncertainty = unc
            self.table.append(m)
            print(f"Adding {m.value}{m.unit} to the table")

        self.save_np()

    def save_np(self):
        for item in self.table:
            self.np = np.append(self.np, item.value)

    def graph(self):
        plt.bar(range(len(self.np)), self.np, yerr=self.uncertainty)
        plt.show()

    def calc_uncertanty(self):
        self.uncertainty = np.mean(np.array([item.uncertainty for item in self.table]))
        print(self.uncertainty)

m = Measurements()
for item in [45, 44.4, 46, 47, 45.9, 46.1, 44.9]:
    m1 = Measurement()
    m1.quantity = "Power"
    m1.unit = "W",
    m1.uncertainty = 2
    m1.value = item
    m.table.append(m1)

m.save_np()
m.calc_uncertanty()
m.graph()
