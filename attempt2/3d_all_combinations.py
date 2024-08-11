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

def check_alignment(primes, rows, cols, depth):
    """Check if primes align vertically, horizontally, or diagonally in 3D."""
    def index(r, c, d):
        return r * cols * depth + c * depth + d

    # Check horizontal alignment in each layer
    for d in range(depth):
        for r in range(rows):
            if all(primes[index(r, c, d)] for c in range(cols)):
                return True

    # Check vertical alignment in each layer
    for d in range(depth):
        for c in range(cols):
            if all(primes[index(r, c, d)] for r in range(rows)):
                return True

    # Check depth alignment in each row and column
    for r in range(rows):
        for c in range(cols):
            if all(primes[index(r, c, d)] for d in range(depth)):
                return True

    # Check diagonal alignment in each layer (top-left to bottom-right)
    if rows == cols:
        for d in range(depth):
            if all(primes[index(i, i, d)] for i in range(rows)):
                return True

    # Check diagonal alignment in each layer (top-right to bottom-left)
        for d in range(depth):
            if all(primes[index(i, cols - 1 - i, d)] for i in range(rows)):
                return True

    # Check diagonal alignment through depth (top-left to bottom-right)
    if rows == depth:
        for c in range(cols):
            if all(primes[index(i, c, i)] for i in range(rows)):
                return True

    # Check diagonal alignment through depth (top-right to bottom-left)
        for c in range(cols):
            if all(primes[index(i, c, depth - 1 - i)] for i in range(rows)):
                return True

    return False

def find_alignments(limit):
    """Find all 3D grid configurations where primes align."""
    numbers, primes = generate_numbers_and_primes(limit)
    alignments = []

    for rows in range(1, limit + 1):
        for cols in range(1, limit // rows + 1):
            if (limit % (rows * cols)) == 0:
                depth = limit // (rows * cols)
                if check_alignment(primes, rows, cols, depth):
                    alignments.append((rows, cols, depth))

    return alignments

def main():
    limit = 100  # You can change this limit to generate more numbers
    alignments = find_alignments(limit)

    if alignments:
        print(f"Prime numbers align in the following 3D grid configurations for limit {limit}:")
        for rows, cols, depth in alignments:
            print(f"Rows: {rows}, Columns: {cols}, Depth: {depth}")
    else:
        print(f"No alignments found for limit {limit}.")

if __name__ == "__main__":
    main()