from exceptions import AddError, IndexError, DurationError
from fraction import Fraction
from sequence import Sequence

class Measure:
    def __init__(self, max_duration):
        self.max_duration = max_duration
        self.current_duration = Fraction(0)
        self.signs = Sequence()
        self.finished = False

    def add(self, sign):
        if self.finished:
            raise AddError("Measure is finished")
        if self.current_duration + sign.duration > self.max_duration:
            raise DurationError("Exceeded measure duration")
        self.signs.add(sign)
        self.current_duration += sign.duration
    
    def finish(self):
        self.finished = True

    def is_incomplete(self):
        return self.current_duration < self.max_duration
    
    def __str__(self):
        return " ".join(str(self.signs.get(i)) for i in range(self.signs.lenght())) + " |"