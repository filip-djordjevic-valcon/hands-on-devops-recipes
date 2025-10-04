from fraction import Fraction

class MusicalSign:
    def __init__(self, duration):
        self.duration = duration

    def __add__(self, other):
        return self.duration + other.duration
    
    def __str__(self):
        return f"{self.description} ({self.duration})"
    
    def description(self):
        raise NotImplementedError("Subclasses must implement this method")