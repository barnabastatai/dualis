from pathlib import Path
from parking import Parking
from fee_calculator import FeeCalculator
from parking import Parking


def main():

    parking = []

    data = Path("input.txt").read_text(encoding="utf-8").splitlines()[2:]

    for line in data:
        parking.append(Parking(line))

    for p in parking:
        calculator = FeeCalculator()
        print(calculator.calculate_fee(p.get_duration()))

if __name__ == "__main__":
    main()
