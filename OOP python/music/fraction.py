class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
