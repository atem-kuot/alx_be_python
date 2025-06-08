# Global conversion factors

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR 
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
