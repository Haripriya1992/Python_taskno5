from functools import reduce

fibonacci = lambda n: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]],
    range(n - 2),
    [0, 1]
)[:n]

n = int(input("Enter number of terms: "))
print(f"Fibonacci series up to {n} terms:")
print(fibonacci(n))