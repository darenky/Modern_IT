import sys

def main():

    value = input("Enter value: ")
    try:
        value = float(value)
    except ValueError:
        print("Invalid value")

    from_unit = input("Type initial units: ").strip().lower()
    to_unit = input("Type desired units: ").strip().lower()
    result = convert_units(value, from_unit, to_unit)
    print(f"{result} {to_unit}")
  
    

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "km": 1000000,
        "mi": 1609344
    }

    if not from_unit or not to_unit or not value:
        raise ValueError("Invalid input")
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid input")

    mm_value = value * conversion_factors.get(from_unit)

    converted_value = mm_value / conversion_factors.get(to_unit)

    return converted_value


if __name__ == "__main__":
    main()

