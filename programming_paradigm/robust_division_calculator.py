def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float first (could raise ValueError)
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division (could raise ZeroDivisionError)
        division = numerator / denominator
        return f"The result of the division is {division}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
