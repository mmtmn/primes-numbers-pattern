from sympy import symbols, Function, Sum, floor, Eq

# Define the symbols
n, d = symbols('n d')
PrimeCount = Function('PrimeCount')

# Define the recursive formula
recursive_formula = Eq(PrimeCount(n), Sum(PrimeCount(floor(n / 2**d)), (d, 1, symbols('D'))))

# Display the formula
from sympy import pretty, pprint
pprint(recursive_formula)