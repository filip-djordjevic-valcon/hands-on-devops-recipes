from fraction import Fraction
from note import Note
from pause import Pause
from measure import Measure
from composition import Composition

def main():
    # Define durations
    eighth = Fraction(1, 8)
    quarter = Fraction(1, 4)
    half = Fraction(1, 2)

    # Define notes and pauses
    mi_2 = Note(2, 2, half)  # E
    re_4 = Note(2, 1, quarter)  # D
    la_8 = Note(2, 5, eighth)  # A
    sol_4 = Note(2, 4, quarter)  # G
    pause_8 = Pause(eighth)

    # Create measures
    measure1 = Measure(half)
    measure1.add(re_4)
    measure1.finish()

    measure2 = Measure(half)
    measure2.add(mi_2)
    measure2.finish()

    measure3 = Measure(half)
    measure3.add(la_8)
    measure3.add(pause_8)
    measure3.add(sol_4)
    measure3.finish()

    # Create composition
    composition = Composition()
    composition.add(measure1)
    composition.add(measure2)
    composition.add(measure3)

    # Print composition
    print(composition)

if __name__ == "__main__":
    main()