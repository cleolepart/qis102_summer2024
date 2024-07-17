# hamming_weight.py
# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

class HammingWeightCalculator:
    """
    A class to calculate and display the Hamming weight of a number.
    """
    
    def __init__(self, number):
        """
        Initialize the HammingWeightCalculator with the given number.
        
        Parameters:
        number (int): The number to calculate the Hamming weight for.
        """
        self.number = number

    def calculate_hamming_weight(self):
        """
        Calculate the Hamming weight of the number.
        
        Returns:
        int: The Hamming weight of the number.
        """
        return bin(self.number).count('1')

    def display_hamming_weight(self):
        """
        Display the Hamming weight of the number.
        """
        weight = self.calculate_hamming_weight()
        print(f"The Hamming weight of {self.number} is: {weight}")

def main():
    """
    Main function to execute and display the HammingWeightCalculator.

    Argument(s):
    int: number whose Hamming weight is to be calculated, user-defined 
    """
    number = 95601
    calculator = HammingWeightCalculator(number)
    calculator.display_hamming_weight()

if __name__ == "__main__":
    main()
