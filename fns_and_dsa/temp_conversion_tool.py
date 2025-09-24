FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/ 5

def convert_to_celsius(fahrenheit):
    temperature = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celsius):
    temperature = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return temperature

temp = float(input("What's the current temperature? "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp_type == "C" or temp_type.lower() == "celsius":
    print(convert_to_fahrenheit(temp))

elif temp_type == "F" or temp_type.lower() == "fahrenheit":
    print(convert_to_celsius(temp))
else:
    print("Invalid temperature/unit!")
