def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            result = value * 0.621371
            print(f"{value} km = {result:.5f} miles")

        elif choice == "2":
            result = value * 1.60934
            print(f"{value} miles = {result:.5f} km")

        elif choice == "3":
            result = value * 3.28084
            print(f"{value} meters = {result:.5f} feet")

        elif choice == "4":
            result = value * 0.3048
            print(f"{value} feet = {result:.5f} meters")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            result = value * 2.20462
            print(f"{value} kg = {result:.5f} pounds")

        elif choice == "2":
            result = value * 0.453592
            print(f"{value} pounds = {result:.5f} kg")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter temperature: "))

        if choice == "1":
            result = (value * 9 / 5) + 32
            print(f"{value}°C = {result:.2f}°F")

        elif choice == "2":
            result = (value - 32) * 5 / 9
            print(f"{value}°F = {result:.2f}°C")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length_converter()

        elif choice == "2":
            weight_converter()

        elif choice == "3":
            temperature_converter()

        elif choice == "4":
            print("Thank you for using the Unit Converter!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
