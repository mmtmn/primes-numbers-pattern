from sympy import symbols, Function, Sum, floor, Eq, pprint

# Define the symbols
n, d = symbols('n d')
PrimeCount = Function('PrimeCount')

# Define the refined recursive formula
refined_formula = Eq(PrimeCount(n), Sum(PrimeCount(floor(n / (2**d))), (d, 1, symbols('D'))))

# Display the refined formula
pprint(refined_formula)

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

# Function to check if one bucket contains all primes and no other buckets contain primes
def check_buckets(n, bucket_fraction):
    bucket_size = max(int(n * bucket_fraction), 1)  # Ensure bucket_size is at least 1
    all_primes = [i for i in range(1, n + 1) if is_prime(i)]
    prime_buckets = []
    non_prime_buckets = []

    for i in range(0, n, bucket_size):
        bucket = range(i + 1, min(i + bucket_size + 1, n + 1))
        bucket_primes = [num for num in bucket if is_prime(num)]
        bucket_non_primes = [num for num in bucket if not is_prime(num)]
        if bucket_primes and not bucket_non_primes:
            prime_buckets.append(bucket_primes)
        elif not bucket_primes:
            non_prime_buckets.append(bucket)

    # Check if exactly one bucket contains all primes and no other buckets contain primes
    if len(prime_buckets) == 1 and set(prime_buckets[0]) == set(all_primes) and all(len(bucket) == 0 for bucket in non_prime_buckets):
        return True, prime_buckets[0], len(prime_buckets) + len(non_prime_buckets)
    return False, [], len(prime_buckets) + len(non_prime_buckets)

# Function to test the formula with decreasing bucket fractions and step sizes
def find_prime_bucket(n_points, start_step, end_step, min_fraction):
    current_step = start_step
    total_buckets = 0

    while current_step >= end_step:
        bucket_fraction = 1.0
        while bucket_fraction >= min_fraction:
            found_prime_bucket, prime_bucket, buckets_used = check_buckets(n_points, bucket_fraction)
            total_buckets += buckets_used

            if found_prime_bucket:
                return True, prime_bucket, total_buckets

            bucket_fraction = max(bucket_fraction - current_step, min_fraction)

        current_step /= 10

    return False, [], total_buckets

# Test the formula with decreasing bucket fractions and step sizes
n_points = 100
start_step = 1
end_step = 0.01
min_fraction = 0.01

found_prime_bucket, prime_bucket, total_buckets_used = find_prime_bucket(n_points, start_step, end_step, min_fraction)

if found_prime_bucket:
    print(f"Found a bucket with all primes: {list(prime_bucket)}")
    print(f"Total number of buckets used: {total_buckets_used}")
else:
    print("No bucket with all primes found.")
    print(f"Total number of buckets used: {total_buckets_used}")