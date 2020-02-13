import math
import matplotlib.pyplot as plt
import random
import functions

random.seed(1)

class Sensory:
    def __init__(self, activation='linear'):
        self.activation_function = functions.func(activation)
        self.output = 0
        self.history = []

    def activate(self, i):
        self.output = self.activation_function(i)
        self.history.append(self.output)

class Unit:
    def __init__(self):
        self.resting_potential = -65
        self.membrane_potential_temp = -65
        self.membrane_potential = -65
        self.threshold_potential = -20
        self.action_potential = 1000
        self.refractory_period = 20
        self.refractory_period_temp = 20
        self.input_units = []
        self.output = self.membrane_potential
        self.output_temp = self.membrane_potential_temp
        self.input_history = []
        self.history = []

    def activate(self):
        if self.membrane_potential_temp >= self.threshold_potential:
            self.membrane_potential_temp = self.action_potential
            self.refractory_period_temp += 50

        if self.refractory_period > 1:
            self.refractory_period_temp -= 1

        self.output_temp += 0.05 * (self.membrane_potential - self.output)

        self.history.append(self.output)
        self.input_history.append(self.inputs())

        if self.membrane_potential >= self.action_potential:
            self.membrane_potential_temp = self.resting_potential - 30

        self.membrane_potential_temp += 0.01 * (self.resting_potential - self.membrane_potential + (1 / self.refractory_period) * self.inputs())

    def inputs(self):
        i = 0
        for n in self.input_units:
            i += n.output
        return i

    def add_input(self, unit):
        self.input_units.append(unit)

    def update(self):
        self.membrane_potential = self.membrane_potential_temp
        self.output = self.output_temp
        self.refractory_period = self.refractory_period_temp

    def __str__(self):
        return str(self.membrane_potential_temp)


class Network:
    def __init__(self, i=256):
        # Create the input layer of sensory neurons paired with unit neurons
        self.sensory_layer = []
        self.layer_0 = []
        for x in range(0, i):
            s = Sensory(activation='linear')
            u = Unit()
            u.add_input(s)
            self.sensory_layer.append(s)
            self.layer_0.append(u)


    def simulate(self, input):
        for s in self.sensory_layer:
            s.activate(1)
        for u in self.layer_0:
            u.activate()
