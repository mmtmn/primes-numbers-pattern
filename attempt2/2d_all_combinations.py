import math

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_numbers_and_primes(limit):
    """Generate numbers and identify primes up to a given limit."""
    numbers = list(range(1, limit + 1))
    primes = [is_prime(num) for num in numbers]
    return numbers, primes

def check_alignment(primes, rows, cols):
    """Check if primes align vertically, horizontally, or diagonally."""
    # Check horizontal alignment
    for r in range(rows):
        if all(primes[r * cols + c] for c in range(cols)):
            return True

    # Check vertical alignment
    for c in range(cols):
        if all(primes[r * cols + c] for r in range(rows)):
            return True

    # Check diagonal alignment (top-left to bottom-right)
    if rows == cols:
        if all(primes[i * cols + i] for i in range(rows)):
            return True

    # Check diagonal alignment (top-right to bottom-left)
        if all(primes[i * cols + (cols - 1 - i)] for i in range(rows)):
            return True

    return False

def find_alignments(limit):
    """Find all grid configurations where primes align."""
    numbers, primes = generate_numbers_and_primes(limit)
    alignments = []

    for rows in range(1, limit + 1):
        if limit % rows == 0:
            cols = limit // rows
            if check_alignment(primes, rows, cols):
                alignments.append((rows, cols))

    return alignments

def main():
    limit = 100  # You can change this limit to generate more numbers
    alignments = find_alignments(limit)

    if alignments:
        print(f"Prime numbers align in the following grid configurations for limit {limit}:")
        for rows, cols in alignments:
            print(f"Rows: {rows}, Columns: {cols}")
    else:
        print(f"No alignments found for limit {limit}.")

if __name__ == "__main__":
    main()