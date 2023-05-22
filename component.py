from abc import ABC, abstractmethod
from itertools import combinations
from random import randint
import time


class Component(ABC):
    @abstractmethod
    def calculate_magnitude(self):
        pass
    
class Resistor(Component):
    calculate_count = 0
    def __init__(self, magnitude):
        self.magnitude = magnitude
        
    def calculate_magnitude(self):
        Resistor.calculate_count += 1
        return self.magnitude
    
    def __str__(self):
        return str(self.magnitude)
    
class SeriesCircuit(Component):
    def __init__(self, components): 
        self.components = components
    
    def calculate_magnitude(self):
        return sum(component.calculate_magnitude() for component in self.components)
    
    def __str__(self):
        return "(S" + ' '.join(str(c) for c in self.components) + ")"


class ParalelCircuit(Component):
    def __init__(self, components):
        self.components = components
        
    def calculate_magnitude(self):
        return 1/sum(1/component.calculate_magnitude() for component in self.components)
    
    def __str__(self):
        return "(P" + ' '.join(str(c) for c in self.components) + ")"
                                            



    