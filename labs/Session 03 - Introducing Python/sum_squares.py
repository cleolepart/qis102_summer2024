#sum_squares.py
#Program description: 'sum_of_squares' calculates the sum of the squares of the first n natural numbers using a loop.
#'gaussian_sum_of_squares' calculates alculate the sum of the squares of the first n natural numbers using the Gaussian summation formula.
#Required argument 'n' is user-defined.

def sum_of_squares(n):
    """Calculate the sum of the squares of the first n natural numbers using a loop."""
    return sum(i ** 2 for i in range(1, n + 1))

def gaussian_sum_of_squares(n):
    """Calculate the sum of the squares of the first n natural numbers using the Gaussian summation formula."""
    return n * (n + 1) * (2 * n + 1) // 6

def main():
    n = 1000

    # Calculate sum of squares using a loop
    loop_sum = sum_of_squares(n)

    # Calculate sum of squares using the Gaussian summation formula
    gaussian_sum = gaussian_sum_of_squares(n)

    # Format the output with commas as thousand separators
    loop_sum_formatted = f"{loop_sum:,}"
    gaussian_sum_formatted = f"{gaussian_sum:,}"

    print(f"Sum of the squares of the first {n} natural numbers (using a loop): {loop_sum_formatted}")
    print(f"Sum of the squares of the first {n} natural numbers (using Gaussian summation): {gaussian_sum_formatted}")

if __name__ == "__main__":
    main()
