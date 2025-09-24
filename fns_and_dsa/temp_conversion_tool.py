# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature

try:
    temp = float(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temp_type.lower() in ["c", "celsius"]:
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")

    elif temp_type.lower() in ["f", "fahrenheit"]:
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")

    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
