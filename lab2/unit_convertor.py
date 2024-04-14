import sys

units = {
    "mm": 1,
    "cm": 10,
    "m": 1000,
    "km": 1000000,
    "mi": 1609344
}

def main():
    
    # Input from stdin
    input = sys.stdin.read().strip().split()
    if len(input) != 2:
        sys.stderr.write("ERROR: Wrong format\n") 
        sys.exit(1)
    
    value = input[0]
    from_unit = input[1]

    # Input from cmd args
    if len(sys.argv) != 2:
        sys.stderr.write("ERROR: Wrong format\n") 
        sys.exit(1)

    to_unit = sys.argv[1]


    try:
        result = convert_units(value, from_unit, to_unit)
        print(f"{result}")
    except ValueError as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(0)


def convert_units(value, from_unit, to_unit):

    try:
        value = float(value)
    except ValueError:
        raise ValueError("Value must be numeric.")
 
    if from_unit not in units or to_unit not in units:
        raise ValueError("Only mm, cm, m, km, mi are accepted.")

    mm_value = value * units[from_unit]

    converted_value = mm_value / units[to_unit]

    return converted_value


if __name__ == "__main__":
    raise SystemExit(main())


'''
тема лаби cli, exitcodes та stdin/stdout/stderr

має працювати: 
echo 100 m | python unit_convertor.py cm
> 10000

тобто програма має мати можливість легко вбудобуватись в пайплайни, без зайвої інтеракції з користувачем

- тести, які перевіряють коди виходу програми (0 якщо все добре, не нуль якщо помилка)
- тести які перевіряють, що помилка пишеться саме в stderr
- тести на те, що значення одиниць для конвертації читаються саме з stdin '''


