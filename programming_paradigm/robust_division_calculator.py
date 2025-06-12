def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            print("Error: Cannot divide by zero.")
            return None
        result = numerator/denominator
        return result
    except (TypeError, ValueError):
        print("Error: Please enter numeric values only.")
        return None
    
