class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and print calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Static method can be called without class context
    result_add = Calculator.add(10, 5)
    print(f"Addition result: {result_add}")

    # Class method has access to class attributes
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication result: {result_multiply}")
