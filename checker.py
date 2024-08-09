from sympy import symbols, Function, Sum, floor, Eq, lambdify
import numpy as np

# Define the symbols
n, d = symbols('n d')
PrimeCount = Function('PrimeCount')

# Define the recursive formula
recursive_formula = Eq(PrimeCount(n), Sum(PrimeCount(floor(n / 2**d)), (d, 1, symbols('D'))))

# Display the formula
from sympy import pretty, pprint
pprint(recursive_formula)

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Recursive function to count primes in the second bucket
def PrimeCount_recursive(n):
    if n <= 1:
        return 0
    primes_in_bucket = [i for i in range(1, n + 1) if is_prime(i)]
    return len(primes_in_bucket) + PrimeCount_recursive(n // 2)

# Test the formula
n_points = 10000000
primes_in_second_bucket = PrimeCount_recursive(n_points)

# Check if all numbers in the second bucket are primes
second_bucket = [i for i in range(1, n_points // 2 + 1)]
second_bucket_primes = [i for i in second_bucket if is_prime(i)]

print(f"Number of primes in the second bucket for {n_points} points: {primes_in_second_bucket}")
print(f"Primes in the second bucket: {second_bucket_primes}")
print(f"All numbers in the second bucket are primes: {all(is_prime(i) for i in second_bucket)}")