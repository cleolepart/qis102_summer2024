#sum_multiples.py
#Program description: 'sum_multiples_of_7_and_11' calculates the sum of all natural numbers less than limit that are divisible by both 7 and 11.
#Required argument 'limit' is user-defined

def sum_multiples_of_7_and_11(limit):
    """Calculate the sum of all natural numbers less than limit that are divisible by both 7 and 11."""

    return sum(i for i in range(1, limit) if i % 7 == 0 and i % 11 == 0)

def main():
    limit = 1900
    total_sum = sum_multiples_of_7_and_11(limit)
    print(f"The sum of all natural numbers less than {limit} that are divisible by both 7 and 11 is: {total_sum}")

if __name__ == "__main__":
    main()
