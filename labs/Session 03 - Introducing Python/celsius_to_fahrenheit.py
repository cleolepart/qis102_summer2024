#celsius_to_fahrenheit.py
#Program description: 'celsius_to_fahrenheit' converts Celsius temperature to Fahrenheit.
#Required argument is a range of Celsius values that will be converted and displayed against Farhenheit with 2 decimal place-formatting.

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def main():
    """Display correctly spaced column headers"""
    print(f"{'Celsius':>10} {'Fahrenheit':>12}")
    """Insert bar of correct length underneath"""
    print("-" * 23)
    
    """For a given range in Celsius, display the Fahrenheit temperature. Display correctly formatted and to 2 decimal places."""
    for celsius in range(-44, 105, 4):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:10.2f} {fahrenheit:12.2f}")

    # Verify correctness with specific values
    test_values = [0, 100, -40]
    for celsius in test_values:
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\nVerification: {celsius}°C = {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
