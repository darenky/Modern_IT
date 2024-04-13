import sys

def main():
    try:
        value_and_from_unit = sys.stdin.readline().strip()
        to_unit = sys.argv[1].lower()

        if len(sys.argv) != 2:
            print("Usage: python unit_convertor.py <to_unit>")
            return 1

        # Split the input string into value and from_unit
        value, from_unit = value_and_from_unit.split()

        result = convert_units(value, from_unit.lower(), to_unit)
        print(f"{result}")
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1


def convert_units(value, from_unit, to_unit):

    conversion_factors = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "km": 1000000,
        "mi": 1609344
    }

    try:
        value = float(value)
    except ValueError:
        raise ValueError("VALUE MUST BE NON-NEGATIVE NUMERIC")
 
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("ONLY mm,cm,m,km,mi ARE ACCEPTED")

    mm_value = value * conversion_factors.get(from_unit)

    converted_value = mm_value / conversion_factors.get(to_unit)

    return converted_value

if __name__ == "__main__":
    main()