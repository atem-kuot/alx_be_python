def  safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            print("Error: Cannot divide by zero.")
            return None
        result = numerator / denominator
    except (TypeError, ValueError):
        print("Error: Please enter numeric values only.")
        return None
    print(f"The result of the division is {result}")
