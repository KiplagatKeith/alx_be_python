# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

# Convert Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature

if __name__ == "__main__":
    try:
        # Prompt user for temperature
        temp = float(input("Enter the temperature to convert: "))
        # Prompt user for unit
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if temp_type.lower() in ["c", "celsius"]:
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")

        elif temp_type.lower() in ["f", "fahrenheit"]:
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")

        else:
            raise ValueError("Invalid temperature unit. Please enter C or F.")

    except ValueError:
        # Handle invalid numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")
