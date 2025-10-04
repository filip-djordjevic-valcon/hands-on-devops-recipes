from musical_sign import MusicalSign

class Note(MusicalSign):
    PITCHES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

    def __init__(self, octave, pitch, duration):
        super().__init__(duration)
        self.octave = octave
        self.pitch = pitch

    def shift_up(self, steps):
        self.octave += steps
    
    def shift_down(self, steps):
        self.octave -= steps

    def description(self):
        return self.PITCHES[self.pitch]
