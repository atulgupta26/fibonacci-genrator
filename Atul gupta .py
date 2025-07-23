def fibonacci_series(n):
    """Return the Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
num_terms = 10
print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci_series(num_terms))