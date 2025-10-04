class AddError(Exception):
    """Custom exception raised when adding is not allowed."""
    pass

class Sequence:
    def __init__(self, sequence):
        self.sequence = []
        self._can_add = True

    def add(self, element):
        if not self._can_add:
            raise AddError("Adding is not allowed after taking an element")
        self._elements.append(element)
    
    def take(self):
        if not self._elements:
            raise IndexError("Sqeuence is empty")
        self._can_add = False
        return self._elements.pop(0)
    
    def get(self, index):
        if index < 0 or index >= len(self._elements):
            raise IndexError("Index out of range")
        return self._elements[index]

    def lenght(self):
        return len(self._elements)