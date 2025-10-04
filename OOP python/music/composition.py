from sequence import Sequence
from exceptions import AddError

class Composition:
    def __init__(self):
        self.measure = Sequence()
        self.first_measure = True
        self.allow_incomplete = True
        self.max_duration = None

    def add(self, measure):
        if not measure.finished:
            raise AddError("Measure is not finished")
        if self.first_measure:
            self.max_duration = measure.max_duration
            self.first_measure = False
        elif measure.max_duration != self.max_duration:
            raise AddError("Inconsistent measure duration")
        if measure.is_incomplete() and not self.allow_incomplete:
            raise AddError("Incomplete measure not allowed")
        self.allow_incomplete = measure.is_incomplete()
        self.measures.add(measure)

def __str__(self):
        return "\n".join(str(self.measures.get(i)) for i in range(self.measures.length()))