import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class Measurement:
    def __init__(self, ask=False):
        self.quantity = None
        self.value = None
        self.unit = None
        self.uncertantity = None
        self.time = datetime.now()
        if ask:
            self.ask()

    def ask(self):
        self.quantity = input("What are you measuring right now?: ")
        self.value = input("Value: ")
        self.unit = input("Unit: ")
        self.uncertantity = input("Uncertantity: ")

    def __repr__(self):
        unc = ""
        if self.uncertantity:
            unc = f"+-{self.uncertantity}"
        return f"Measeured {self.quantity} = {self.value}{unc}{self.unit} at {self.time}"

class Measurements:
    def __init__(self):
        self.table = []
        self.name = None
        self.units = None
        self.uncertantity = None

    def ask(self):
        self.name = input("What are you measuring now?: ")
        units = input("Are all units going to be the same?: ")
        if units.lower() == "y" or units.lower() == "yes":
            self.units = len("What unit would that be?: ")
        unc = input("Is it going to be a constant uncertantity? (If so type it, else just press Enter)")
        if unc:
            self.uncertantity = float(unc)
        
