import sys

def main():

    try:
        print("Enter value: ")
        value = sys.stdin.readline().strip()

        from_unit = input("Type initial units: ").strip().lower()
        to_unit = input("Type desired units: ").strip().lower()
        result = convert_units(value, from_unit, to_unit)

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

'''тема лаби cli, exitcodes та stdin/stdout/stderr

має працювати: 
echo 100 m | python unit_convertor.py cm
> 10000

тобто програма має мати можливість легко вбудобуватись в пайплайни, без зайвої інтеракції з користувачем

- тести, які перевіряють коди виходу програми (0 якщо все добре, не нуль якщо помилка)
- тести які перевіряють, що помилка пишеться саме в stderr
- тести на те, що значення одиниць для конвертації читаються саме з stdin '''

