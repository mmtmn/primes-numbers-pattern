import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def check_alignment(primes, rows, cols, depth, angle):
    """Check if primes align in a single continuous line or curve in 3D."""
    def index(r, c, d):
        return r * cols * depth + c * depth + d

    prime_positions = [(r, c, d) for r in range(rows) for c in range(cols) for d in range(depth) if primes[index(r, c, d)]]

    # Check all possible lines and curves in 3D space
    for r1, c1, d1 in prime_positions:
        for r2, c2, d2 in prime_positions:
            if (r1, c1, d1) != (r2, c2, d2):
                dr, dc, dd = r2 - r1, c2 - c1, d2 - d1
                gcd = math.gcd(math.gcd(abs(dr), abs(dc)), abs(dd))
                dr, dc, dd = dr // gcd, dc // gcd, dd // gcd

                aligned_positions = []
                r, c, d = r1, c1, d1
                while 0 <= r < rows and 0 <= c < cols and 0 <= d < depth:
                    if primes[index(r, c, d)]:
                        aligned_positions.append((r, c, d))
                    r += dr
                    c += dc
                    d += dd

                if len(aligned_positions) == len(prime_positions):
                    return aligned_positions

                # Check for curves
                for theta in range(1, angle + 1):
                    theta_rad = math.radians(theta)
                    cos_theta, sin_theta = math.cos(theta_rad), math.sin(theta_rad)
                    r, c, d = r1, c1, d1
                    aligned_positions = [(r, c, d)]
                    while 0 <= r < rows and 0 <= c < cols and 0 <= d < depth:
                        r += int(dr * cos_theta - dc * sin_theta)
                        c += int(dr * sin_theta + dc * cos_theta)
                        d += dd
                        if 0 <= r < rows and 0 <= c < cols and 0 <= d < depth and primes[index(r, c, d)]:
                            aligned_positions.append((r, c, d))
                        else:
                            break

                    if len(aligned_positions) == len(prime_positions):
                        return aligned_positions

    return None

def find_alignments(limit, angle):
    """Find all 3D grid configurations where primes align."""
    numbers, primes = generate_numbers_and_primes(limit)
    alignments = []

    for rows in range(2, limit + 1):
        for cols in range(2, limit // rows + 1):
            if (limit % (rows * cols)) == 0:
                depth = limit // (rows * cols)
                if depth > 1:
                    alignment = check_alignment(primes, rows, cols, depth, angle)
                    if alignment:
                        alignments.append(alignment)

    return alignments

def visualize_alignments(alignments, limit):
    """Visualize the 3D grid configurations where primes align."""
    numbers, primes = generate_numbers_and_primes(limit)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    current_index = [0]
    show_line = [False]

    def plot_grid(index):
        ax.clear()
        alignment = alignments[index]
        rows, cols, depth = max([r for r, c, d in alignment]) + 1, max([c for r, c, d in alignment]) + 1, max([d for r, c, d in alignment]) + 1
        ax.set_title(f"Rows: {rows}, Columns: {cols}, Depth: {depth}")
        for r in range(rows):
            for c in range(cols):
                for d in range(depth):
                    idx = r * cols * depth + c * depth + d
                    if primes[idx]:
                        ax.scatter(r, c, d, c='r', marker='o')
                    else:
                        ax.scatter(r, c, d, c='b', marker='x')
        if show_line[0]:
            line_x, line_y, line_z = zip(*alignment)
            ax.plot(line_x, line_y, line_z, c='g')
        plt.draw()

    def on_key(event):
        if event.key == 'right':
            current_index[0] = (current_index[0] + 1) % len(alignments)
            show_line[0] = False
            plot_grid(current_index[0])
        elif event.key == 'up':
            show_line[0] = True
            plot_grid(current_index[0])
        elif event.key == 'escape':
            plt.close(fig)

    plot_grid(current_index[0])
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

def main():
    limit = 100  # You can change this limit to generate more numbers
    angle = 89  # Maximum angle to check for curves
    alignments = find_alignments(limit, angle)

    if alignments:
        print(f"Prime numbers align in the following 3D grid configurations for limit {limit}:")
        for alignment in alignments:
            rows, cols, depth = max([r for r, c, d in alignment]) + 1, max([c for r, c, d in alignment]) + 1, max([d for r, c, d in alignment]) + 1
            print(f"Rows: {rows}, Columns: {cols}, Depth: {depth}")
        
        visualize = input("Do you want to visualize the alignments? (yes/no): ").strip().lower()
        if visualize == 'yes':
            print("Press the right arrow key to go to the next pattern, up arrow key to show the alignment line, and ESC to stop visualizations.")
            visualize_alignments(alignments, limit)
    else:
        print(f"No alignments found for limit {limit}.")

if __name__ == "__main__":
    main()