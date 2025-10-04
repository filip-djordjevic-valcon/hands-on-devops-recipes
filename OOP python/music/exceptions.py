class AddError(Exception):
    def __init__(self, message="Adding is not allowed"):
        super().__init__(self.message)

class IndexError(Exception):
    def __init__(self, message="Invalid index"):
        super().__init__(self.message)
    
class DurationError(Exception):
    def __init__(self, message="Exceeded measure duration"):
        super().__init__(self.message)
